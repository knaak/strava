import requests
from pandas.io.json import json_normalize
import json
import csv
import strava_sdk as ssdk
import time

import os.path
from os import path

access_tokens = ssdk.getTokens()

def downloadSegmentInstanceData(segment):
    with open(ssdk.getSegmentInstancePath(segment["id"]), 'w') as outfile:
        print("writing segment", segment['id'])
        json.dump(segment, outfile)
        

with open(ssdk.path_activities) as json_file:
    activities = json.load(json_file)

url_mask = "https://www.strava.com/api/v3/activities/{0}?access_token={1}&include_all_efforts=true"
for activity in activities:
    activity_id = activity["id"]
    if (not path.exists(ssdk.getActivityPath(activity_id))): 
        response = requests.get(
                    url = url_mask.format(activity_id, access_tokens['access_token'])
                )
        detailed_activity = response.json()
        
        if (not response.ok):
            print("Error downloading", activity_id)
            if (ssdk.isRateLimited(detailed_activity)):
                print("Rate limited, sleeping for 15 minutes")
                time.sleep(1000)
            continue
    
        for segment in detailed_activity["segment_efforts"]:
            if (not path.exists(ssdk.getSegmentInstancePath(segment['id']))):
                downloadSegmentInstanceData(segment)

        #writes cache to ensure we don't reprocess
        with open(ssdk.getActivityPath(activity_id), 'w') as outfile:
            print("writing", activity_id)
            json.dump(detailed_activity, outfile) 
    else:
        print("skipping", activity_id)

print("all done")

