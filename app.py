from flask import Flask, render_template, request, flash, send_from_directory


app = Flask(__name__)
app.secret_key = "pass123"


@app.route("/profile")
def index():
	#flash("What's your name?")
	flash("hernan.gavilan@outlook.com")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html")

@app.route('/favicon.ico')
def fav():
    return send_from_directory(os.path.join(app.root_path, 'static'),'icons/favicon.ico')