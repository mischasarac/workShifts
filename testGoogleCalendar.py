from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

# The API you want to use (Google Calendar in this case)
SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google_account():
    """Handles the OAuth 2.0 authorization flow and returns credentials."""
    # Make sure the redirect URI in this code matches the one registered in Google Cloud Console
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json',  # Path to your client secrets file
        scopes=SCOPES,
        redirect_uri='http://localhost:8080/'  # Ensure this is the same URI registered in the console
    )
    
    credentials = flow.run_local_server(port=8080)
    
    return credentials

def get_calendar_service(credentials):
    """Returns a Google Calendar service object."""
    service = build('calendar', 'v3', credentials=credentials)
    return service

def list_upcoming_events(service):
    """Lists the upcoming events from Google Calendar."""
    # Call the Calendar API
    events_result = service.events().list(
        calendarId='primary', timeMin='2025-03-24T00:00:00Z', maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    
    events = events_result.get('items', [])
    
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(f"{event['summary']} at {start}")

def main():
    """Main function to authenticate and get calendar events."""
    credentials = authenticate_google_account()
    
    # Get the calendar service
    service = get_calendar_service(credentials)
    
    # List upcoming events
    list_upcoming_events(service)

if __name__ == '__main__':
    main()
