from flask import render_template, flash, redirect, url_for
from flask.blueprints import Blueprint
from flask.ext.babel import lazy_gettext as _
from flask.ext.login import login_user

from szulabs.extensions import login_manager
from szulabs.account.forms import LoginForm
from szulabs.account.models import UserAccount


account_app = Blueprint("account", __name__, template_folder="templates")

#: set login view to current blueprint
login_manager.login_view = "account.login"


@account_app.route("/login", methods=["GET", "POST"])
def login():
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
