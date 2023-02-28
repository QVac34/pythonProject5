# import sqlite3
#
# connection = sqlite3.connect("itstep_DB.sl3", 5)
# cur = connection.cursor()
# print(connection)
# print (cur)
# connection.close()
import sqlite3
connection = sqlite3.connect("C:\itstep.sl3", 5)
cur = connection.cursor()
cur.execute("CREATE TABLE first_table (name TEXT);")
# cur.execute("INSERT INTO first_table (name) "
#             "VALUES ('Nick');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Ann');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Kats');")
# cur.execute("INSERT INTO first_table (name) VALUES ('John');")
connection.commit()
# res = cur.commit()
# print(res)
connection.close()