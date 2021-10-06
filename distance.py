import cx_Oracle
import os
from haversine import haversine


def distance(cursor):

    s= (input("출발지 : "))
    g= (input("도착지 : "))

    cursor.execute("select 위도 , 경도 from jeju where 장소명 = :1 ",[s])
    result1 = cursor.fetchone()


    cursor.execute("select 위도 , 경도  from jeju where 장소명 = :1 ",[g])
    result2 = cursor.fetchone()


    start=(float(result1[0]), float(result1[1]))
    goal=(float(result2[0]), float(result2[1]))

    haversine(start,goal)

    print(haversine(start,goal))

if __name__ == "__main__" :
    LOCATION = r"C:\instantclient_19_12"
    os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]

    connect = cx_Oracle.connect("MiniProject", "0000", "localhost:1521/xe")
    cursor = connect.cursor()
    distance()



