__author__ = 'shreyas'

import webapp2
from BaseHandler import BaseHandler
from Stream import Popular
import datetime
import urllib2
from bs4 import BeautifulSoup
import time

class UpdatePopular(webapp2.RequestHandler, BaseHandler):
    def get(self):
        url = "http://www.hotnewhiphop.com/songs/popular/"
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page.read(), "html.parser")
        allGridItems = soup.find_all('div', {'class':'gridItem-trackInfo'})

        items = list()

        for item in allGridItems:
            now = str(item)
            items.append(now)

        links = list()

        for item in items:
            now = str(item)
            start =  now.index("href=") + 6
            end = now.index('"',start)
            links.append("http://www.hotnewhiphop.com" + now[start:end])

        soundLinks = list()
        notFound = list()
        meta = list()

        for link in links:
            web = link
            site = urllib2.urlopen(web)
            soup = BeautifulSoup(site.read(),"html.parser")
            sound = str(soup.find("iframe"))
            lstart = sound.find("https://soundcloud.com/")
            if(lstart==-1):
                # soundLinks.append("CANNOT FIND: " + link)
                notFound.append("CANNOT FIND: " + link)
            else:
                lend = sound.find("&amp;", lstart)
                sclink = "https://w.soundcloud.com/player/?url=" + sound[lstart:lend]
                soundLinks.append(sclink)
                heading = str(soup.find_all('h1', {'class':'audioContent-title'}))
                start = heading.find('>')+3
                end = heading.find('</h1>',start)
                info=heading[start:end].strip().replace('&amp;','&').replace('</h1>','').split(" - ")
                meta.append({'artist':info[0], 'title':info[1], 'link':sclink})

        upToDate = False
        already = Popular.query()
        for each in already:
            mod = each.date_modified
            if(mod==datetime.datetime.now().date()):
                upToDate=True
                break

        if(not upToDate):
            linkStore = Popular(songs=meta, date_modified=datetime.datetime.now().date())
            linkStore.put()
        else:
            ret = Popular.query().order(-Popular.date_modified).get()
            ret.songs = meta
            ret.put()