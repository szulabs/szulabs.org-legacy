from flask import render_template, flash, redirect, url_for
from flask.blueprints import Blueprint
from flask.ext.babel import lazy_gettext as _
from flask.ext.login import login_user

from szulabs.extensions import db, login_manager
from szulabs.account.forms import LoginForm, SignUpForm
from szulabs.account.models import UserAccount


account_app = Blueprint("account", __name__, template_folder="templates")

#: set login view to current blueprint
login_manager.login_view = "account.login"


@account_app.route("/login", methods=["GET", "POST"])
def login():
    """The login view and handler."""
    #: TODO support 'next' argument to back
    form = LoginForm()
    if form.validate_on_submit():
        account = UserAccount.query.get_by_email(form.email.data)
        if account and account.check_password(form.password.data):
            login_user(account)
        else:
            flash(_("The email has not been registered, "
                    "or the password is wrong."))
        #: TODO: where?
        return redirect(url_for("account.login"))
    return render_template("login.html", form=form)


@account_app.route("/signup", methods=["GET", "POST"])
def signup():
    """The sign up view and handler."""
    form = SignUpForm()
    if form.validate_on_submit():
        #: FIXME add a validator to confirm email has not been used
        account = UserAccount(email=form.email.data,
                              nickname=form.nickname.data)
        account.change_password(form.password.data)
        #: TODO need to send a confirmation email
        db.session.add(account)
        db.session.commit()
        #: success
        flash(_("Welcome to our site."))
        #: FIXME: where?
        return redirect(url_for("account.login"))
    return render_template("signup.html", form=form)
