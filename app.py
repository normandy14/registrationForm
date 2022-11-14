from flask import Flask, render_template, request
from dotenv import load_dotenv
import hashlib
import mysql.connector

import os

user_ = os.environ.get("USER")
pass_ = os.environ.get("PASSWORD")

cnx = mysql.connector.connect(user=user_, password=pass_,
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
        password = request.form['password'] + "SuperThresh212" # add salt to form password
        account = request.form['account']
        
        hashedPassword = hashlib.sha256(password.encode()).hexdigest()
        
        sql = "INSERT INTO persons (firstname, lastname, email, password, account) VALUES ('{}', '{}', '{}', '{}', '{}');".format(firstName, lastName, email, hashedPassword, account)
        cur = cnx.cursor()
        cur.execute(sql)
        cnx.commit()
    return render_template("app.html")


if __name__ == "__main__":
   app.run()