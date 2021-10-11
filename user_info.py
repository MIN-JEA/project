
from Admin_class import Admin
from User_class import User

def login(cursor):
    ID = input("ID를 입력하세요. : ")
    cursor.execute("select * from user_info where id = :1", [ID])

    if cursor.fetchone() == None:
        print("존재하지 않는 ID입니다.")
    else:
        passwd = input('비밀번호를 입력하세요. : ')
        cursor.execute("select passwd from user_info where id = :1", [ID])
        if cursor.fetchone()[0] == passwd:
            if ID == 'admin':
                admin = Admin(ID,cursor)
                return admin
                # return ID
            else:
                user = User(ID,cursor)
                return user
                # return ID
        else:
            print('잘못된 비밀번호')


def regist(cursor):
    new_ID = input("생성할 ID를 입력하세요. : ")
    cursor.execute("select * from user_info where id = :1", [new_ID])
    if cursor.fetchone() != None:
        print("이미 존재하는 ID입니다.")
    else:
        passwd = input('비밀번호를 입력하세요. : ')
        cursor.execute("insert into user_info values (:1, :2)", [new_ID, passwd])
        # print(cursor.fetchone()[0])
        print("계정 생성 성공")


if __name__ == "__main__":
    import cx_Oracle
    import os
    

    LOCATION = r"C:\instantclient_19_12"
    os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]  #환경변수 등록

    connect = cx_Oracle.connect("miniproject/0000@localhost:1521/xe")
    cursor = connect.cursor()

    user = None
    while user is None:
        pick = input('[1] 로그인, [2] 계정 생성 : ')
        if pick == '1':
            user = login(cursor)
        elif pick == '2':
            regist(cursor)

