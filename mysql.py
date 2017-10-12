# coding=utf-8
#!/usr/bin/python3
 
 # pip3  install PyMySQL

import pymysql
import time;
 
# 打开数据库连接
connection = pymysql.connect(host="localhost",user="root",passwd="root",db="test",charset="utf8")

# 使用 cursor() 方法创建一个游标对象 cursor
with connection.cursor(pymysql.cursors.DictCursor) as cursor:
  cursor.execute("set names 'utf8'")  
  # 使用 execute()  方法执行 SQL 查询 
  cursor.execute("drop table if exists member")
  cursor.execute("""
            CREATE TABLE member (
            id int AUTO_INCREMENT,
            name varchar(20) null, 
            age int null, 
            createTime bigint null,
            PRIMARY KEY (`id`))
            """)
  currentTime = time.time();
  members = [(None,'keeley_%d' % i, i,currentTime) for i in range(1,10)]
  cursor.executemany("insert into member values (%s,%s,%s,%s)", members)
  connection.commit()
  cursor.execute("SELECT * from member")

  for m in cursor.fetchall():
    print (m)
