import strava_sdk as ssdk
import requests
import json

access_tokens = ssdk.getTokens()

# Make Strava auth API call with your 
# client_code, client_secret and code
url_mask = "https://www.strava.com/api/v3/athlete/activities?access_token={0}&per_page=200&include_all_efforts=true"
response = requests.get(
                    url = url_mask.format(access_tokens['access_token'])
                )

#Save json response as a variable
strava_response = response.json()
# Save tokens to file
with open(ssdk.path_activities, 'w') as outfile:
    json.dump(strava_response, outfile)


