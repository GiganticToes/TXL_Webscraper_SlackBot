from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import requests
import json

# TXL Coin
req = Request('https://nomics.com/assets/txl2-tixl-token-erc-20')
page = urlopen(req).read()

page_soup = soup(page, "html.parser")
price = page_soup.find("span", {
                       "class": "mono f3 f-30-l fw5 n-near-black nowrap n-mb1-neg-l lh-solid n-mr9"}).text

pChange = page_soup.find("span", {
    "class": "mono fw5 f4-l"}).text

pChange = float(pChange.replace('%', ''))


slack_url = 'https://hooks.slack.com/services/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'
payload = {
    "text": "TXL Price is: " + price + "\nChange of: " + str(pChange)+"%"}
requests.post(slack_url, data=json.dumps(payload))
