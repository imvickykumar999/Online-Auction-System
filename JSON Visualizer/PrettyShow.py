
import requests, json

BaseURL = "https://www.googleapis.com/youtube/v3/search?"
part = "part=" + "snippet"
q = "&q=" + "imvickykumar999"
key = "&key=" + "AIzaSyCcJX4qdbo9caqxZSKDmuBjNVWfvq8_Wcs"
maxResults = "&maxResults=" + "20"

payload={}
headers = {}
url = BaseURL + part + q + key + maxResults
response = requests.request("GET", url, headers=headers, data=payload)

response = response.text
response = json.loads(response)
response = dict(response)

def JsonPrint(response, response_Keys):
    print()
    print(response_Keys)
    for i in range(len(response_Keys)):

        if type(response[response_Keys[i]]) == dict:
            JsonPrint(response[response_Keys[i]], list(response[response_Keys[i]].keys()))

        elif type(response[response_Keys[i]]) == list:
            print()
            for j in range(len(response_Keys[i])):
                # print(response_Keys)
                print()

        else:
            print(response_Keys[i], '->', response[response_Keys[i]])


JsonPrint(response, list(response.keys()))
