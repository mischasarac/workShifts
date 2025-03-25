import os
import pickle
import datetime
from htmlParser import getShifts
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from datetime import datetime
import datetime as dt
import pytz 

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticateGoogleAccount():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens
    if os.path.exists('../storedData/token.pickle'):
        with open('../storedData/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # If there's no valid token, let the user log in and get the credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '../storedData/credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)
        
        # Save the credentials for the next run
        with open('../storedData/token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    service = build('calendar', 'v3', credentials=creds)
    return service


def validateNewShifts(shifts):
    service = authenticateGoogleAccount()
    
    now = dt.datetime.utcnow()  # Current time (naive, without timezone)
    events_result = service.events().list(
        calendarId='primary',
        timeMin=now.isoformat() + 'Z',  # Google requires UTC format
        maxResults=50,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    if not events:
        print("No upcoming events found.")
        return shifts  # If no calendar shifts, return all shifts

    # **Extract shift start times (naive datetime objects)**
    shiftEvents = set()
    for event in events:
        if event.get('summary') == 'Shift':
            start_time = event['start'].get('dateTime', event['start'].get('date'))
            parsed_time = datetime.strptime(start_time[:16], "%Y-%m-%dT%H:%M")  # Remove timezone part
            shiftEvents.add(parsed_time)

    if not shiftEvents:
        print("No upcoming shifts found.")
        return shifts  # If no shifts are found in Google Calendar, return all shifts

    # **Filter new shifts that are not in `shiftEvents`**
    new_shifts = [shift for shift in shifts if shift not in shiftEvents]
    return new_shifts