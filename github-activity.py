#!/usr/bin/env python3

import urllib.request
import json
import sys
from handlers import dispatch

def fetch_activity(username):
    url = f"https://api.github.com/users/{username}/events"

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            data = response.read()
            return json.loads(data)
    except Exception as e:
        print(f"Error: {e}")
        return []
try:    
    user = sys.argv[1]
except IndexError:
    print("Error: A username must be provided as an argument.")
    sys.exit()

if len(sys.argv)>2:
    print("Error: Too many arguments provided. Please provide a single username.")
    sys.exit()

user_activities = fetch_activity(user)
for event in user_activities:
    dispatch(event)