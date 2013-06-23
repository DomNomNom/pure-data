from google.appengine.ext import db
import webapp2
import logging
import json, urllib2
# from pprint import pprint

import data

url = 'http://api.twitch.tv/kraken/games/top?limit=24&offset=0&on_site=1'

class Scrape(webapp2.RequestHandler):
    def get(self):
        jsondata = json.loads(urllib2.urlopen(url, timeout=30).read())

        dataPoint = data.DataPoint().put()

        # data.Game(twitchid=-1, name="gameName")

        for game in jsondata['top']:
            twitchid = game['game']['_id']
            gameKey = db.GqlQuery('SELECT __key__ FROM Game WHERE twitchid=:1', twitchid).get()
            if not gameKey:
                gameName = game['game']['name']
                gameKey = data.Game(twitchid=twitchid, name=gameName).put()
                logging.info("Created new game: " + gameName)

            data.GameDataPoint(
                viewers  = game['viewers'],
                channels = game['channels'],

                game = gameKey,
                dataPoint = dataPoint,
            ).put()
            # pprint(gameData)

        self.response.write('success')
