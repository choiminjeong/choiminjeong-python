import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200325',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#############################
# (입맛에 맞게 코딩)
rows = soup.select('#old_content > table > tbody > tr')
# print(rows)
# print(len(tr)) - 길이 알려줌
# fr = soup.select_one('#old_content > table > tbody > tr')
# print(fr)
rank = 1
for row in rows:
    movie_names = row.select_one(' div.tit5 > a')
    if movie_names != None:
        movie_point = row.select_one('.point')
        # print(movie_names)
        # print(rank, end=". ")
        # print(movie_names.text, end="  ")
        # print(movie_point.text, end="    /")
        print(str(rank)+'. '+movie_names.text + ' ' + movie_point.text)
        # print(rank, movie_names.text , movie_point.text)
        rank += 1
        # print(movie_point.text)

# for grade in rows:
#     movie_star = grade.select_one('.point')
#     if movie_star != None:
#         print(movie_star.text)

#############################