
import requests, json

# ---------------------------

BaseURL = "https://www.googleapis.com/youtube/v3/search?"
part = "part=" + "snippet"
q = "&q=" + "imvickykumar999"
key = "&key=" + "AIzaSyCcJX4qdbo9caqxZSKDmuBjNVWfvq8_Wcs"
maxResults = "&maxResults=" + "20"

# comment any 1 line of 2 urls to test upon
url = BaseURL + part + q + key + maxResults
url = "https://raw.githubusercontent.com/imvickykumar999/Postman-30-Days-Challenge/master/Day%2001%3A%20Fork%20a%20collection/Day%2001-%20Fork%20a%20collection.postman_collection.json"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
response = response.text
response = json.loads(response)
response = dict(response)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(response, f, ensure_ascii=False, indent=4)

# ---------------------------------

response = open('data.json')
response = json.load(response)

import CallPretty as cp
cp.JsonPrint(response, list(response.keys()))
