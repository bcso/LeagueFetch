from urllib2 import Request, urlopen
import json
from LeagueAPI import *

def main():
	summonerName = raw_input('\n Input your summoner name: ')

	if type(summonerName) != type('s'):
		summonerName = str(summonerName)

	myLeagueObject = LeagueObject()

	summonerDict = 	myLeagueObject.callSummonerDict(summonerName)

	matchDict = myLeagueObject.callMatchDict(
		summonerDict[summonerName]['id'])

	myLeagueObject.prettyPrintJson(summonerDict)

	myLeagueObject.scrapeNames(100)

main()