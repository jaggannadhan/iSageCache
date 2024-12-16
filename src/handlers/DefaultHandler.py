from flask import Blueprint, render_template

default = Blueprint("default", __name__)


@default.route("/", methods=["GET"])
def landing():
    return render_template("pageNotFound.html")