__author__ = 'shreyas'
import webapp2
import jinja2
import json
import urllib2
import os
from Stream import Stream
from google.appengine.api import users
from Stream import Personal
from Stream import Artist
from Stream import Song

class BaseHandler():
    def createSong(self, Title, Artist, song_link):
        already = Song.query(Song.link==song_link).get()
        if already:
            return already
        else:
            new_song = Song(link=song_link, title=Title, artist=Artist)
            return new_song

    def createArtist(self, artist_name):
        # url = "http://api.seatgeek.com/2/performers?q=kendrick%20lamar"
        base_url = "http://api.seatgeek.com/2/performers?q="
        sec = str(artist_name).lower().replace('.','').replace('-',' ').replace('$','s').split(" ")
        suffix = sec.pop(0)

        while(len(sec)>0):
            suffix = suffix + "%20" + sec.pop(0)

        url = base_url + suffix


        response = urllib2.urlopen(url)
        data = response.read()
        values = json.loads(data)
        if values['performers']:
            output = values['performers'][0]
            new_artist = Artist(name=output['name'], id=output['id'], image_link=output['image'])
            return new_artist
        else:
            return None

            # ret = Artist.query(Artist.id==output['id']).get()
            #
            # if ret:
            #     ret
            # else:
            #     new_artist.put()

            # print type(output)
            #print values['performers']

            # for key in output:
            #     print "Key is " + key + " : " + str(output[key])

    def cache(self, currentTab):
        JINJA_ENVIRONMENT = jinja2.Environment(
        loader=jinja2.FileSystemLoader('templates'),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)

        user = users.get_current_user()
        user_id = user.user_id()
        logout_url = users.create_logout_url('/')

        existing = Personal.query(Personal.user_id==user_id).get()
        if existing:
            existing #do nothing
        else:
            new_user = Personal(user_id=str(user_id),version=0)
            new_user.put()



        #welcome to Connexus
        userInfo = {
            'user':user,
            'logout_url': logout_url
        }


        # template = JINJA_ENVIRONMENT.get_template('Welcome.html')
        # self.response.write(template.render(userInfo))

        # #Get the list of streams
        # streams = Stream.query()
        # taglist = []
        #
        # streamNames = []
        # for stream in streams:
        #     streamNames.append(str(stream.name))
        #     for tag in stream.tags:
        #         if tag not in taglist:
        #             streamNames.append(tag)
        #             taglist.append(tag)
        #
        #
        # template_values = {
        #     'streams':streams
        # }
        #
        # template = JINJA_ENVIRONMENT.get_template('Search.html')
        # self.response.write(template.render(streams = json.dumps(streamNames)))

        #test search header

        headerInfo = {
            'current' : currentTab,
            'user':user,
            'logout_url': logout_url
        }

        searchHead = JINJA_ENVIRONMENT.get_template('Header.html')
        # self.response.write(searchHead.render(current = currentTab))
        self.response.write(searchHead.render(headerInfo))

    def errorpage(self, msg):
        # self.cache('')

        JINJA_ENVIRONMENT = jinja2.Environment(
        loader=jinja2.FileSystemLoader('templates'),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)

        template_values = {'message':msg}

        searchHead = JINJA_ENVIRONMENT.get_template('ErrorPage.html')
        # self.response.write(searchHead.render(current = currentTab))
        self.response.write(searchHead.render(template_values))

        # self.response.write(msg)
