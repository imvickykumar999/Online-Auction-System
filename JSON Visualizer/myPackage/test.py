
import json
import CallPretty as vix

response = open('JSON Visualizer/sample.json')
response = json.load(response)

vix.JsonPrint(response, list(response.keys()))
