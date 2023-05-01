from flask import *
from database import init_db, db_session
from models import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/updates")
def updates():
    return render_template("updates.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.before_first_request
def setup():
    init_db()

if __name__ == "__main__":
    app.run(debug=True)

