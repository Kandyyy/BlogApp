from flask import Blueprint, redirect, render_template

error = Blueprint("error", __name__)

@error.app_errorhandler(404)
def error_404(error):
    return render_template("error_pages/404.html"), 404
