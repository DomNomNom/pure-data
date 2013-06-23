from google.appengine.ext import db


class Game(db.Model):
    name = db.StringProperty( required=True)
    twitchid = db.IntegerProperty(required=True)
    creationTime   = db.DateTimeProperty(auto_now_add=True)
    # website = db.LinkProperty(required=True)

class DataPoint(db.Model):
    creationTime   = db.DateTimeProperty(auto_now_add=True)

class GameDataPoint(db.Model):
    creationTime   = db.DateTimeProperty(auto_now_add=True)
    dataPoint = db.ReferenceProperty(reference_class=DataPoint, collection_name='GameDataPoints', required=True)
    game      = db.ReferenceProperty(reference_class=Game,      collection_name='GameDataPoints', required=True)

    viewers  = db.IntegerProperty(required=True)
    channels = db.IntegerProperty(required=True)