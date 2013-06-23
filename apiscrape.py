
import json, urllib2
from pprint import pprint

url = 'http://api.twitch.tv/kraken/games/top?limit=24&offset=0&on_site=1'
data = json.loads(urllib2.urlopen(url, timeout=30).read())


for game in data['top']:
    gameData = (
        game['game']['_id'],
        game['game']['name'],
        game['viewers'],
        game['channels']
    )
    pprint(gameData)
