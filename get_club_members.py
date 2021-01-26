import requests
import json
import strava_sdk as ssdk

credentials = ssdk.getCredentials()
access_tokens = ssdk.getTokens()

# Make Strava auth API call with your 
# client_code, client_secret and code
url_mask = "https://www.strava.com/api/v3/clubs/{0}/members?access_token={1}"
response = requests.get(
                    url = url_mask.format(credentials['club_id'],access_tokens['access_token'])
                )

#Save json response as a variable
strava_response = response.json()
# Save tokens to file
with open(ssdk.path_club, 'w') as outfile:
    json.dump(strava_response, outfile)


