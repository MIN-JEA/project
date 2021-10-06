import cx_Oracle
import os

def category(cursor):

    b = input("찾고 싶은 항목 : ")
    b = '%' + b + '%'

    cursor.execute("select 장소명 , nvl(도로명주소 , 지번주소) from jeju where 장소명 like :1 ", [b])
    # result4 = cursor.fetchall()
    for i, v in enumerate(cursor):
        print(f"{i+1}. {v}")


    # print(result4)

if __name__ == "__main__" :
    LOCATION = r"C:\instantclient_19_12"
    os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]

    connect = cx_Oracle.connect("MiniProject", "0000", "localhost:1521/xe")
    cursor = connect.cursor()
    category()
