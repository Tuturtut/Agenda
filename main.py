from __future__ import print_function

import datetime
import os.path
import sys


from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

# id of the choser calandar
# Use 'primary' for the default one
# Id of the 'IUT' calendar
# IUT id : e6640acb143e779764fab8e6d6eff54b9fc80608aa4b422a6ca92037976c2734@group.calendar.google.com
chosen_calandar = 'e6640acb143e779764fab8e6d6eff54b9fc80608aa4b422a6ca92037976c2734@group.calendar.google.com'


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Add an event to the calendar with a duration of 1 hour and a description
    try:
        if sys.argv[1] == "add":
            addEvent(creds, sys.argv[2], sys.argv[3])
    except IndexError:
        print("Error: missing arguments")
        print("Usage: python main.py add <duration> <description>")
        addEvent(creds, 1, "Test")


def addEvent(creds, duration, description):
    start = datetime.datetime.utcnow()

    end = datetime.datetime.utcnow() + datetime.timedelta(hours=int(duration))
    start_formatted = start.isoformat() + 'Z'
    end_formatted = end.isoformat() + 'Z'

    event = {
        'summary': description,
        'start': {
            'dateTime': start_formatted,
            'timeZone': 'Europe/Paris',
        },
        'end': {
            'dateTime': end_formatted,
            'timeZone': 'Europe/Paris',
        },
    }

    service = build('calendar', 'v3', credentials=creds)
    event = service.events().insert(calendarId=chosen_calandar, body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))


if __name__ == '__main__':
    main()
