import cx_Oracle
import os
# import user_info, popular_place, search, category,distance
from user_info import login,regist
from search import search
from distance import distance
from category import category
from popular_place import popularity
from history import history
from bookmark import bookmark


LOCATION = r"C:\instantclient_19_12"
os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]  #환경변수 등록

connect = cx_Oracle.connect("miniproject/0000@localhost:1521/xe")
cursor = connect.cursor()

ID = None

while ID is None:
    pick = input('[1] 로그인, [2] 계정 생성 :  ')
    if pick == '1':
        ID = login(cursor)
    elif pick == '2':
        regist(cursor)
    else:
        print('잘못된 명령어입니다.')

while True:
    pick = input('[1] 주소검색 [2] 거리계산 [3] 유형별검색 [4] 인기검색어 [5] 히스토리 [6] 즐겨찾기 [7] 종료 : ')
    if pick == '1':
        search(cursor,ID)
    elif pick == '2':
        distance(cursor)
    elif pick == '3':
        category(cursor)
    elif pick == '4':
        popularity(cursor)
    elif pick == '5':
        history(cursor,ID)
    elif pick == '6':
        bookmark(cursor,ID)
    elif pick == '7':
        print('종료')
        break
    else:
        print('명령어 오류')

connect.commit()
cursor.close()
connect.close()