import requests
import json
import os.path
from os import path

import strava_sdk as ssdk

if (path.exists(ssdk.path_tokens)):
  print("delete strava_tokens.json first")
  quit()

with open('credentials.json', 'r') as credentials:
  credential = json.load(credentials)

for verifycredentials in ['client_id', 'client_secret', 'code']:
  if (credential[verifycredentials]) is None:
    print("Can't read", verifycredentials,"from credentials.json")
    quit()

# Make Strava auth API call with your 
# client_code, client_secret and code
response = requests.post(
                    url = 'https://www.strava.com/oauth/token',
                    data = {
                            'client_id': credential['client_id'],
                            'client_secret': credential['client_secret'],
                            'code': credential['code'],
                            'grant_type': 'authorization_code'
                            }
                )
#Save json response as a variable
strava_tokens = response.json()
# Save tokens to file
with open(ssdk.path_tokens, 'w') as outfile:
    json.dump(strava_tokens, outfile)

# Open JSON file and print the file contents 
# to check it's worked properly
with open(ssdk.path_tokens) as check:
  data = json.load(check)
print(data)