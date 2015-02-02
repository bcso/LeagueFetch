from urllib2 import Request, urlopen
import json
import time

class LeagueObject:
	def __init__(self, summonerKey):
		self.key = summonerKey
		
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
		print json.dumps(inputJson, sort_keys=True, indent=4, separators=(',', ': '))

	def scrapeNames(self, numberOfNames):
		currID = 24918846
		count = 0;
		while (count < numberOfNames): #Loop over for unique names
			url = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/' + str(currID) + '?api_key=' + self.key
			nameListObj = json.loads(urlopen(Request(url)).read())
			currName = nameListObj[str(currID)]["name"]
			if currName[:2] != 'IS':
				print currName
				count = count +1
			currID = currID + 1
			time.sleep(1)
