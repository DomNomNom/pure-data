import webapp2

import handlers.api
import handlers.views
import handlers.apiscrape


''' here we define routing '''

app = webapp2.WSGIApplication(
    routes = [
        (r'/',                              handlers.views.MainPage             ),
        (r'/api/latest-data/([0-9]+)\.tsv',   handlers.api.LatestData             ),

        (r'/cron/scrape',                   handlers.apiscrape.Scrape           ),


        # (r'/_ah/login_required',            handlers.login.Steam                ),

    ],


    config = {
        'webapp2_extras.jinja2': {
            'environment_args': {
                'autoescape': True,
            },
        },
    },

    debug = True
)