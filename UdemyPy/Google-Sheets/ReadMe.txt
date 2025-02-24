To Get Connectivity to a Spreadsheet on your Google Cloud, follow the below steps -
- Go to "console.cloud.google.com" and create a new project

- Click on "+ Enable APIs and Services"
- Search, Select and Enable "google drive api"
- After Enabling, "Create Credentials" with "Google Drive API" checking 'Application Data'
- Provide Service account details and "Create and Continue"
- Grant 'Project' and 'Editor' role

- Go to the Service account and click on the email link.
- Add Key, Create New Key, JSON --> Create

- Enable another API and Service = "Google sheets api"

- After enabling Sheets API, go to your google sheet and give permission to the Python Script's email (one found in JSON)
