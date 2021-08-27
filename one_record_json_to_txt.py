# This script will ask for a record attatched to REDCap project
# LIANNE DESTROY ME and output it in "flat" format to a given
# file
import requests, json

# API request constants
api_url = "https://redcap.iths.org/api/"
api_key = ""
with open("keys/lianne_destroy_me.txt", "r") as f:
    api_key = f.read()

dataReq = {
    'token': api_key,
    'content': "record",
    'format': "json",
    'type': "flat",
    'returnFormat': "json",
    'records[0]': "1020524",
}

# test print
print("Program initialized.\n")

# handle text file creation
recordName = ""
recordName = int(input("What record would you like to export (INO)? "))
dataReq['records[0]'] = str(recordName)
outputName = input("What would you like the text file to be named? ")
text_file = open(outputName, "w")
# text_file2 = open(outputName + "Dumps", "w")

# API request
project = requests.post(api_url, data=dataReq)
print("HTTP status: " + str(project.status_code))
recordJSON = project.json()

print("This is the raw json from the project before .json:\n")
print(project)

print("This is the json after .json formatting:\n")
print(recordJSON)

# json formatting
formattedJSON = json.dumps(recordJSON)
print(json.dumps(recordJSON, sort_keys=True, indent=4))

# json into text file
n = text_file.write(formattedJSON)
# o = text_file2.write(recordJSON)
text_file.close()

