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

def hourandMinuteToSeconds(time):
    data = time.split(":")
    sum = 0
    count = 0
    factor = [1, 60, 3600]

    if (len(data) == 1):
        # remove that pesky "s" at the end
        return data[0][:len(data[0])-1]

    if (len(data)> 3):
        print("WARN: Time is too big, check strava_sdk hourMinuteToSeconds method")

    for item in reversed(data):
        sum = sum + (int(item) * factor[count])
        count = count +1
    return sum

def isRateLimited(data):
    try :
     if (data["message"].startswith("Rate Limit Exceeded")): 
         return True
    except:
        return False