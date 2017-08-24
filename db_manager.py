# conding:utf-8
import MySQLdb

class Db_Manager(object):
    def __init__(self):
        self.conn = MySQLdb.Connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = '123456', db='cook', charset='utf8')

    def add(self, data):
        corsor = self.conn.cursor()
        sql = "insert into book (name, writer, url, tap, updates) values ('%s', '%s', '%s', '%s', '%s')" % (data['name'], data['writer'], data['url'], data['tag'], data['update'])
        print sql
        try:
            corsor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print e
        finally:
            corsor.close()

    def close(self):
        self.conn.close()