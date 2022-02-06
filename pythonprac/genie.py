import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
#old_content > table > tbody > tr:nth-child(2) > td.point
for tr in trs:
    a_tag = tr.select_one('td.info > a.title.ellipsis')
    if a_tag is not None:
        rank = tr.select_one('td.number').text[0:2].strip()
        title = a_tag.text.strip()
        point = tr.select_one('td.info > a.artist.ellipsis').text.strip()
        print(rank,title,point)