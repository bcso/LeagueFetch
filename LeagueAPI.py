from urllib2 import Request, urlopen
import json

class LeagueObject:
	def __init__(self):
		self.key = "a87458ef-570a-4509-98d8-f7f0c30b183b"

	def callMatchDict(self, summId):
		url = 'https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/' + str(summId) + '?api_key=' + self.key
		result = urlopen(Request(url)).read()
		matchDict = json.loads(result)
		return matchDict

	def callSummonerDict(self, summonerName):
		url = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/' + summonerName.lower() + '?api_key=' + self.key
		response = urlopen(Request(url)).read()
		summonerDict= json.loads(response)
		return summonerDict

	def prettyPrintJson(self, inputJson):
		print json.dumps(inputJson.values(), sort_keys=True, indent=4, separators=(',', ': '))