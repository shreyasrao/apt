__author__ = 'shreyas'

import webapp2
from google.appengine.api import users
from Stream import Personal
from handlers.BaseHandler import BaseHandler
import time

class RemoveSongsHandler(webapp2.RequestHandler, BaseHandler):
    def post(self):
        remove_song_links = self.request.get_all('remove_songs')

        user_id = users.get_current_user().user_id()
        me = Personal.query(Personal.user_id==user_id).get()
        old_version = me.version

        newSongs = me.liked_songs

        while(len(remove_song_links)>0):
            for song in me.liked_songs:
                if (song.link == remove_song_links[0]):
                    remove_song_links.pop(0)
                    newSongs.remove(song)
                    break

        new_version = old_version + 1
        me.version = new_version
        me.liked_songs = newSongs

        me.put()
        time.sleep(1.5)

        self.redirect('/like_songs')
