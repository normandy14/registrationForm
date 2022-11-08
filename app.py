from flask import Flask, render_template
from dotenv import load_dotenv
import mysql.connector

import os

pass_ = os.environ.get("PASSWORD")

cnx = mysql.connector.connect(user='normandy14', password=pass_,
                              host='127.0.0.1',
                              database='registration')
                

app = Flask(__name__)

@app.route("/")
def html_form():
     return render_template("app.html")

if __name__ == "__main__":
   app.run()