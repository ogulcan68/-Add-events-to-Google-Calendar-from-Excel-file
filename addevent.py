# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 20:42:12 2020

@author: D. Ogulcan CELIK
"""
from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE = 'CLIENT SECRET FILE.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

calendar_id_dersp = 'CALENDAR ID'

"""
event oluşturma
"""
colors = service.colors().get().execute()
pprint(colors)

def event(name, date, desc):
    event_request_body = {
        'summary': name,
        'description': desc,
        'start': {
        'dateTime': date,
        'timeZone': 'Africa/Addis_Ababa',
        },
        'end': {
        'dateTime': date,
        'timeZone': 'Africa/Addis_Ababa',
        },
        'colorId' : 5,
        'status' : 'confirmed',
        'transparency' : 'opaque',
        'visibility' : 'private',
        'location' : 'Turkey, Ankara',
        'attachments' : [
            {
                'fileUrl' : '  ',
                'title' : 'Invitation Letter Tamplate in Word Doc'
            }    
        ],
        'attendees' : [
            {
                'displayName' : 'Ogulcan',
                'comment' : 'I enjoy coding',
                'email' : 'davutogulcancelik@gmail.com',
                'optional': False,
                'organizer' : True,
                'responseStatus' : 'accepted'
            }    
        ]
    
    }
    
    
    maxAttendees = 5
    sendNotification = True
    sendUpdate = 'none'
    supportsAttachments = True
    
    response = service.events().insert(
        calendarId=calendar_id_dersp,
        maxAttendees=maxAttendees,
        sendNotifications=sendNotification,
        sendUpdates=sendUpdate,
        supportsAttachments=supportsAttachments,
        body=event_request_body
    ).execute()
    
    def islem ():
        pprint(response)
        print("SUCCES!!!!!!!!")
    islem()