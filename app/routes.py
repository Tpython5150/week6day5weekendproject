from flask import render_template
from app import app

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/products')
def products():
   return render_template('products.html')

@app.route('/signup')
def sign_up():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cart')
def my_cart():
    return render_template ('cart.html')