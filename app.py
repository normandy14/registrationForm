from flask import Flask, render_template, request
from dotenv import load_dotenv
import hashlib
import mysql.connector
from pymongo import MongoClient

from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, PasswordField, IntegerField, RadioField, SelectField, EmailField)
from wtforms.validators import InputRequired, Length, Email


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

HOUR_CHOICES = [('1', '8am'), ('2', '10am')]


class Form(FlaskForm):
    # Mysql
    firstName = StringField('firstName', validators=[InputRequired()])
    lastName = StringField('lastName', validators=[InputRequired()])
    
    email = EmailField('email', validators=[InputRequired(), Length(4, 128), Email()])

    password = PasswordField('password', [
        validators.InputRequired() #,validators.EqualTo('confirm', message='Passwords must match')
    ])
    
    account = RadioField('account',
                       choices=['Beginner', 'Intermediate', 'Advanced'],
                       validators=[InputRequired()])
    
    # Mongodb
    age = IntegerField('age', validators=[InputRequired()])
    # referrer = SelectField(choices=[('personal', 'Personal Account'), ('business', ' Business Account')])
    bio = TextAreaField('bio', 
                        validators=[InputRequired(),
                        Length(max=200)])

@app.route("/", methods=['GET', 'POST'])
def html_form():
    if request.method == 'POST':
        data = request.form
        print (data)
        form = Form()
        if form.validate_on_submit():
            print("success")
        else:
            print("not successful")
        '''
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
    return render_template("app.html")


if __name__ == "__main__":
   app.run()