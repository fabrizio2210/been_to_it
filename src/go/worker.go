package main

import (
    "context"
    "encoding/json"
    "fmt"
    "io/ioutil"
    "log"
    "net/http"
    "os"
    "strconv"
    "time"

    "github.com/go-redis/redis/v8"
    "golang.org/x/oauth2"
    "golang.org/x/oauth2/google"
    "google.golang.org/api/option"
    "google.golang.org/api/sheets/v4"
)
var (
  spreadsheetId = "1uyKtjMczCQVUfR2ZRwDWW8iKupxp6k1TP_6xQrmiNXA"
  readRange = "Invitati!A1:K100"
)

type Token struct {
    Token string
    Refresh_Token string
    Token_Uri string
    Client_Id string
    Client_Secret string
    Scopes []string
    Expiry string
}

type Credentials struct {
    Client_Id string
    Project_Id string
    Auth_Uri string
    Token_Uri string
    Auth_Provider_X509_Cert_Url string
    Client_Secret string
    Redirect_Uris []string
}

type CredStore struct {
	Installed Credentials
}

var redisClient = redis.NewClient(&redis.Options{
  Addr: os.Getenv("REDIS_HOST") + ":6379",
})

func createTokenFile() {
	token := Token {
		Token: "xxx",
		Refresh_Token: os.Getenv("REFRESH_TOKEN"),
		Token_Uri: "https://oauth2.googleapis.com/token",
		Client_Id: os.Getenv("CLIENT_ID"),
		Client_Secret: os.Getenv("CLIENT_SECRET"),
		Scopes: []string{"https://www.googleapis.com/auth/spreadsheets"},
		Expiry: "2023-03-14T20:36:21.226655Z",
	}
		
	file, _ := json.MarshalIndent(token, "", " ")
	_ = ioutil.WriteFile("token.json", file, 0644)
}

func createCredentialsFile() {
	credentials := CredStore {
		Installed: Credentials{
			Client_Id: os.Getenv("CLIENT_ID"),
			Project_Id: os.Getenv("PROJECT_ID"),
			Auth_Uri: "https://accounts.google.com/o/oauth2/auth",
			Token_Uri: "https://oauth2.googleapis.com/token",
			Auth_Provider_X509_Cert_Url: "https://www.googleapis.com/oauth2/v1/certs",
			Client_Secret: os.Getenv("CLIENT_SECRET"),
			Redirect_Uris: []string{"http://localhost"},
		},
	}
	file, _ := json.MarshalIndent(credentials, "", " ")
	 _ = ioutil.WriteFile("credentials.json", file, 0644)
}

// Retrieve a token, saves the token, then returns the generated client.
func getClient(config *oauth2.Config) *http.Client {
	// The file token.json stores the user's access and refresh tokens, and is
	// created automatically when the authorization flow completes for the first
	// time.
	tokFile := "token.json"
	tok, err := tokenFromFile(tokFile)
	if err != nil {
		tok = getTokenFromWeb(config)
		saveToken(tokFile, tok)
	}
	return config.Client(context.Background(), tok)
}

// Request a token from the web, then returns the retrieved token.
func getTokenFromWeb(config *oauth2.Config) *oauth2.Token {
        authURL := config.AuthCodeURL("state-token", oauth2.AccessTypeOffline)
        fmt.Printf("Go to the following link in your browser then type the "+
                "authorization code: \n%v\n", authURL)

        var authCode string
        if _, err := fmt.Scan(&authCode); err != nil {
                log.Fatalf("Unable to read authorization code: %v", err)
        }

        tok, err := config.Exchange(context.TODO(), authCode)
        if err != nil {
                log.Fatalf("Unable to retrieve token from web: %v", err)
        }
        return tok
}

// Retrieves a token from a local file.
func tokenFromFile(file string) (*oauth2.Token, error) {
        f, err := os.Open(file)
        if err != nil {
                return nil, err
        }
        defer f.Close()
        tok := &oauth2.Token{}
        err = json.NewDecoder(f).Decode(tok)
        return tok, err
}

