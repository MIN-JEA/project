import cx_Oracle
import os

os.putenv('NLS_LANG', '.UTF8')


def bookmark(cursor, ID):
	cursor.execute("select place from bookmark where id = :1", [ID])

	for i, v in enumerate(cursor):
		print(f"{i+1}. {v[0]}")


if __name__ == "__main__":
	cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_19_12")

	con_ip = 'localhost:1521/xe'
	con_id = 'miniproject'
	con_pw = '0000'
	connection = cx_Oracle.connect(con_id, con_pw, con_ip)
	cursor = connection.cursor()
	ID = 'test'
	bookmark(cursor, ID)
