import pymysql


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Database@44',
                             database='transamount')




cur = connection.cursor()


connection1 = pymysql.connect(host='localhost',
                             user='root',
                             password='Database@44',
                             database='cementfactory')




cur1 = connection1.cursor()




















