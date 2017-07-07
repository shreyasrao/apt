#!/usr/bin/python

import webapp2
import jinja2
import os

from handlers.MainPageHandler import MainPageHandler
from handlers.ErrorHandler import ErrorHandler
from handlers.LatestHandler import LatestHandler
from handlers.PopularHandler import PopularHandler
from handlers.LikeSongHandler import LikeSongHandler
from handlers.RecommendArtistsHandler import RecomendArtistHandler
from handlers.RecommendEventsHandler import RecomendEventsHandler
from handlers.RemoveSongsHandler import RemoveSongsHandler
from handlers.LikeArtistHandler import LikeArtistHandler
from handlers.RemoveArtistsHandler import RemoveArtistsHandler
from handlers.UpdateLatest import UpdateLatest
from handlers.UpdatePopular import UpdatePopular


app = webapp2.WSGIApplication([('/', MainPageHandler),
                               ('/latest',LatestHandler),
                               ('/popular',PopularHandler),
                               ('/error',ErrorHandler),
                               ('/like_songs',LikeSongHandler),
                               ('/like_artists',LikeArtistHandler),
                               ('/rec_artists',RecomendArtistHandler),
                               ('/rec_events',RecomendEventsHandler),
                               ('/remove_songs',RemoveSongsHandler),
                               ('/remove_artists',RemoveArtistsHandler),
                               ('/update_latest',UpdateLatest),
                               ('/update_popular',UpdatePopular),
                              ], debug=True)