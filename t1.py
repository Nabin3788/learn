from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/blog'
# //name	email	phone_no	message	serial	date	

class Contacts(db.Model):
    serial = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_no= db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

@app.route("/")
def hello():
    return render_template('index.html')

# @app.route("/about")
# def harry():
#     name = "rohan das"
#     return render_template('about.html', name2= name)

# @app.route("/bootstrap")
# def bootstrap():
#     return render_template('bootstrap.html')

app.run(debug=True)
