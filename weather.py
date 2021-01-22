from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

# opening up connection and grabbing the page
url = 'https://weather.gc.ca/city/pages/on-24_metric_e.html'

uClient = urlopen(url)  #downloads webpage
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# team's next game
teams_4nxt = page_soup.findAll("span", {"class": "abbrev"})

# temp = page_soup.findAll("span", {"class": "temp"})
temp = page_soup.findAll("span", {"class": "wxo-metric-hide"})[0].text
time = page_soup.findAll("dd", {"class": "mrgn-bttm-0"})[1].text
condition = page_soup.findAll("p", {"class":"visible-xs text-center"})
# icons from https://www.flaticon.com/packs/weather-forecast

if condition[0].text == "Mostly Cloudy":
    wthr_img = "static/images/cloudy.PNG"

elif condition[0].text == "Sunny":
    wthr_img = "static/images/sunny.PNG"

elif condition[0].text == "Partly Cloudy":  # consider night and morning
    wthr_img = "static/images/partlycloudy.PNG"

elif condition[0].text == "Light Snow":
    wthr_img = "static/images/snowing.PNG"

else:
    wthr_img = "static/images/thunder.PNG"
#
# elif condition[0].text == "Mostly Cloudy":
#     img_src = "static/images/cloudy.PNG"
# temp_img = page_soup.findAll("img", {"class": "center-block mrgn-tp-md"})

