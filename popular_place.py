import cx_Oracle
import os

def popularity(cursor) :
    cursor.execute("""select *
                    from (select place
                            from user_history
                            group by place
                            order by count(*) DESC)
                    where rownum <= 10""")
    # result = cursor.fetchall()
    for i, v in enumerate(cursor):
        print(i+1, v[0])
    


if __name__ == "__main__" :
    LOCATION = r"C:\instantclient_19_12"
    os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]  #환경변수 등록

    connect = cx_Oracle.connect("miniproject/0000@localhost:1521/xe")
    cursor = connect.cursor()

    ID = 'test'
    while True:
        pick = input('기능을 선택하세요. [1]... [4] 인기 검색어 ...[7]종료 : ')
        if pick == '4':
            popularity()
        elif pick == '7':
            break


