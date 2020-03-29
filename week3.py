import requests
from bs4 import BeautifulSoup

import datetime

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
dt = datetime.date.today()
d = dt.strftime('%Y%m%d')
today_date = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd='+d
data = requests.get(today_date,headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#############################
# (입맛에 맞게 코딩)
# print(dt)
# print(d)
# print(today_date)

rows = soup.select(' tr > td.info')
# print(rows)
rank = 1
for row in rows:
    music_names = row.select_one('td > a.title.ellipsis')
    music_name = music_names.text
    # print(music_name.strip())
    artist_names = row.select_one('td > a.artist.ellipsis')
    artist_name = artist_names.text
    # print(artist_name)
    print(str(rank), music_name.strip(), '- '+artist_name)
    rank += 1
#############################