// Saves a token to a file path.
func saveToken(path string, token *oauth2.Token) {
        fmt.Printf("Saving credential file to: %s\n", path)
        f, err := os.OpenFile(path, os.O_RDWR|os.O_CREATE|os.O_TRUNC, 0600)
        if err != nil {
                log.Fatalf("Unable to cache oauth token: %v", err)
        }
        defer f.Close()
        json.NewEncoder(f).Encode(token)
}

func toChar(i int) string {
    return string('A' + i)
}

func writeToSheet(ctx context.Context) {
  for {
    cellToWrite, err := redisClient.LPop(ctx, "write_queue").Result()
    if err != nil {
      break
    }
    fmt.Printf("Read value from queue: %v\n", cellToWrite)
    valueToWrite, err := redisClient.Get(ctx, cellToWrite).Result()
    fmt.Printf("Value to write is:%v\n", valueToWrite)

    b, err := os.ReadFile("credentials.json")
    if err != nil {
      log.Fatalf("Unable to read client secret file: %v", err)
    }

    // If modifying these scopes, delete your previously saved token.json.
    config, err := google.ConfigFromJSON(b, "https://www.googleapis.com/auth/spreadsheets")
    if err != nil {
      log.Fatalf("Unable to parse client secret file to config: %v", err)
    }
    apiClient := getClient(config)

    srv, err := sheets.NewService(ctx, option.WithHTTPClient(apiClient))
    if err != nil {
      log.Fatalf("Unable to retrieve Sheets client: %v", err)
    }

    var vr sheets.ValueRange
    myval := []interface{}{valueToWrite}
    vr.Values = append(vr.Values, myval)
    _, err = srv.Spreadsheets.Values.Update(spreadsheetId, cellToWrite, &vr).ValueInputOption("RAW").Context(ctx).Do()
    if err != nil {
      log.Fatalf("Unable to write data to sheet: %v", err)
    }
  }
}

func readFromSheet(ctx context.Context) {
  fmt.Println("Reading from Sheet...")
  b, err := os.ReadFile("credentials.json")
  if err != nil {
    log.Fatalf("Unable to read client secret file: %v", err)
  }

  // If modifying these scopes, delete your previously saved token.json.
  config, err := google.ConfigFromJSON(b, "https://www.googleapis.com/auth/spreadsheets.readonly")
  if err != nil {
    log.Fatalf("Unable to parse client secret file to config: %v", err)
  }
  apiClient := getClient(config)

  srv, err := sheets.NewService(ctx, option.WithHTTPClient(apiClient))
  if err != nil {
    log.Fatalf("Unable to retrieve Sheets client: %v", err)
  }

  resp, err := srv.Spreadsheets.Values.Get(spreadsheetId, readRange).Do()
  if err != nil {
    log.Fatalf("Unable to retrieve data from sheet: %v", err)
  }

  if len(resp.Values) == 0 {
    fmt.Println("No data found.")
  } else {
    for r, row := range resp.Values {
      for c :=0 ; c < 100; c++ {
        var value interface{}
        value = ""
        if c < len(row) {
          value = row[c]
        }
        redisClient.Set(ctx, fmt.Sprintf("%s%d", toChar(c), r + 1), value, 0)
      }
    }
  }
}

func main() {
  ctx := context.Background()
	createCredentialsFile()
	createTokenFile()
  intervall_time, err := strconv.Atoi(os.Getenv("SYNC_INTERVAL_SECONDS"))
  if err != nil {
    panic(err)
  }

  for {
    redisClient.Set(ctx, "write_lock", 1, 5 * time.Second)
    writeToSheet(ctx)
    readFromSheet(ctx)
    redisClient.Set(ctx, "write_lock", 0, 0)
    time.Sleep(time.Duration(intervall_time) * time.Second)
  }
}

