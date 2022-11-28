# Registration Form

An implementation of a registration form
![snapshot](static/img/profile.PNG)

## Description

Implentation of form built with the following technologies

* :snake: Python/Flask/Pipenv
* :writing_hand: Git
* :writing_hand: HTML5/CSS3
* :cloud: MySQL
* :cloud: Mongodb

This project uses .env to record secrets: MySQL username, password, secretkey to not commit this important information to github
This project uses 3rd party Python modules such as the following: dotenv, hashlib, mysql.connector, ppymongo, flask_wtf

Why does this project have 2 databases?
MySQL is best for information strongly associated with user account, such as name, email, and password
Mongodb is best for storing preferences and optional information from the user, so that the web app can offer a customized version of the app when he or she logs on

The fields collected from the user are of the following:

* First Name
* Last Name
* Email
* Password
* Account Type (Personal  or Business)
* Age
* Referral
* Bio



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
