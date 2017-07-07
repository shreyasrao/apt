__author__ = 'shreyas'

import urllib2
import webapp2
import jinja2
from handlers.BaseHandler import BaseHandler
from google.appengine.api import users
from Stream import Personal
# from Stream import Artist
import json

class Event():
    Title = None
    Location = None
    Url = None
    Date = None

class RecomendEventsHandler(webapp2.RequestHandler, BaseHandler):
    def get(self):
        self.cache('rec_events')

        user_id = users.get_current_user().user_id()
        me = Personal.query(Personal.user_id==user_id).get()

        if me.liked_artists:
            key = '&client_id=Mzk0Njg1OHwxNDQ5NTQ2NTUx'
            zip = '&postal_code=78705'
            base_url = "http://api.seatgeek.com/2/recommendations?"

            my_fav_artists = me.liked_artists
            base_url = base_url + "performers.id=" + str(my_fav_artists.pop(0).id)
            while(len(my_fav_artists)>0):
                base_url = base_url + "&performers.id=" + str(my_fav_artists.pop(0).id)

            url = base_url + zip + key
            response = urllib2.urlopen(url)
            data = response.read()
            values = json.loads(data)
            # self.response.write(url)
            if values['recommendations']:
                # recommended_events = list()
                events = list()
                output = values['recommendations']
                for hit in output:
                    event = hit['event']
                    Title = event['title']
                    Location = event['venue']['name'] + ", " + event['venue']['address'] + ", " + event['venue']['extended_address']
                    Url = event['url']
                    Date = str(event['datetime_local']).split('T')[0]
                    a = Event()
                    a.Title = Title
                    a.Location = Location
                    a.Url = Url
                    a.Date = Date
                    events.append(a)


                JINJA_ENVIRONMENT = jinja2.Environment(
                loader=jinja2.FileSystemLoader('templates'),
                extensions=['jinja2.ext.autoescape'],
                autoescape=True)

                template_values = {
                    'events':events,
                }

                template = JINJA_ENVIRONMENT.get_template('RecommendEventsPage.html')
                self.response.write(template.render(template_values))
            else:
                self.errorpage("No recommendations can be given for the artists that you have liked")

        else:
            # self.response.write("In order to get recommendations, you must like least 1 song")
            self.errorpage("In order to get recommendations, you must like least 1 song")