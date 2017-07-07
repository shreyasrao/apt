import json
import sys
import re
import urllib2
from bs4 import BeautifulSoup

def scrape():
    # jsonQuoteData = "[]"
    print "HELLO"
    filename = "/Users/shreyas/Desktop/APT/shreyas/Final_Soups/New Hip Hop Songs, Hottest Music Releases.html"
    inputFile = open(filename)

    url = "http://www.hotnewhiphop.com/songs/"
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
    print "the numbers of links is " + str(len(links))

    # web = "http://www.hotnewhiphop.com/r-kelly-christmas-party-new-song.1967561.html"

    soundLinks = list()
    notFound = list()

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
            soundLinks.append(sound[lstart:lend])

    #print soundLinks
    print "Number of found links is " + str(len(soundLinks))
    print "Number of not found links is " + str(len(notFound))
    #print notFound


    print "Done!"
    return

scrape()