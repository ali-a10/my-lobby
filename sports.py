from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

# opening up connection and grabbing the page
url = 'https://www.espn.com/soccer/team/_/id/83/barcelona'

uClient = urlopen(url)  #downloads webpage
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# team's next game
teams_4nxt = page_soup.findAll("span", {"class": "abbrev"})
nxtgm_team_a = teams_4nxt[0].text
nxtgm_team_b = teams_4nxt[1].text

if not page_soup.findAll("div", {"class": "game-date"}):  #live game
    nxtgm_date = page_soup.findAll("span", {"class": "game-time"})[0].text
    nxtgm_time = ''
else:
    nxtgm_date = page_soup.findAll("div", {"class": "game-date"})[0].text
    nxtgm_time = page_soup.findAll("div", {"class": "time"})[0].text

news = page_soup.findAll("div", {"class": "item-info-wrap"})
team_img = "static/images/barca.png"
next_game = (nxtgm_team_a, nxtgm_team_b, nxtgm_time, nxtgm_date, team_img)


#LAKERS
url = 'https://www.espn.com/nba/team/_/name/lal/los-angeles-lakers'

uClient = urlopen(url)  #downloads webpage
page_html = uClient.read()
uClient.close()

# html parsing
page_soup2 = soup(page_html, "html.parser")

# team's next game
opponent2 = page_soup2.findAll("div", {"class": "game-info"})[0].text

if not page_soup2.findAll("div", {"class": "game-date"}):  #live game
    nxtgm_date2 = "LIVE"
    nxtgm_time2 = ""
else:
    nxtgm_date2 = page_soup2.findAll("div", {"class": "game-date"})[0].span.text
    nxtgm_time2 = page_soup2.findAll("div", {"class": "time"})[0].text

news2 = page_soup2.findAll("div", {"class": "item-info-wrap"})
team_img2 = "static/images/lakers.png"
next_game2 = (opponent2, nxtgm_time2, nxtgm_date2, team_img2)


# # TORONTO NEWS
# url3 = 'https://globalnews.ca/toronto/'

# uClient3 = urlopen(url3)  #downloads webpage
# page_html3 = uClient3.read()
# uClient3.close()

# # html parsing
# page_soup3 = soup(page_html3, "html.parser")

# headline = page_soup3.findAll("span", {"class": "c-posts__headlineText"})


news_lst = []
for j in range(len(news)):
    b = news[j].div.span.text
    if b[-1] == 'h':
        news_lst.append((int(b[0:-1]), j, team_img))
    else:
        news_lst.append((int(b[0:-1]) + 24, j, team_img))

for i in range(len(news2)):
    y = news2[i].div.span.text
    if y[-1] == 'h':
        news_lst.append((int(y[0:-1]), i, team_img2))
        # print(int(y[0:-1]))
    else:
        news_lst.append((int(y[0:-1]) + 24, i, team_img2))

news_lst.sort()
news_lst1 = []
for n in news_lst:
    if n[2] == team_img:
        if news[n[1]].h1.a['href'][:5] != 'https':
            news_lst1.append((news[n[1]], team_img, 'https://www.espn.com' +
                              news[n[1]].h1.a['href']))
        else:
            news_lst1.append((news[n[1]], team_img, news[n[1]].h1.a['href']))
    else:
        if news2[n[1]].h1.a['href'][:5] != 'https':
            news_lst1.append((news2[n[1]], team_img2, 'https://www.espn.com' +
                              news2[n[1]].h1.a['href']))
        else:
            news_lst1.append((news2[n[1]], team_img2, news2[n[1]].h1.a['href']))

