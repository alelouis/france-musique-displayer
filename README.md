# France Musique Bitbar Plug-in

Displays up to 20 last played tracks on https://www.francemusique.fr/ webradios.

Favorite webradio and number of items displayed can be set up in `franceMusiqueDisplay.py`

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

Preview : 

![alt tag](http://i.imgur.com/3taBiDB.png)

Dependencies : `Bitbar` and `BeautifulSoup`  
https://github.com/matryer/bitbar  
https://www.crummy.com/software/BeautifulSoup/ or `pip install beautifulsoup4`
