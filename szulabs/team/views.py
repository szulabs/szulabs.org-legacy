from flask import render_template
from flask.blueprints import Blueprint


team_app = Blueprint("team", __name__, template_folder="templates")


@team_app.route("/")
def home():
    return render_template("home.html")
