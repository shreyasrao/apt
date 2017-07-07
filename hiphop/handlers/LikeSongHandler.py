__author__ = 'shreyas'

import webapp2
from google.appengine.api import users
from Stream import Personal
from handlers.BaseHandler import BaseHandler
from Stream import Artist
from Stream import Song
import jinja2
import time
import cgi
from google.appengine.ext import ndb

class LikeSongHandler(webapp2.RequestHandler, BaseHandler):
    def post(self):
        songs = self.request.get_all('liked_songs')

        user_id = users.get_current_user().user_id()
        me = Personal.query(Personal.user_id==user_id).get()
        old_version = me.version

        for song in songs:
            s = str(song).split('|')
            artist = str(s[0])
            title = str(s[1])
            link =  str(s[2])

            new_artist = self.createArtist(artist)
            if not new_artist:
                # self.response.write("Artist not found: " + artist)
                new_artist
            else:
                # self.response.write("Artist: " + artist + " id: " + str(new_artist.id))
                already_liked_artist = False

                #dont duplicated liked artists in Personal
                if me.liked_artists:
                    for my_artist in me.liked_artists:
                        if(my_artist.id==new_artist.id):
                            already_liked_artist = True
                            break

                    if(not already_liked_artist):
                        me.liked_artists.append(new_artist)
                else:
                    #if no liked artists, then create new list and add item
                    new_artist_list = list()
                    new_artist_list.append(new_artist)
                    me.liked_artists = new_artist_list

                #dont duplicate artists in DB
                artist_in_db = Artist.query(Artist.id==new_artist.id).get()
                if artist_in_db:
                    artist_in_db
                else:
                    new_artist.put()

            new_song = self.createSong(title, artist, link)

            #Dont duplicate liked song in Personal
            already_liked_song = False
            if me.liked_songs:
                for song in me.liked_songs:
                    if(song.link==new_song.link):
                        already_liked_song=True
                        break

                if(not already_liked_song):
                    me.liked_songs.append(new_song)
            else:
                #if no liked songs, then create new list and add item
                new_song_list = list()
                new_song_list.append(new_song)
                me.liked_songs = new_song_list

            #dont duplicate song in DB
            song_in_db = Song.query(Song.link==new_song.link).get()
            if song_in_db:
                song_in_db
            else:
                new_song.put()

        me.version = old_version + 1
        me.put()
        time.sleep(1.5)
        self.redirect('/like_songs')


    def get(self):
        user_id = users.get_current_user().user_id()
        me = Personal.query(Personal.user_id==user_id).get()
        self.cache('liked_songs')

        if me.liked_songs:
            JINJA_ENVIRONMENT = jinja2.Environment(
            loader=jinja2.FileSystemLoader('templates'),
            extensions=['jinja2.ext.autoescape'],
            autoescape=True)

            template_values = {
                'songs':me.liked_songs,
            }

            template = JINJA_ENVIRONMENT.get_template('LikedSongs.html')
            self.response.write(template.render(template_values))
        else:
            # self.response.write("You have not liked any songs yet")
            self.errorpage("You have not liked any songs yet")



        # self.response.write("MY Version:" + str(me.version) + "\n")

        # self.redirect('/management')

        # stream_names = self.request.get_all('deleted_streams')
        # for stream_name in stream_names:
        #     stream_key = ndb.Key(Stream,stream_name)
        #     stream_key.delete()
        #
        #
        #
        # self.redirect('/management')