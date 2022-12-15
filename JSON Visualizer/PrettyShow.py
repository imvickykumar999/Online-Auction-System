
import requests, json

BaseURL = "https://www.googleapis.com/youtube/v3/search?"
part = "part=snippet"
q = "&q=imvickykumar999"
key = "&key=AIzaSyCcJX4qdbo9caqxZSKDmuBjNVWfvq8_Wcs"
maxResults = "&maxResults=20"

payload={}
headers = {}
url = BaseURL + part + q + key + maxResults
response = requests.request("GET", url, headers=headers, data=payload)

response = response.text
response = json.dumps(response)
response = json.loads(response)
print(response)