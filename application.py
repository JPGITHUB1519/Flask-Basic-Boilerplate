from flask import Flask, url_for, render_template
from dbqueries import *
# flask app
app = Flask(__name__)
# change default folders
# template_folder -> change folder templates, static_folder = change static folder
#app = Flask(__name__, template_folder="templates_finalproject", static_folder="static_finalproject")

# view
@app.route('/')
def index():
	return "<h1>Hello World</h1>"

@app.route('/welcome')
def welcome():
	return render_template("index.html")

@app.route('/hello/<username>')
def hello(username):
	return render_template("welcome.html", username=username)

@app.route('/users')
def listUsers():
	users = getUsers()
	return render_template('users.html', users=users)

if __name__=='__main__':
	app.run(debug=True)