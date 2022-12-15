
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
response_Keys = list(response.keys())

def JsonPrint(response_Keys):
    for i in response_Keys:

        if type(response[i]) == dict:
            # JsonPrint(response_Keys)
            print(i, '->', response[i])
            print()

        elif type(response[i]) == list:
            for j in range(len(response[i])):
                print(f'{i[:-1]} {j+1} ->', response[i][j])
                print()

        else:
            print(i, '->', response[i])

JsonPrint(response_Keys)
