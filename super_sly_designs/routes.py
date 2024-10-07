from super_sly_designs.app import app
from flask import render_template, send_from_directory

@app.route('/')
def home():
  return render_template('home.html', title='Home')

@app.route('/about')
def about():
  return render_template('about.html', title='About Us')

@app.route('/contact')
def contact():
  return render_template('contact.html', title='Contact Us')

@app.route('/favicon.ico')
def favicon():
  return send_from_directory('static', 'images/favicon.ico')