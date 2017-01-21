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
![alt tag](blob:http://imgur.com/b0c95548-ff3d-408c-8f87-ce43f6c5c2ca)

Dependencies : `Python 2.7`, `Bitbar` and `BeautifulSoup`  
https://github.com/matryer/bitbar  
https://www.crummy.com/software/BeautifulSoup/ or `pip install beautifulsoup4`
