__author__ = 'shreyas'

import webapp2
import jinja2
from google.appengine.api import users
from BaseHandler import BaseHandler
from Stream import Latest

class LatestHandler(webapp2.RequestHandler, BaseHandler):
    def get(self):
        self.cache('latest')

        JINJA_ENVIRONMENT = jinja2.Environment(
        loader=jinja2.FileSystemLoader('templates'),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)

        user = users.get_current_user()
        user_id = user.user_id()

        #CRON job is responsible for scraping for songs in the background and updating the data store
        ret = Latest.query().order(-Latest.date_modified).get()

        template_values = {
            'songs':ret.songs,
        }

        template = JINJA_ENVIRONMENT.get_template('ShowPage3.html')
        self.response.write(template.render(template_values))