import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

credentials = None
__G_DRIVE_TOKEN_FILE = "token.pickle"
__OAUTH_SCOPE = ["https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube.readonly",
    "https://www.googleapis.com/auth/youtube.force-ssl",
]
if os.path.exists(__G_DRIVE_TOKEN_FILE):
    with open(__G_DRIVE_TOKEN_FILE, "rb") as f:
        credentials = pickle.load(f)
        if (
            (credentials is None or not credentials.valid)
            and credentials
            and credentials.expired
            and credentials.refresh_token
        ):
            credentials.refresh(Request())
else:
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", __OAUTH_SCOPE)
    credentials = flow.run_local_server(port=0, open_browser=False)

# Save the credentials for the next run
with open(__G_DRIVE_TOKEN_FILE, "wb") as token:
    pickle.dump(credentials, token)
