# Been_to_it

This is a web application which allow to show data stored in Google Sheet and manipulate them.

This software is written by Fabrizio Waldner and it is not related in any way with Google.


## App scripts


To sync the content, you need to set up a script in your Google Spreadsheet.
The script POST data in the web application.

```
// url is the URL of the web application to sync.
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
