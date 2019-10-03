from flask import Flask, abort, render_template, request, make_response, redirect
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
# from flask_bootstrap import Bootstrap

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# This creates the SQL ORM feature of the app
from flask_sqlalchemy import SQLAlchemy

from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator

# from customClass.models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Chicken Noodle Soup'


# This module will create instances for SQL Model and Moment
db = SQLAlchemy(app)
moment = Moment(app)

# Add bootstrap elements for the app

# # Registering Navbar elements
# nav = Nav(app)
# nav.register_element('my_navbar', Navbar(
#     'Lizzie!',
#     View('Home','home'),
#     View('Login', 'login'),
#     View('About','about'),
#     Subgroup('Product',View("Product", 'products'),
#         View('List', 'product_list')),
#     View('You', 'user',name="migs")
# ))

# Forms template
class captureUserDetails(FlaskForm):
    # def __init__(self,event):     
    #     self.event = event
    
    # def Fields(self):
    uid = StringField('Preferred User ID', validators=[DataRequired()])
    pwd = StringField('Password',validators=[DataRequired()])
        # if self.event == 'signup':
    firstName = StringField('First Name',validators=[DataRequired()] )
    lastName = StringField('Last Name',validators=[DataRequired()])
        #     submit = SubmitField('Sign Up')
        # else:
    submit = SubmitField('Login')

class SignInForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("views/landing.html")

@app.route('/login', methods=['GET','POST'])
def login():
    # name= None
    captureForm = captureUserDetails()
    # if loginForm.validate_on_submit():
    #     loginForm.name.Data = ''
    return render_template("views/loginORsignup.html", 
        form=captureForm,
        current_time=datetime.utcnow())

@app.route('/products')
def products():
    return render_template('views/products.html')

@app.route('/product/list')
def product_list():
    return {
        'product' :  ['Ice Cream', 'Chocolate', 'Fruit','Mango']
        }

@app.route('/user/<string:name>')
def user(name):
    return render_template('views/user.html', name = name)

@app.route('/about')
def about():
    return render_template('views/about.html') 

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404


if __name__ == '__main__':
    app.run(ssl_context=('certs/cert.pem','certs/key.pem'),host = '0.0.0.0', port = 80, debug = True)