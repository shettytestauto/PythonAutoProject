import getpass
import oracledb

connection = oracledb.connect(user="hr", password='admin', dsn="localhost/onerisk")

# print("Successfully connected to Oracle Database")

# cursor = connection.cursor()
# for row in cursor.execute("select * from employees where EMPLOYEE_ID = :mybv", mybv=102):
#     print(row)
# ------------- Cursors can be closed in various ways:---------------------------------

with connection.cursor() as cursor:
    for row in cursor.execute("select * from employees where EMPLOYEE_ID in ('101','102')"):
        print(row)


# ----------------  Cursors can be explicitly closed by calling close() ----------------

# cursor = connection.cursor()
# cursor.execute("select * from employees where EMPLOYEE_ID in ('101','102')")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
# cursor.close()

# -----------------Query Column Metadata-------------------------------
# cursor = connection.cursor()
# cursor.execute("select * from employees")
# for column in cursor.description:
#     print(column)

# ---------Changing Fetched Data Types with Output Type Handlers--------
# def output_type_handler(cursor, metadata):
#     if metadata.type_code is oracledb.DB_TYPE_NUMBER:
#         return cursor.var(oracledb.DB_TYPE_VARCHAR, arraysize=cursor.arraysize)
#
#
# cursor.outputtypehandler = output_type_handler
# cursor.execute("select 123 as col1, 'abc' as col2 from dual")
# for r in cursor.fetchall():
#     print(r)
