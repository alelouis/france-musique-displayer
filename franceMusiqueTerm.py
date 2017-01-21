#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import numpy as np
import csv
import time
import os
import codecs
import encodings
from bs4 import BeautifulSoup as bs

def id_to_radio_name(argument):
    switcher = {
        401: "Classique Easy",
        402: "Classique Plus",
        403: "Concert Radio France",
        404: "La Jazz",
        405: "La Contemporaine",
        406: "Musique du Monde",
        407: "Classique Kids",
    }
    return switcher.get(argument)

# WebRadio ID
classique_easy = 401
classique_plus = 402
concert_radio = 403
la_jazz = 404
la_contemporaine = 405
musique_du_monde = 406
classique_kids = 407

# Configuration
active_radio = la_jazz  # Select from
                            # classique_easy
                            # classique_plus
                            # la_jazz
                            # la_contemporaine
                            # musique_du_monde
                            # classique_kids
history_max = 5         # Can't exceed 20, you don't need more than 20.


webradio_url = 'https://www.francemusique.fr/programmes/oeuvres-diffusees?stationID=' + str(active_radio)
response = urllib2.urlopen(webradio_url)
html = response.read()
radio_history = bs(html, "html5lib")

# History arrays
titles = np.array([])
performers = np.array([])
composers = np.array([])
albums = np.array([])
labels = np.array([])
date = np.array([])

# Parse France Musique history pages
for data in radio_history.find_all('span'):
    if data.get("class") is not None and data.get("class")[0]=="past-expression-list-element-performers":
        performers = np.append(performers, data.string.encode('utf8'))
    if data.get("class") is not None and data.get("class")[0]=="past-expression-list-element-composers":
        composers = np.append(composers, data.string.encode('utf8'))
    if data.get("class") is not None and data.get("class")[0]=="past-expression-list-element-album":
        albums = np.append(albums, data.string[8:].encode('utf8'))
    if data.get("class") is not None and data.get("class")[0]=="past-expression-list-element-label":
        labels = np.append(labels, data.string[8:].encode('utf8'))

for data in radio_history.find_all('h2'):
    if data.get("class") is not None and data.get("class")[0]=="past-expression-list-element-title":
        titles = np.append(titles, data.string.encode('utf8'))

for data in radio_history.find_all('div'):
    if data.get("class") is not None and data.get("class")[0]=="past-expression-list-element-date":
        date = np.append(date, time.strftime("%Y/%m/%d " + data.string.strip().encode('utf8')))

# Bitbar display
menubar_indicator = id_to_radio_name(active_radio) + ' ' + u'\U0000266B'
print menubar_indicator.encode("utf-8")
for history_indice in range(0,history_max):
    url = 'http://www.google.com/search?' + urllib.urlencode({'q': titles[history_indice] })
    print '---'
    print titles[history_indice]
    print "Interprète : " + performers[history_indice]
    if active_radio != la_jazz :
        print "Compositeur : " + composers[history_indice]
    print "Album : " + albums[history_indice]
    print "Label : " + labels[history_indice]
    print "Début : " + date[history_indice]
