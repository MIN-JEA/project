
class Admin():
    def __init__(self, ID, cursor) :
        self.ID = ID
        self.cursor = cursor
    
    def __call__(self):
        while True:
            pick = input("[1] set_table, [2] show_table_list, [3]show_working_table, [4] add_tuple, [5] delete_tuple, [6] find_tuple, [7] 종료  :  ")
            if pick == '1':
                self.set_table()
            elif pick == '2':
                self.show_table_list()
            elif pick == '3':
                self.show_working_table()
            elif pick == '4':
                self.add_tuple()
            elif pick == '5':
                self.delete_tuple()
            elif pick == '6':
                self.find_tuple()
            elif pick == '7':
                break
            else:
                print('잘못된 명령어 입니다.')

    def set_table(self):
        print('편집할 테이블을 선택합니다.')
        self.cursor.execute('select table_name from user_tables')
        table_list = self.cursor.fetchall()
        for i, v in enumerate(table_list):
            print(f"{i+1}. {v[0]}")
        pick = int(input('테이블을 선택하세요. : '))
        self.table = table_list[pick-1][0]
        print(f"{self.table} 을 선택하셨습니다.")

    def show_table_list(self):
        print('------테이블 목록------')
        self.cursor.execute('select * from user_tables')
        for i, v in enumerate(self.cursor):
            print(f"{i+1}. {v[0]}")
        print()

    def show_working_table(self):
        try:
            print(f"현재 작업중인 테이블은 {self.table} 입니다.")
            self.cursor.execute(f'select * from {self.table}')
            for i, v in enumerate(self.cursor):
                print(f"{i+1}. {v}")
        except:
            print('==테이블을 선택해주세요==')


    def add_tuple(self):
        try:
            self.cursor.execute(f"select column_name, data_type, nullable from cols where table_name = '{self.table}'")
            values = []
            for colname, datatype, nullable in self.cursor:
                print(f'column_name = {colname}, datatype = {datatype}, nullable = {nullable}')
                # values.append(input("값을 입력하세요 : "))
                data = input('값을 입력하세요 : ')
                if datatype == 'NUMBER':
                    data = int(data)
                elif datatype == 'VARCHAR2':
                    data = str(data)
                if (nullable == 'N') and (data is None):
                    raise TypeError
                print('입력값 오류! 다시 실행합니다.')
                self.add_tuple()

                values.append(data)

                values = tuple(values)
                self.cursor.execute(f"insert into {self.table} values {values}")
                print('추가 완료')
        except:
            print('===테이블을 선택해주세요===')

    def delete_tuple(self):
        try:
            self.cursor.execute(
                f"""select cols.column_name
                    from user_constraints cons, user_cons_columns cols
                    where cons.table_name = upper('{self.table}')
                    and cons.constraint_type = 'P'
                    and cons.owner = cols.owner
                    and cons.constraint_name = cols.constraint_name""")
            pk_list = []
            for i in self.cursor:
                pk_list.append(i[0])
            print(f"pk is {pk_list}")
            values = []
            for i in pk_list:
                values.append(input(f"{i}값 입력 : "))

            op = []
            for pk, v in zip(pk_list, values):
                op.append(pk + " = '" + v + "'")
            condition = " and ".join(op)

            self.cursor.execute(f"delete from {self.table} where {condition}")
            print('데이터삭제를 시작합니다.')
        except:
            print('===테이블을 선택해주세요===')

    def find_tuple(self):
        try:
                self.cursor.execute(f"select column_name, data_type from cols where table_name = '{self.table}'")
                for colname, datatype in self.cursor:
                    print(f'column_name = {colname}, datatype = {datatype}')
                condition = [input('컬럼을 입력하세요. : '), input('데이터를 입력하세요. :')]
                self.cursor.execute(f"select * from {self.table} where {condition[0]} = '{condition[1]}'")
                result = self.cursor.fetchall()
                for i, v in enumerate(result):
                    print(f"{i+1}. {v}")
                return result
        except:
            print('===테이블을 선택해주세요===')


if __name__ == "__main__":
    import cx_Oracle
    import os 
    LOCATION = r"C:\instantclient_19_12"
    os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]  # 환경변수 등록

    connect = cx_Oracle.connect("hr/hr@localhost:1521/xe")
    cursor = connect.cursor()
    ID = 'admin'

    admin = Admin(ID, cursor)
    admin()
    # admin.show_table_list()
    # admin.set_table()
    # admin.show_working_table()
    # admin.find_tuple()

