import json
import http.client

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'fe36bb2ee42647c8ac011d129de5b700' }
connection.request('GET', 'https://api.football-data.org/v2/teams', None, headers)
# response = json.loads(connection.getresponse().read().decode())
js = connection.getresponse().read().decode()

response = json.loads(js)


print(js)