from urllib2 import Request, urlopen
import json

url = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/ddomokunn,theflyingrock?api_key=a87458ef-570a-4509-98d8-f7f0c30b183b'

req = Request(url)
response = urlopen(req)
result = response.read()

summonerName = raw_input('\n Input your summoner name: ')

if type(summonerName) != type('s'):
	summonerName = str(summonerName)

d = json.loads(result)
summName = d[summonerName]['name']
summId = d[summonerName]['id']

print json.dumps(d, sort_keys=True, indent=4, separators=(',', ': '))

url2 = 'https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/' + str(summId) + '?api_key=a87458ef-570a-4509-98d8-f7f0c30b183b'
req = Request(url2)
response = urlopen(req)
result = response.read()
d = json.loads(result)
print json.dumps(d.values(), sort_keys=True, indent=4, separators=(',', ': '))


