# Been_to_it

This is a web application which allow to show data stored in Google Sheet and manipulate them.
This software is written by Fabrizio Waldner and it is not related in any way with Google.

The web application is born to show a Wedding invite and register the guest's attendance in a Google spreadsheet. Moreover, the web application uses data stored in the spreadsheet to show a proper invite to the guest.
It does not make use of the Google Sheets API because a proper authorization was needed. To have a proper authorization you need to publish your app by abiding by all the rules to be published.
Indeed, publishing an app is designed for whom wants make it available to everyone.
In my case, I just wanted to sync my private spreadsheet with my web application.

## App scripts


To sync the content, you need to set up a script in your Google Spreadsheet.
The script POST data in the web application.

```javascript
// url is the URL of the web application to sync. Something like https://HOSTNAME/api/cache.
// secret is an arbitrary password shared between the web application and this script to avoid bad actors uploading the data.
function syncCache(url, secret) {
  var spreadsheet = SpreadsheetApp.getActiveSheet();
  var values = spreadsheet.getRange("A1:O100").getValues();
  // Make a POST request with a JSON payload.
  var data = {
    'values': JSON.stringify(values)
  };
  var options = {
    'method' : 'post',
    'contentType': 'application/json',
    'headers': {
      'Authorization': secret
    },
    'payload' : JSON.stringify(data)
  };
  var response = UrlFetchApp.fetch(url, options);
  Logger.log(response.getContentText());
  valuesToWrite = JSON.parse(response.getContentText());
  for (const [cell, value] of Object.entries(valuesToWrite.cache)) {
    console.log(`Writing ${cell}: ${value}`);
    spreadsheet.getRange(cell).setValue(value);
  }
}
```


## Execution

To bring up the web application you need `docker` with  `docker-compose` plugin.
You can find an installation guide [here](https://docs.docker.com/engine/install/debian/#install-using-the-repository).

An env file is needed to populate some variable in the stack file. 
Create a file in `~/.docker/been_to_it-dev.env` with this structure:

```
CACHE_TOKEN=<same secret used in the Apps Scripts>
```

To run a developping version of the web server run:

```
$ docker/lib/createLocalDevStack.sh
```

It will build and bring ups all the jobs. The code will automatically be rebuilt if a change is detected.

If you want to run localhost version of the webapplication just run:

```
$ docker/lib/createLocalStack.sh
```
