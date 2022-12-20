
import json
import CallPretty as vix

response = open('sample.json')
response = json.load(response)

# import requests
# url = "https://arduino.esp8266.com/stable/package_esp8266com_index.json"
# payload={}
# headers = {}
# response = requests.request("GET", url, headers=headers, data=payload)
# response = response.text
# response = json.loads(response)
# response = dict(response)

vix.JsonPrint(response, list(response.keys()))
