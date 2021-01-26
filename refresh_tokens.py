import requests
import json
import time
import strava_sdk as ssdk


with open(ssdk.path_tokens) as json_file:
    strava_tokens = json.load(json_file)

if not strava_tokens['expires_at'] < time.time():
    print("Tokens not expired")
    quit()

credential = ssdk.getCredentials()
response = requests.post(
                    url = 'https://www.strava.com/oauth/token',
                    data = {
                        'client_id': credential['client_id'],
                        'client_secret': credential['client_secret'],
                        'code': credential['code'],
                        'grant_type': 'authorization_code'
                        }
                )

new_strava_tokens = response.json()

if (not response.ok):
    print("Error refreshing token")
    print(new_strava_tokens)
    quit()

with open(ssdk.path_tokens, 'w') as outfile:
    json.dump(new_strava_tokens, outfile)

with open('strava_tokens.json') as check:
    data = json.load(check)
    print(data)

print("done")