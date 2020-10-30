import datetime
import cx_Oracle            # https://developer.oracle.com/dsl/prez-python-queries.html

# dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XE')
# conn = cx_Oracle.connect(user='scott', password='tiger', dsn=dsn_tns)
# cur = conn.cursor()



try:
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XE')
    conn = cx_Oracle.connect(user='scott', password='tiger', dsn=dsn_tns)
    cur = conn.cursor()
except Exception as e:
    print(e)
# finally:
#     if cur:
#         cur.close()
#     if conn:
#         conn.close()

date = str(datetime.datetime.now().date())
class Test():
    def __init__(self):
        print('status     -- >    ' + str(conn))


tt = Test()
Test();

print('---------------')
print(cur)





#
#create table userlist(username varchar2(9), password varchar2(9));
#insert into userlist values ('sanjay','sanjay');
#insert into userlist values ('san','sanjay');
#commit;
#
#

