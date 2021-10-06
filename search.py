import cx_Oracle
import os

def search(cursor,ID):
    a = input("장소명 : ")

    cursor.execute("select  nvl(도로명주소 , 지번주소) from jeju where 장소명 = :1 ", [a])
    result3 = cursor.fetchone()
    print(f"{a}의 주소 : {result3[0]}")
    b = [ID, a, None, result3[0]]
    cursor.execute("INSERT INTO user_history VALUES(:1, :2, :3, :4)", b)

    menu = """즐겨찾기를 추가 하시겠습니까?"""
    print(menu)
    num = input('[1] 예   [2]아니요 : ')

    if num == '1':
        cursor.execute("INSERT INTO bookmark VALUES(:1, :2)", [ID, a]) 
        print('즐겨찾기 설정 완료')     
    elif num == '2':
        print("취소")

if __name__ == "__main__" :
    LOCATION = r"C:\instantclient_19_12"
    os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]

    con_ip = 'localhost:1521/xe'
    con_id = 'miniproject'
    con_pw = '0000'

    connect = cx_Oracle.connect(con_id, con_pw, con_ip)
    cursor = connect.cursor()

    ID = "test"  #user_history  

    search(cursor,ID)
    connect.commit()
    cursor.close()
    connect.close()