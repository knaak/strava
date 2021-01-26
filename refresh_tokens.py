import requests
import json
import time
import strava_sdk as ssdk

access_token = ssdk.getTokens()

if not access_token['expires_at'] < time.time():
    print("Tokens not expired")
    quit()

credential = ssdk.getCredentials()

response = requests.post(
                    url = 'https://www.strava.com/oauth/token',
                    data = {
                        'client_id': credential['client_id'],
                        'client_secret': credential['client_secret'],
                        'grant_type' : 'refresh_token',
                        'refresh_token' : access_token['refresh_token']
                        }
                )

new_strava_tokens = response.json()

if (not response.ok):
    print("Error refreshing token")
    print(new_strava_tokens)
    quit()

with open(ssdk.path_tokens, 'w') as outfile:
    json.dump(new_strava_tokens, outfile)

print("done")