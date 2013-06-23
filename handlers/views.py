import webapp2
from google.appengine.ext import db
from environment import jinja_environment

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('view.html')
        self.response.out.write(template.render({
            'games' : db.GqlQuery("SELECT * FROM Game ORDER BY name")
        }))
