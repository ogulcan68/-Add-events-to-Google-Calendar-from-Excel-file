# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 20:21:59 2020

@author: D. Ogulcan CELIK
"""

from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE = 'CLIENT SECRET NAME .json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

request_body = {
    'summary': ' NAME '    
}

response = service.calendars().insert(body=request_body).execute()