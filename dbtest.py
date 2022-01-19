import pymysql

conn = pymysql.connect(host='database-1.cd3lh4w1vr3o.ap-northeast-2.rds.amazonaws.com',db='pbldb',port=3306,passwd='chd2stiny',user='admin')
print(conn)
conn.close()


