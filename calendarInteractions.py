import os
import pickle
import datetime
from htmlParser import getShifts
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# If modifying your shifts, you may need to specify the correct scope
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Authenticate and create the service
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

# Function to add shift events to the calendar
def addShiftsToCalendar(shifts):
    service = authenticateGoogleAccount()
    
    for shift in shifts:
        event = {
            'summary': 'Shift',
            'location': 'Work',
            'description': 'Work shift for the day.',
            'start': {
                'dateTime': shift.strftime('%Y-%m-%dT%H:%M:%S'),
                'timeZone': 'Australia/Adelaide',
            },
            'end': {
                'dateTime': (shift + datetime.timedelta(hours=6)).strftime('%Y-%m-%dT%H:%M:%S'),
                'timeZone': 'Australia/Adelaide',
            },
            'reminders': {
                'useDefault': True,
            },
        }

        # Insert event into Google Calendar
        event_result = service.events().insert(calendarId='primary', body=event).execute()
        print(f"Event created: {event['summary']} at {event['start']['dateTime']}")
        # print("event created")



