import mysql.connector
import csv

u, p, l, d = ('uname', 'password', 'localhost', 'assignment1')

mydb = mysql.connector.connect(host=l, user = u, passwd=p, database=d)
mycursor = mydb.cursor()

f1 = list(csv.reader(open('dataset1.csv')))
f2 = list(csv.reader(open('dataset2.csv')))

for row in f1[1:]:
    row[0] = int(row[0])

for row in f2[1:]:
    row[0], row[2] = (int(row[0]), int(row[2]))

l1 = [tuple(i) for i in f1[1:]]
l2 = [tuple(i) for i in f2[1:]]

sql1 = "INSERT INTO table1 (ID_no, Cities, Pincode, Office_ID) VALUES (%s, %s, %s, %s)"
sql2 = "INSERT INTO table2 VALUES (%s, %s, %s)"
mycursor.executemany(sql1, l1)
mydb.commit()
mycursor.executemany(sql2, l2)
mydb.commit()

mydb.close()
