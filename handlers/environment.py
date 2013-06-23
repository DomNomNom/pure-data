import jinja2, os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), os.path.pardir, 'html')),
    autoescape=True,
)

jinja_environment.globals.update(
    str=str,
    xrange = xrange,
    unixTime = lambda datetime: time.mktime(datetime.timetuple()), # for javascript
    iso8601  = lambda datetime: time.strftime("%Y-%m-%dT%H:%M:%SZ", datetime.timetuple()), # for http://timeago.yarp.com/
)