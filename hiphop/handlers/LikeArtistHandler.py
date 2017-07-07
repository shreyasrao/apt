__author__ = 'shreyas'

import webapp2
from google.appengine.api import users
from Stream import Personal
from handlers.BaseHandler import BaseHandler
from Stream import Artist
from Stream import Song
import jinja2
import cgi
from google.appengine.ext import ndb

class LikeArtistHandler(webapp2.RequestHandler, BaseHandler):
    def get(self):
        user_id = users.get_current_user().user_id()
        me = Personal.query(Personal.user_id==user_id).get()
        self.cache('liked_artists')

        if me.liked_artists:
            JINJA_ENVIRONMENT = jinja2.Environment(
            loader=jinja2.FileSystemLoader('templates'),
            extensions=['jinja2.ext.autoescape'],
            autoescape=True)

            template_values = {
                'artists':me.liked_artists,
            }

            template = JINJA_ENVIRONMENT.get_template('LikedArtists.html')
            self.response.write(template.render(template_values))
        else:
            # self.response.write("You have not liked any artists yet")
            self.errorpage("As you like songs, those artists will be displayed here")