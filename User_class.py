import cx_Oracle
import os
from haversine import haversine

LOCATION = r"C:\instantclient_19_12"
os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]  #환경변수 등록

connect = cx_Oracle.connect("MiniProject/0000@localhost:1521/xe")
cursor = connect.cursor()


class User:
    def __init__(self, ID, cursor):
        self.ID = ID
        self.cursor = cursor


    def __call__(self):
        while True:
            pick = input('[1] 주소검색 [2] 거리계산 [3] 유형별검색 [4] 인기검색어 [5] 히스토리 [6] 즐겨찾기 [7] 종료 : ')
            if pick == '1':
                self.search()
            elif pick == '2':
                self.distance()
            elif pick == '3':
                self.category()
            elif pick == '4':
                self.popularity()
            elif pick == '5':
                self.history()
            elif pick == '6':
                self.bookmark()
            elif pick == '7':
                print('종료')
                break
            else:
                print('명령어 오류')


    def search(self):
        try:
            place = input("장소명 : ")
            self.cursor.execute("select  도로명주소, 지번주소,  sysdate from jeju where 장소명 = :1 ", [place])
            result = self.cursor.fetchone()


            if result[0] == None:
                print(f"{place}의 주소 : {result[1]}")
            else:
                print(f"{place}의 주소 : {result[0]}")
            V = [self.ID, place, result[0], result[1], result[2]]
            self.cursor.execute("INSERT INTO user_history VALUES(:1, :2, :3, :4, :5)", V)


            menu = """즐겨찾기를 추가 하시겠습니까?"""
            print(menu)
            num = input('[1] 예   [2]아니요 : ')

            if num == '1':
                self.cursor.execute("INSERT INTO bookmark VALUES(:1, :2)", [self.ID, place])
                print('즐겨찾기 설정 완료')
            elif num == '2':
                print("취소")

        except:
            print("장소를 찾을 수 없습니다.")

    # distance 빠져나오기 구현 , 출발지 틀림 -> 메뉴로 while result1 is None
    def distance(self):

        s = (input("출발지 : "))

        self.cursor.execute("select 위도 , 경도 from jeju where 장소명 = :1 ", [s])
        result1 = self.cursor.fetchone()

        if result1 is None:
            print("출발지가 존재하지 않습니다.")


        g = (input("도착지 : "))

        self.cursor.execute("select 위도 , 경도  from jeju where 장소명 = :1 ", [g])
        result2 = self.cursor.fetchone()


        try:
            start = (float(result1[0]), float(result1[1]))
            goal = (float(result2[0]), float(result2[1]))
            print(haversine(start, goal))
        except:
            print("도착지가 존재하지 않습니다. 다시 입력하십시오")


    def category(self):

            item = input("카테고리(-공항 -숙소 -공원 -식당 -렌트 -게스트하우스 -펜션 -카페 -박물관) : ")
            item = '%' + item + '%'

            self.cursor.execute("select 장소명 , nvl(도로명주소 , 지번주소) from jeju where 장소명 like :1 ", [item])
            result = self.cursor.fetchall()
           # print(result)
            for i, v in enumerate(result):
                print(f"{i + 1}. {v}")

            if result == []:
                print("항목이 존재하지 않습니다.")


    def popularity(self):
        self.cursor.execute("""select *
                        from (select place
                                from user_history
                                group by place
                                order by count(*) DESC)
                        where rownum <= 10""")

        for i, v in enumerate(self.cursor):
            print(i + 1, v[0])


    def history(self):

        menu = """
    =================================
        menu
    1. 주소 검색 
    =================================
    """
        num = None
        while num is None:
            print(menu)
            print("Select menu: ")
            num = input()
            if num == '1':
                self.cursor.execute("select place, adress, roadname, to_char(search_time, 'YY.MM.DD/HH:MI') from user_history where id = :1", [self.ID])

                for list in self.cursor:
                    print(list)
                print("주소로 검색 완료")


            # elif num == '2':
            #     self.cursor.execute("select place, roadname from user_history where id = :1", [self.ID])
            #
            #     for list in self.cursor:
            #         print(list)
            #     print("도로명 주소로 검색 완료")


    def bookmark(self):
        cursor.execute("select place from bookmark where id = :1", [self.ID])

        for i, v in enumerate(cursor):
            print(f"{i + 1}. {v[0]}")


if __name__ == "__main__":
    user = User("park", cursor)
    user()
    connect.commit()
    cursor.close()
    connect.close()