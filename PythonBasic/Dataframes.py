import pandas as pd
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
try:
   engine = sqlalchemy.create_engine("oracle+oracledb://hr:admin@localhost/?service_name=onerisk", arraysize=1000)
   orders_sql = """select * from employees where EMPLOYEE_ID in ('101','102')""";
   df_orders = pd.read_sql(orders_sql, engine)
   details_sql = """select * from employees where EMPLOYEE_ID in ('103')""";
   df_details = pd.read_sql(details_sql, engine)
   print(df_orders)
   print(df_details)
   data_12 = df_orders.merge(df_details, indicator=True, how='outer')
   print(data_12)
   data_diff = data_12.loc[lambda x : x['_merge'] != 'both']
   print(data_diff)
except SQLAlchemyError as e:
   print(e)