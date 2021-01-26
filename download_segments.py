import requests
import json
import strava_sdk as ssdk

import os.path
from os import path

access_tokens = ssdk.getTokens()

for segment_data_filename in os.listdir("cache"):
    if (not segment_data_filename.startswith("segment_instance_")): continue

    with open("cache/"+segment_data_filename) as json_file:
        segment_instance = json.load(json_file)

    segment_id = segment_instance["segment"]["id"]

    if (path.exists(ssdk.getSegmentPath(segment_id))): 
        print("segment cache exists", segment_id)
        continue

    url_mask = "https://www.strava.com/api/v3/segments/{0}?access_token={1}"
    response = requests.get(url = url_mask.format(segment_id,access_tokens['access_token']))
    segment = response.json()

    if (not response.ok):
        print("error loading segment")
        if (segment["message"].startswith("Rate Limit Exceeded")): 
            print("Rate Limit Exceeded, wait 15 minutes and try again")
            break
        print("attempting to continue")
        continue

    with open(ssdk.getSegmentPath(segment_id), 'w') as outfile:
        print("writing", segment_id)
        json.dump(segment, outfile) 

    


