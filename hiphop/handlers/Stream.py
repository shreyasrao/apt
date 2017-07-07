__author__ = 'shreyasrao'

from google.appengine.ext import ndb
import urllib2
from bs4 import BeautifulSoup

class Personal(ndb.Model):
    user_id = ndb.StringProperty()
    liked_artists = ndb.PickleProperty()
    liked_songs = ndb.PickleProperty()


    version = ndb.IntegerProperty()

class Song(ndb.Model):
    title = ndb.StringProperty()
    artist = ndb.StringProperty()
    link = ndb.StringProperty()

class Artist(ndb.Model):
    name = ndb.StringProperty()
    image_link = ndb.StringProperty()
    id = ndb.IntegerProperty()

class Popular(ndb.Model):
    songs = ndb.PickleProperty()
    date_modified = ndb.DateProperty()

class Latest(ndb.Model):
    date_modified = ndb.DateProperty()
    songs = ndb.PickleProperty()
