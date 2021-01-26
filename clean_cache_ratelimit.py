import json
import os.path
from os import path

for filename in os.listdir("cache"):
    with (open("cache/" + filename) as jsonfile):
        data = json.load(jsonfile)

        try:
            message = data["message"]

            if (message.startswith("Rate Limit Exceeded")):
                print("will remove:", filename)
                os.remove("cache/"+filename)
        except:
            continue
        

    


