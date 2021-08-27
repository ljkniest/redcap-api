# this version of the script will pull all records from the database
# and re-input each with the new records receiving sequential record
# ID's (INO's) starting with the first available one.

import requests, json, time

# API request constants
api_url = "https://redcap.iths.org/api/"
projectName = ""
api_key = ""
dataReq = {
    'token': api_key,
    'content': "record",
    'format': "json",
    'type': "flat",
    'returnFormat': "json"
}

# test print
print("Program initialized.")
time.sleep(1)

# ask for project input
projectEstablished = False
while not projectEstablished:
    projectName = input("What project do you want to modify? ")
    print("\nIs this your project (y/n)? " + projectName)
    verified = False
    while not verified:
        projectCorrect = input()
        if(projectCorrect.lower() == "y"):
            verified = True
            projectEstablished = True
        elif(projectCorrect.lower() == "n"):
            verified = True
        else:
            print("Invalid input. Is this your project (y/n)? " + projectName)           

# API request
projectName = "./keys/" + projectName
print(projectName)
with open(projectName, 'r') as f:
    api_key = f.read()
dataReq['token'] = api_key
print("token: " + dataReq.get('token'))
project = requests.post(api_url, data=dataReq)
print("HTTP status: " + str(project.status_code))

# format JSON
projectJSON = project.json()
formattedJSON = json.dumps(projectJSON)

print("Record grabbed. Here is the output format:\n")
time.sleep(1)
print(formattedJSON)

# re-structure dataReq
dataReq = {
    'token': api_key,
    'content': "record",
    'format': "json",
    'type': "flat",
    'overwriteBehavior': "normal",
    'forceAutoNumber': "true",
    'returnFormat': "json",
    'data': formattedJSON,
}

print("Attempting to input record.")

project = requests.post(api_url, data=dataReq)
print("HTTP status: " + str(project.status_code))


