# Registration Form

An implementation of a registration form from [FreeCodeCamp](https://www.freecodecamp.org/learn/2022/responsive-web-design/learn-html-forms-by-building-a-registration-form/step-1)

A snapshot of the program: 

![snapshot](static/img/profile.PNG)

## Description

This project is used to practice front-end and back-end development. Gathering information from the user in the form from a user is essential for almost every web application. Storing the information in a database is essential.

For practicing of both SQL and NoSQL databases, this project uses a local MySQL database and local Mongodb NoSQL database to store information. The design choice is justified because the MySQL stores data essential to the user login information (first name, last name, email, password, etc.), while the Mongodb NoSQL database stores information optional to the user (age, referral, bio, etc.).

Implentation of form built with the following technologies:

* :snake: Python/Flask/Pipenv
* :writing_hand: Git
* :writing_hand: HTML5/CSS3
* :cloud: MySQL
* :cloud: Mongodb

This project also used the following Python modules:

* [dotenv](https://pypi.org/project/python-dotenv/)
* [hashlib](https://pypi.org/project/hashlib/)
* [mysql.connector](https://pypi.org/project/mysql-connector-python/)
* [pymongo](https://pypi.org/project/pymongo/)
* [flask-wtf](https://pypi.org/project/Flask-WTF/)

This project uses .env to record secrets: MySQL username, password, secretkey to not commit this important information to github

See the following pattern:

```
import os 
 
# obtain sensitive information using os module in .env file from pipenv shell
user_ = os.environ.get("USER") 
pass_ = os.environ.get("PASSWORD")

# use user_ and pass_ in code
```

The .env file it listed in .gitignore and should never be uploaded to github or committed locally in git because it contains sensitive data

This project uses [pipenv](https://pipenv.pypa.io/en/latest/) globally to install Python modules, load .env file, and start the flask server

## Getting Started

### Dependencies

* Requires Java Development Kit, JDK

### Installing

* To install the ava Development JDK, [JDK](https://docs.oracle.com/en/java/javase/17/install/overview-jdk-installation.html#GUID-8677A77F-231A-40F7-98B9-1FD0B48C346A)

### Executing program

The easiest method is the following:
* Install Eclipse, or equivalent Java IDE
* Import folders in this repo as new Java Projects
* Select a project and run in Java IDE

## License

This project is licensed under the GNU General Public License v3.0 [License](License.md) - see the LICENSE.md file for details

## Authors

* :ocean: **Normandy14** - *Initial work* - [Github Account](https://github.com/Normandy14)
