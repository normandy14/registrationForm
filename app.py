from flask import Flask, render_template, request
from dotenv import load_dotenv
import mysql.connector

import os

pass_ = os.environ.get("PASSWORD")

cnx = mysql.connector.connect(user='normandy14', password=pass_,
                              host='127.0.0.1',
                              database='registration')
              

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def html_form():
    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        data = request.form
        print (data)
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        account = request.form['account']
        
        sql = "INSERT INTO persons (firstname, lastname, email, account) VALUES ('{}', '{}', '{}', '{}');".format(firstName, lastName, email, account)
        cur = cnx.cursor()
        cur.execute(sql)
        cnx.commit()
    return render_template("app.html")

''''
@app.route("/form")
def form():
    sql = "SELECT * FROM persons"
    cur = cnx.cursor()
    cur.execute(sql)
    myresult = cur.fetchall()
    for x in myresult:
        print(x)
    
    
    sql = "INSERT INTO persons (firstname, lastname, email, account) VALUES ('Bob', 'Blue', 'blue@gmail.com', 'business');"
    cur = cnx.cursor()
    cur.execute(sql)
    cnx.commit()
    return ""
'''

if __name__ == "__main__":
   app.run()