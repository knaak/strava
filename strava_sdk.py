import json
from os import path

path_tokens = "cache/strava_tokens.json"
path_credentials = "private/credentials.json"
path_club = 'cache/club_members.json'
path_activities = "cache/activities.json"

def getTokens():
    if (not path.exists(path_tokens)):
        print("create strava_tokens.json first")
        quit()

    with open(path_tokens, 'r') as ftokens:
        access_tokens = json.load(ftokens)

    return access_tokens

def getCredentials():
    with open(path_credentials, 'r') as credentials:
        credential = json.load(credentials)
    return credential

def getActivityPath(activityid):
    return str.format("cache/activity_{0}.json", activityid)

def getSegmentInstancePath(segmentid):
    return str.format("cache/segment_instance_{0}.json", segmentid)

def getSegmentPath(segmentid):
    return str.format("cache/segment_{0}.json", segmentid)
