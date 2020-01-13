from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='uname', passwd='password', database='assignment1')

app = Flask(__name__)


#for SQLAlchemy mysql://username:password@hostname/database

@app.route('/')
def main():
    mycursor = mydb.cursor()
    query = "SELECT table1.Pincode, SUM(table2.Population) FROM table1 INNER JOIN table2 ON table1.Office_ID=table2.Office_ID WHERE table1.Cities='Jaipur' GROUP BY table1.Pincode;"
    mycursor.execute(query)
    result = mycursor.fetchall()
    return str(result)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
