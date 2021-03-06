LeagueFetch
===========

### Welcome to League Fetch.
It is the beginnings of a thin wrapper between the [League of Legends API](https://developer.riotgames.com/) and the API calls that the user may use with their user key.

Included is a python script leveraging the use of this wrapper, going through some test cases. Users may choose between one of two options - first is to retrieve histories for their past 10 games and associated Match History ID, second is to scrape summoner in-game-names. Match History ID can be easily used to query match history details by concatenating it in the request URL.


```
$ git clone https://github.com/bcso/LeagueFetch.git
$ cd LeagueFetch
$ python main.py
```

### Finding match history
Find a list of your last 10 most recent match histories and the corresponding duration. This is used mainly for development purposes - ID's are unique and can be used to find more match details.

```
$ python main.py 
1. Find your match history
2. Scrape some names
3. Quit
Choice: 1 

 Input your summoner name: ddomokunn
Match ID: 1564048672 Duration: 1704
Match ID: 1564868327 Duration: 2016
Match ID: 1564942790 Duration: 1735
Match ID: 1564958838 Duration: 2508
Match ID: 1569546251 Duration: 1270
Match ID: 1569604125 Duration: 1564
Match ID: 1623238744 Duration: 2194
Match ID: 1642182564 Duration: 3029
Match ID: 1657117433 Duration: 1984
Match ID: 1657171207 Duration: 2224
```

### Scraping names
Scrape some names that start from the specified user ID. The scraper will increment by 1 from this start point.
```
$ python main.py 
1. Find your match history
2. Scrape some names
3. Quit
Choice: 2

 Number of names: 3
DDomokunn
BiggestAnBaddest
RenderDead
```

### Future work
As shown above the basic data retrieval is very intuitive - this opens the possibility for:
- Mapping friend networks, visualization with D3
- Generating insights based on friend groups and main roles
- Storing names scraped in local database for faster querying

### Authors and Contributors
In 2015 Brian So (@bcso) decided to create his first GH page for this project. This is a proof of concept project playing around with Riot's League of legends API to test endpoints. Credits go out to [Riot Games](http://www.riotgames.com/) for developing this amazing API!