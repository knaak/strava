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
    item = statistics[stat]    

    distance_to_kom = item["pr"] - item["kom"]
    distance_to_qom = item["pr"] - item["qom"]

    
    result = list()
    result.append(str.format("Opportunity detected: {0} click here to review: {1}",
        item["name"],
        str.format("https://www.strava.com/segments/{0}?filter=overall",
                        item["id"])
        ))


    if (distance_to_kom <= 5):
        result.append(str.format("{0} withing 5 seconds of KOM (pr:{1}, kom:{2})", 
            item["name"],item["pr"], item["kom"]))
    
    #if (distance_to_qom <= 5):
    #    result.append(str.format("{0} withing 5 seconds of QOM (pr:{1}, qom:{2})", 
    #        item["name"],item["pr"], item["qom"]))

    if (item["athletes"] <= 50):
        result.append(str.format("{0} has only {1} atheletes all-time, you can take them!", 
            item["name"],item["athletes"]))

        print(item["name"],item["id"], "only has", item["athletes"], " athletes that have attempted, you can take them")

    if (len(result)> 1):
        print (result)



        

        

        

