import cx_Oracle
import os
from user_info import login,regist

LOCATION = r"C:\instantclient_19_12"
os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]  #환경변수 등록

connect = cx_Oracle.connect("miniproject/0000@localhost:1521/xe")
cursor = connect.cursor()

user = None
while user is None:
    pick = input('[1] 로그인, [2] 계정 생성 :  ')
    if pick == '1':
        user = login(cursor)
    elif pick == '2':
        regist(cursor)
    else:
        print('잘못된 명령어입니다.')

user()

connect.commit()
cursor.close()
connect.close()