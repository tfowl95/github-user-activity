#!/usr/bin/env python3

import urllib.request
import json

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
    
response = fetch_activity("tfowl95")
for object in response:
    print(json.dumps(object, indent = 4))
print()