#######################################################################################
# Yourname: Nattanon
# Your student ID: Vongnongvang
# Your GitHub Repo: https://github.com/endphaze/NPA2023-Final.git

#######################################################################################
# 1. Import libraries for API requests, JSON formatting, time, and (restconf_final or netconf_final).

import requests
import json
import time

from restconf_final import create, delete, enable, disable, status
#######################################################################################
# 2. Assign the Webex hard-coded access token to the variable accessToken.

accessToken = "Bearer NTQwZDk2MzYtYzRhNy00YTNlLTliZDQtNGE2MzJlNjY4MzcyYzJjZDc2OWMtNzZl_P0A1_bc884c7a-820b-497b-8b60-00b4d15ea95d"

#######################################################################################
# 3. Prepare parameters get the latest message for messages API.

# Defines a variable that will hold the roomId
roomIdToGetMessages = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNjIwNmJkNjAtNWU5ZC0xMWVmLWEyM2MtNzFiOTEzZDZjMzU3" # ADD

while True:
    # always add 1 second of delay to the loop to not go over a rate limit of API calls
    time.sleep(1)

    # the Webex Teams GET parameters
    #  "roomId" is the ID of the selected room
    #  "max": 1  limits to get only the very last message in the room
    getParameters = {"roomId": roomIdToGetMessages, "max": 1}

    # the Webex Teams HTTP header, including the Authoriztion
    getHTTPHeader = {"Authorization": accessToken} # Add

# 4. Provide the URL to the Webex Teams messages API, and extract location from the received message.
    
    # Send a GET request to the Webex Teams messages API.
    # - Use the GetParameters to get only the latest message.
    # - Store the message in the "r" variable.
    r = requests.get(
        "https://webexapis.com/v1/messages", # Add
        params=getParameters, # Add
        headers=getHTTPHeader, # Add
    )
    
    # verify if the retuned HTTP status code is 200/OK
    if not r.status_code == 200:
        raise Exception(
            "Incorrect reply from Webex Teams API. Status code: {}".format(r.status_code)
        )

    # get the JSON formatted returned data
    json_data = r.json()
    
    # check if there are any messages in the "items" array
    if len(json_data["items"]) == 0:
        raise Exception("There are no messages in the room.")

    # store the array of messages
    messages = json_data["items"]
    
    # store the text of the first message in the array
    message = messages[0]["text"]
    print("Received message: " + message)

    # check if the text of the message starts with the magic character "/" followed by your studentID and a space and followed by a command name
    #  e.g.  "/66070123 create"
    if message.find("/65070018") == 0: # Add
        
        # extract the command
        command = message.split(" ", 1) # Add
        command = command[1] # Add
        print(command)

# 5. Complete the logic for each command

        if command == "create":
            responseMessage = create() # Add 
        elif command == "delete":
            responseMessage = delete() # Add
        elif command == "enable":
            responseMessage = enable() # Add
        elif command == "disable":
            responseMessage = disable() # Add
        elif command == "status":
            responseMessage = status() # Add
        else:
            responseMessage = "Error: No command or unknown command"
        
# 6. Complete the code to post the message to the Webex Teams room.
        
        # the Webex Teams HTTP headers, including the Authoriztion and Content-Type
        postHTTPHeaders = HTTPHeaders = {"Authorization": accessToken, "Content-Type": "application/json"} # Add

        # The Webex Teams POST JSON data
        # - "roomId" is is ID of the selected room
        # - "text": is the responseMessage assembled above
        postData = {"roomId": roomIdToGetMessages, "text": responseMessage} # Add

        # Post the call to the Webex Teams message API.
        r = requests.post(
            "https://webexapis.com/v1/messages", # Add
            data=json.dumps(postData), # Add
            headers=postHTTPHeaders, # Add
        )
        if not r.status_code == 200:
            raise Exception(
                "Incorrect reply from Webex Teams API. Status code: {}".format(r.status_code)
            )