import cx_Oracle
import os



def login(cursor) :
    ID = input("ID를 입력하세요. : ")
    cursor.execute("select * from user_info where id = :1",[ID])
    # print(cursor.fetchone())
    if cursor.fetchone() == None:
        print("존재하지 않는 ID입니다.")
    else:
        passwd = input('비밀번호를 입력하세요. : ')
        cursor.execute("select passwd from user_info where id = :1",[ID])
        # print(cursor.fetchone()[0])
        if cursor.fetchone()[0] == passwd:
            print('로그인 성공')
            return ID
        else:
            print('잘못된 비밀번호')


def regist(cursor) :
    new_ID = input("생성할 ID를 입력하세요. : ")
    cursor.execute("select * from user_info where id = :1",[new_ID])
    if cursor.fetchone() != None:
        print("이미 존재하는 ID입니다.")
    else:
        passwd = input('비밀번호를 입력하세요. : ')
        cursor.execute("insert into user_info values (:1, :2)",[new_ID,passwd])
        # print(cursor.fetchone()[0])
        print("계정 생성 성공")
            

if __name__ == "__main__" :
    LOCATION = r"C:\instantclient_19_12"
    os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]  #환경변수 등록

    connect = cx_Oracle.connect("miniproject/0000@localhost:1521/xe")
    cursor = connect.cursor()

    id = None
    while id is None:
        pick = input('[1] 로그인, [2] 계정 생성 :  ')
        if pick == '1':
            id = login()
        elif pick == '2':
            regist()

