from flask import Flask, render_template, request, flash
from dotenv import load_dotenv # for loading secret values in .env file
import hashlib # this is for hashing passwords
import mysql.connector # this is for connection to a MySQL databse
from pymongo import MongoClient # this is for connection to a Mongodb NoSQL database

# the following is for form validation on server side
from flask_wtf import FlaskForm 
from wtforms import (StringField, TextAreaField, PasswordField, IntegerField, RadioField, SelectField, EmailField)
from wtforms.validators import InputRequired, Length, Email, Regexp, NumberRange, Optional

# used to read the  environment variables
import os

# obtain sensitive information using os module in .env file
user_ = os.environ.get("USER")
pass_ = os.environ.get("PASSWORD")

# connection to a local instance ('127.0.0.1') of a MySQL database
# hide the user and password fields for security
# database name for this instance is 'registration' (choose any optional name)

cnx = mysql.connector.connect(user=user_, password=pass_,
                              host='127.0.0.1',
                              database='registration')
            
# this is the instance for the Mongodb database
# assumes NoSQL databse is local with 'localhost' in 'client'
# port to listen to is '27017' (this is the default port for a new installation)
# 'db', connects to a database named 'flask_db' (created manually in Mongodb)
# 'users', conneects to these documents, 'users', in the 'flask_db' database

client = MongoClient("localhost", 27017)
db = client.flask_db 
users = db.users

# a secret key is required to generate a 'form.csrf_token'
# assume secret key is secret, so store in .env file and recover value below

secretKey = os.environ.get("

app = Flask(__name__)

app.secret_key = secretKey.encode('utf8')

# from 'flask_wtf', import these validation fields (String, Email, Password, Radio, Integer, Select, Text, etc.) to vertify format in backend
class Form(FlaskForm):
    firstName = StringField('firstName', validators=[InputRequired()])
    lastName = StringField('lastName', validators=[InputRequired()])
    email = EmailField('email', validators=[InputRequired(), Length(4, 128), Email()])
    password = PasswordField('password', validators=[InputRequired(), Length(6, 12), Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])')])
    account = RadioField('account', choices=['personal', 'business'], validators=[InputRequired()])
    
    age = IntegerField('age', validators=[NumberRange(min=13, max=120), Optional()])
    referrer = SelectField(choices=['', 'freeCodeCamp News', 'freeCodeCamp Youtube Channel', 'freeCodeCamp Forum', 'Other'], validators=[Optional()])
    bio = TextAreaField('bio', validators=[Length(max=280), Optional()])
    
@app.route("/", methods=['GET', 'POST'])
def html_form():
    form = Form()
    if form.validate_on_submit():
        print("success")
    else:
        print("not successful")
  
    if request.method == 'POST':
            
        data = request.form
        print (data)
        
        form = Form()
        if form.validate_on_submit():
            print("success")
            # the following fields will be stored in a local MySQL databse
            firstName = (request.form['firstName']).lower()
            lastName = (request.form['lastName']).lower()
            email = (request.form['email']).lower()
            password = request.form['password'] + "SuperThresh212" # add salt to form password
            account = request.form['account']
            
            # the following fields will be stored in a local Mongodb NoSQL database
            age = request.form['age']
            referrer = request.form['referrer']
            bio = request.form['bio']
            
            # we hash the password after adding salt
            hashedPassword = hashlib.sha256(password.encode()).hexdigest()
            
            # will equal an error if there is an error with inserting values into MySQL database and/or Mongodb database
            error = ""
            
            # did not use SQLalchemy, need to patch SQL injection
            # MySQL try/catch
            try:
                sql = "INSERT INTO persons (firstname, lastname, email, password, account) VALUES ('{}', '{}', '{}', '{}', '{}');".format(firstName, lastName, email, hashedPassword, account)
                cur = cnx.cursor()
                cur.execute(sql)
                cnx.commit()
                cur.close()
            except mysql.connector.IntegrityError:
                print ("email already registered in MySQL database")
                error = "Email already registered!"
            
            # Mongodb if/else
            if users.count_documents({ '_id': email }, limit = 1):
                print ("email already exists in MongoDB")
                error = "Email already registered!"
            else:
                users.insert_one({ '_id': email, 'age': age, 'referrer': referrer, 'bio': bio})
            
            # flash 'email already registered error' in render_template
            # two checks because MySQL is independant of Mongodb database
            if error != "":
                flash(error)
                return render_template("app.html", form=form)
            else:
                message = "Form sumission was successful!"
                flash(message)
                return render_template("app.html", form=form)

        else:
            # validation with flask_wtf failed
            # usually because of 'evil' user input (purposeful hacking)
            error = "Form submission was unsuccessful!"
            flash(error)
    # for populates template in 'app.html' with values from this backend
    return render_template("app.html", form=form) 


if __name__ == "__main__":
   app.run()