# France Musique History Displayer

Displays up to 20 last played tracks on https://www.francemusique.fr/ webradios.
Can be used with Bitbar for menubar access, clicking on items starts a Google search of the specified title.
The terminal only version is also available.

Favorite webradio and number of items displayed can be set up in `franceMusique*.py`

```python
# Configuration
active_radio = la_jazz  # Select from
                            # classique_easy
                            # classique_plus
                            # la_jazz
                            # la_contemporaine
                            # musique_du_monde
                            # classique_kids
history_max = 5         # Can't exceed 20, you don't need more than 20.
```

Preview as Bitbar plug-in : 

![alt tag](http://i.imgur.com/KyHF1AB.jpg)

Preview in terminal : 
```
La Jazz ♫
---
La femme de l'aubergiste
Interprète : Le Taraf De Clejani
Album : Roumanie : Musique des tsiganes de Valachie
Label : OCORA
Début : 2017/01/21 18:14
---
Danses de Lörincreve
Interprète : Zsigmond Szekely, Daniel Hamar, Sandor Csoori
Album : Hongrie/Le dernier passage
Label : OCORA
Début : 2017/01/21 18:09
---
Merzifon oyun havasi
Interprète : Barbaros Erkose, Sezgin Sezer, Hosses Gungor Hosses, Ali Erkose, Selahaddin Erkose, Les Freres Erkose
Album : Turquie : Musique tzigane
Label : 558649
Début : 2017/01/21 18:03
---
Taksim en nihavend
Interprète : Les Freres Erkose, Ali Erkose, Sezgin Sezer, Selahaddin Erkose, Hosses Gungor Hosses, Barbaros Erkose
Album : Turquie : Musique tzigane
Label : 558649
Début : 2017/01/21 18:00
---
Pentozalis
Interprète : Stelios Petrakis, Vassilis Stavrakakis, Giorgos Manolakis, Thanassis Mavrokostas, Giannis Papatzanis, Giorgios Stavrakakis
Album : Crète/L'art de la lyra
Label : OCORA
Début : 2017/01/21 17:57
```

Dependencies : `Python 2.7`, `Bitbar` and `BeautifulSoup`  
https://github.com/matryer/bitbar  
https://www.crummy.com/software/BeautifulSoup/ or `pip install beautifulsoup4`
