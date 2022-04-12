import pymysql


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Makelabs@44',
                             database='cementfactory')




cur = connection.cursor()