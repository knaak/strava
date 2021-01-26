import json
import os.path
from os import path
import strava_sdk as ssdk

def extractData(data):
    return {
        "id": data["id"],
        "name": data["name"],
        "pr":   int(data["athlete_segment_stats"]["pr_elapsed_time"]),
        "pr_activity_id" : data["athlete_segment_stats"]["pr_activity_id"],
        "kom": int(ssdk.hourandMinuteToSeconds(data["xoms"]["kom"])),
        "qom": int(ssdk.hourandMinuteToSeconds(data["xoms"]["qom"])),
        "starred" : data["star_count"],
        "athletes" : int(data["athlete_count"]),
        "attempts" : data["effort_count"]
        }

    


statistics = dict()
for filename in os.listdir("cache"):
    if ("segment" not in filename): continue
    if ("instance" in filename): continue

    with (open("cache/" + filename) as jsonfile):
        data = json.load(jsonfile)

        d = extractData(data)
        statistics[d["name"]] = d


with (open("data/run.json", "w") as file): 
    json.dump(statistics, file)
        
for stat in statistics:
    distance_in_seconds = 5
    mininum_athletes = 50

    item = statistics[stat]    

    if (item['pr'] < 0): continue
    if (item['kom'] < 0): continue

    distance_to_kom = item["pr"] - item["kom"]
    #distance_to_qom = item["pr"] - item["qom"]

    if (distance_to_kom <= 0):
        print("You have this KOM", item["name"])
        continue
    
    percent_to_kom = item["kom"] / item["pr"]

    
    result = list()
    result.append(str.format("Opportunity detected: {0} click here to review: {1}",
        item["name"],
        str.format("https://www.strava.com/segments/{0}?filter=overall",
                        item["id"])
        ))

    if (distance_to_kom <= distance_in_seconds):
        result.append(str.format("You are within {0} seconds of KOM (pr:{1} sec, kom:{2} sec)", 
            distance_to_kom,
            item["pr"], item["kom"]))

    if (percent_to_kom > 0.9):
        result.append(str.format("You are within {0} seconds of KOM (pr:{1} sec, kom:{2} sec)", 
            distance_to_kom,
            item["pr"], item["kom"]))

    
    #if (distance_to_qom <= distance_in_seconds):
    #    result.append(str.format("You are within {0} seconds of QOM (pr:{1} sec, qom:{2} sec)", 
    #        distance_in_seconds,
    #        item["pr"], item["qom"]))

    if (item["athletes"] <= mininum_athletes):
        result.append(str.format("Only {0} atheletes all-time, you can take them!", 
            item["athletes"]))        

    if (len(result)> 1):
        print (result)
        print("-------------\n")



        

        

        

