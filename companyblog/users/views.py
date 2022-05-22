from flask import redirect, render_template, Blueprint, request, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from companyblog import db
from companyblog.models import User, BlogPost
from companyblog.users.forms import LoginForm, RegisterForm, UpdateUserForm
from companyblog.users.picture_handler import add_profile_picture

users = Blueprint("users", __name__)

@users.route("/")
def logout():
    logout_user()
    return redirect(url_for("core.index"))

@users.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("users.login"))
    return render_template("register.html", form=form)

@users.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("Login successful!")
            next = request.args.get("next")
            if next == None or not next[0] == "/":
                next = url_for("core.index")
            return redirect(next)
    return render_template("login.html", form=form)