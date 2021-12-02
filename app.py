import os
from flask import Flask, render_template, request, flash, send_from_directory


app = Flask(__name__)
app.secret_key = "pass123"


@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/about", methods=['GET', 'POST'])
def about():
	return render_template("index.html")

@app.route("/resume", methods=['GET', 'POST'])
def resume():
	return render_template("resume.html")


@app.route('/favicon.ico')
def fav():
    return send_from_directory(os.path.join(app.root_path, 'static'),'icons/favicon.ico')





##def greeter():
##	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
##	return render_template("index.html")
