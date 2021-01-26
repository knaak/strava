
Create the private directory, place a file called credentials.json in that folder with this format:
{
"client_id" : "<insertid>",
"client_secret" : "<insertid>",
"code" : "<insertid>",
"club_id" : "<insertid>"
}

Steps.

1. Run generate_tokens.py to build the strava_tokens.json file.
2. run "download_activities.py" to set the activities that you want to analyse.
3. run "download_segment_instances.py" to pull the segment data for each of your activities.
4. run "download_segments.py" to pull the global segment data for each of your segment instances.


Troubleshooting:

If you get rate limited or you mistakenly write cache files that are limited, use the clean_cache_ratelimit.py to remove.
If your tokens expire, trying running refresh tokens to get a new one.



helped by:
    https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86