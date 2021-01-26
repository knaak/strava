import json
import os.path
from os import path

for filename in os.listdir("cache"):
    with (open("cache/" + filename) as jsonfile):
        data = json.load(jsonfile)
        
        try:
            if (not data["message"]): continue
        except:
            continue

        message = data["message"]

        if (message.startswith("Rate Limit Exceeded")):
            jsonfile.close()
            os.remove("cache/"+filename)
            print("removed", filename)
            
        

    


