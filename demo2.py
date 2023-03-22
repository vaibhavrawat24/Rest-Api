import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta
from dateutil import tz

# Set up the API client object
creds, project = google.auth.default(scopes=['https://www.googleapis.com/auth/fitness.heart_rate.read'])
service = build('fitness', 'v1', credentials=creds)

# Set the start and end times for the query (last week)
to_time = datetime.now(tz.tzlocal())
from_time = to_time - timedelta(days=7)

# Build a request for step count data
request = {
    "aggregateBy": [{
        "dataTypeName": "com.google.step_count.delta",
        "dataSourceId": "derived:com.google.step_count.delta:com.google.android.gms:estimated_steps"
    }],
    "bucketByTime": {
        "durationMillis": 86400000
    },
    "startTimeMillis": int(from_time.timestamp() * 1000),
    "endTimeMillis": int(to_time.timestamp() * 1000)
}

# Retrieve the step count data
try:
    response = service.users().dataset().aggregate(userId='me', body=request).execute()
    print(response)
except HttpError as error:
    print(f'An error occurred: {error}')

