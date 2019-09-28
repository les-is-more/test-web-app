from flask import Flask, abort, render_template, request, make_response, redirect
from flask_moment import Moment
from datetime import datetime

# This module will 
app = Flask(__name__)

moment = Moment(app)

@app.route('/')
def home():
    # response = make_response('<h1> This document carries cookies. </h1>')
    # response.set_cookie('answer', '42')
    # return response
    # user_agent = request.headers.get('User-Agent')
    return render_template("views/index.html", current_time=datetime.utcnow())

@app.route('/products')
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
    app.run(host = '0.0.0.0', port = 80, debug = True)