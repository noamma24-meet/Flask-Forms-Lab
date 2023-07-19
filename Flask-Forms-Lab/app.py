from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "noam"
password = "123"
facebook_friends=["ava","hila","george","yuka"]


@app.route('/', methods=['GET','POST'])  # '/' for the default page
def login():
	if request.method =='POST':
		user=request.form["username"]
		passy=request.form["password"]
		if user==username and passy==password:
			return redirect(url_for('home'))
	return render_template('login.html')

@app.route('/home')
def home():
	return render_template("home.html", friends=facebook_friends)

@app.route('/friend_exists/<string:name>', methods=['GET','POST'])
def friends(name):
	if name in facebook_friends:
		return render_template("/friend_exists.html", status="True")
	else:
				return render_template("/friend_exists.html", status="False")



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		debug=True
	)

