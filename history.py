import cx_Oracle  # orcale 탑재
import os  # os 탑재

def history(cursor,ID):
    
    menu = """
=================================
    menu
1. 지번 주소로 검색
2. 도로명 주소로 검색
=================================
"""
    num = None
    while num is None:
        print(menu)
        print("Select menu: ")
        num = input()
        if num == '1':
            cursor.execute("select adress from user_history where id = :1", [ID])

            for list in cursor:
                print(list)
            print("지번 주소로 검색 완료")

        elif num == '2':
            cursor.execute("select roadname from user_history where id = :1", [ID])

            for list in cursor:
                print(list)
            print("도로명 주소로 검색 완료")

if __name__ == "__main__" :
    os.putenv('NLS_LANG', '.UTF8')

    cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_19_12")

    con_ip = 'localhost:1521/xe'
    con_id = 'miniproject'
    con_pw = '0000'

    connection = cx_Oracle.connect(con_id, con_pw, con_ip)
    cursor = connection.cursor()
    ID = 'test'
    history(cursor, ID)

    cursor.close()
    connection.close()