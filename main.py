from urllib2 import Request, urlopen
import json
from LeagueAPI import *

def main():
	choice = 0;
	myLeagueObject = LeagueObject()

	while choice != 3:
		print "1. Find your match history"
		print "2. Scrape some names"
		print "3. Quit"
		choice = int(raw_input("Choice: "))

		if choice == 1:
			summonerName = raw_input('\n Input your summoner name: ')
			if type(summonerName) != type('s'):
				summonerName = str(summonerName)
			summonerDict = 	myLeagueObject.callSummonerDict(summonerName)

			matchDict = myLeagueObject.callMatchDict(
				summonerDict[summonerName]['id'])

			for match in matchDict["matches"]:
				print "Match ID: " + str(match["matchId"]) + " Duration: " + str(match["matchDuration"])
			# myLeagueObject.prettyPrintJson(matchDict["matches"][0])

		elif choice == 2:
			numNames = int(raw_input('\n Number of names: '))
			myLeagueObject.scrapeNames(numNames)

main()