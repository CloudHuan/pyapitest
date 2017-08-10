import pymysql

'''
host=None, user=None, password="",
                 database=None
'''

class SqlHelper():

    myconnector = {
        'host': 'localhost',
        'user': 'root',
        'password': 'insta360',
        'database': 'cnote'
    }

    def __init__(self, host, database, user, password, ):
        try:
            self.connector = {'host': host, 'database': database, 'user': user, 'password': password};
        except pymysql.err.OperationalError as e:
            print(e)

    def __init__(self, connect_info=myconnector):
        self.connector = connect_info;

    def exec(self, sql='',args=[]):
        db = pymysql.connect(**self.connector)
        cursor = db.cursor();
        try:
            cursor.execute(sql,args);
            db.commit();
        except:
            db.rollback();
        finally:
            db.close();

    def query(self, sql='',args=[]):
        db = pymysql.connect(**self.connector)
        cursor = db.cursor();
        try:
            cursor.execute(sql,args);
            results = cursor.fetchall();
            return results;
        except:
            db.rollback();
        finally:
            db.close();

    def clearTable(self,t_name):
        self.exec('DELETE FROM '+t_name);

if __name__ == '__main__':
    myconnector = {
        'host': 'localhost',
        'user': 'root',
        'password': 'insta360',
        'database': 'cnote'
    }
    SqlHelper(myconnector).exec(
        'INSERT INTO account_user(name,pwd,phone,uid) VALUES(%s,%s,%s,%s)',['cczz3', '1111', '4555662013', 80]);
    results = SqlHelper(myconnector).query('SELECT * FROM account_user LIMIT %s',[3]);
    for result in results:
        print(result[2]);