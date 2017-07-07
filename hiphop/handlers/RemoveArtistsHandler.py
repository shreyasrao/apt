__author__ = 'shreyas'

import webapp2
from google.appengine.api import users
from Stream import Personal
from handlers.BaseHandler import BaseHandler
import time
from Stream import Artist
from Stream import Song
import jinja2
import cgi
from google.appengine.ext import ndb

class RemoveArtistsHandler(webapp2.RequestHandler, BaseHandler):
    def post(self):
        remove_artist_ids = self.request.get_all('remove_artists')
        self.response.write(remove_artist_ids)

        user_id = users.get_current_user().user_id()
        me = Personal.query(Personal.user_id==user_id).get()
        old_version = me.version

        newArtists = me.liked_artists

        stop = False

        while(len(remove_artist_ids)>0):
        # while(not stop):
            for artist in me.liked_artists:
                if (str(artist.id) == str(remove_artist_ids[0])):
                    remove_artist_ids.pop(0)
                    newArtists.remove(artist)
                    break
                # else:
                #     self.response.write("ID does not match: " + str(artist.id) + "|")
            stop = True

        self.response.write("Done with matching")

        new_version = old_version + 1
        me.version = new_version
        me.liked_artists = newArtists

        me.put()
        time.sleep(1.5)
        # updated = False

        # while(not updated):
        #     me = Personal.query(Personal.user_id==user_id).get()
        #     if (me.version == new_version):
        #         updated = True

        # self.response.write("removed")
        self.redirect('/like_artists')
