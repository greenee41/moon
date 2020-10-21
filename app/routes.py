from flask import render_template
from app import app
 
@app.route('/')
@app.route('/index')
def index():
	# user = {'usrername' : 'lyana'}
	return render_template('index.html')
	
@app.route('/snoop')
def snoop():
	return render_template('snoop.html')

@app.route('/about')
def about():
	return render_template('about.html')