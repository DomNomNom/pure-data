import webapp2, logging
from environment import jinja_environment
from google.appengine.ext import db

import time

unixTime = lambda datetime: time.mktime(datetime.timetuple()) # for javascript
iso8601  = lambda datetime: time.strftime("%Y-%m-%dT%H:%M:%SZ", datetime.timetuple()) # for http://timeago.yarp.com/


class LatestData(webapp2.RequestHandler):
    def get(self, twichid):

        logging.info(twichid)
        game = db.GqlQuery('SELECT * FROM Game WHERE twitchid=:1', int(twichid)).get()
        logging.info(game.name)

        out = 'date\t' + game.name + '\n'

        for dp in reversed(db.GqlQuery('SELECT * FROM GameDataPoint WHERE game=:1 ORDER BY creationTime DESC', game).fetch(limit=50)):
            out += iso8601(dp.creationTime) + '\t' + str(float(dp.viewers)) + '\n'

        logging.info(out)

        self.response.out.write(out)

        # template = jinja_environment.get_template('api/latest-data.html')
        # self.response.out.write(template.render({
        #         "latestPoints" : db.GqlQuery('SELECT * FROM GameDataPoint WHERE game=:1 ORDER BY creationTime DESC LIMIT 20', game)
        # }))