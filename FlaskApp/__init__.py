from flask import Flask
app = Flask(__name__)
from flask import Flask, render_template, request, redirect, g 

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
	return render_template('about.html')
 
@app.route("/tech")
def tech():
	return render_template('tech.html')

if __name__ == "__main__":
    app.run()



