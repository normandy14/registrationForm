from flask import Flask, render_template, request
from dotenv import load_dotenv
import hashlib
import mysql.connector
from pymongo import MongoClient

from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, PasswordField, IntegerField, RadioField, SelectField, EmailField)
from wtforms.validators import InputRequired, Length, Email, Regexp, NumberRange


import os

user_ = os.environ.get("USER")
pass_ = os.environ.get("PASSWORD")

cnx = mysql.connector.connect(user=user_, password=pass_,
                              host='127.0.0.1',
                              database='registration')
              
client = MongoClient("localhost", 27017)
db = client.flask_db
users = db.users

app = Flask(__name__)

app.secret_key = 'GreenZed55'.encode('utf8')

class Form(FlaskForm):
    # Mysql
    firstName = StringField('firstName', validators=[InputRequired()])
    lastName = StringField('lastName', validators=[InputRequired()])
    email = EmailField('email', validators=[InputRequired(), Length(4, 128), Email()])
    password = PasswordField('password', validators=[InputRequired(), Length(6, 12), Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])')])
    account = RadioField('account',
                       choices=['personal', 'business'],
                       validators=[InputRequired()])
    
    # Mongodb
    age = IntegerField('age', validators=[NumberRange(min=13, max=120)])
    referrer = SelectField(choices=['', 'freeCodeCamp News', 'freeCodeCamp Youtube Channel', 'freeCodeCamp Forum', 'Other'])
    bio = TextAreaField('bio', validators=[Length(max=280)])
    
@app.route("/", methods=['GET', 'POST'])
def html_form():
    form = Form()
    if form.validate_on_submit():
        print("success")
    else:
        print("not successful")
    '''
    if request.method == 'POST':
  
        data = request.form
        print (data)
        form = Form()
        if form.validate_on_submit():
            print("success")
        else:
            print("not successful")
            
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        password = request.form['password'] + "SuperThresh212" # add salt to form password
        account = request.form['account']
        
        age = request.form['age']
        referrer = request.form['referrer']
        bio = request.form['bio']
        
        users.insert_one({ '_id': email, 'age': age, 'referrer': referrer, 'bio': bio})
        
        hashedPassword = hashlib.sha256(password.encode()).hexdigest()
        
        sql = "INSERT INTO persons (firstname, lastname, email, password, account) VALUES ('{}', '{}', '{}', '{}', '{}');".format(firstName, lastName, email, hashedPassword, account)
        cur = cnx.cursor()
        cur.execute(sql)
        cnx.commit()
        '''
    return render_template("app.html", form=form)


if __name__ == "__main__":
   app.run()