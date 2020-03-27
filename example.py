# # # print('스파르타 코딩클럽')
# # #
# # # a = 'spartacodingclub@gmail.com'
# # # b= 'dkjdkanaver.com'
# # #
# # # #채워야하는 함수
# # # def check_mail(s):
# # # 	## 여기에 코딩을 해주세요
# # #     return '@' in s
# # #
# # # #결과값
# # # print(check_mail(b))
# # #
# # # #아래와 같이 출력됩니다
# # # # True
# # #
# # # #입력값
# # fruits = ['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']
# #
# # #채워야하는 함수
# # def count_list(fruits):
# #
# #
# #     result = {}
# #     for fruit in fruits:
# #         if fruit in result:
# #             result[fruit] += 1
# #         else:
# #             result[fruit] = 1
# #     return result
# #
# # #결과값
# # print(count_list(fruits))
# #
# # #아래와 같이 출력됩니다
# # # {'사과': 1, '감': 3, '배': 1, '포도': 3, '딸기': 2, '수박': 1}
#
#
# numbers = [1,2,3,2,2,3,4,2,2,2,1,4,5,3,3,4,3]
#
# def count_num(numbers):
#     result ={}
#     for number in numbers:
#         if number in result:
#             result[number] +=1
#         else:
#             result[number] =1
#     return result
#
# print(count_num(numbers))

import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

gus = rjson['RealtimeCityAir']['row']

for gu in gus:
    if gu['IDEX_MVL']> 75:
	    print (gu['MSRSTE_NM'], gu['IDEX_MVL'])