from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

# html = urlopen("http://localhost:3000")

# soup = BeautifulSoup(html, "html.parser")
# print(soup)

def getCountry(ip):
    resp = urlopen('http://freegeoip.net/json/'+ip).read().decode("utf-8")
    print(resp)
    # json_response = json.loads(resp)
    # return json_response.get("country_code")

print(getCountry('50.78.253.58'))
