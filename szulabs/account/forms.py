from flask.ext.babel import lazy_gettext as _
from flask.ext.wtf import Form, TextField, PasswordField, SubmitField
from flask.ext.wtf import required, email, length, equal_to


class LoginForm(Form):
    """The login form."""

    email = TextField(_("Email"), [required(), email()])
    password = PasswordField(_("Password"), [required(), length(min=6)])
    submit = SubmitField(_("Login"))


class SignUpForm(Form):
    """The sign up form."""

    email = TextField(_("Email"), [required(), email()])
    nickname = TextField(_("Nick Name"), [required(), length(max=20)])
    password = PasswordField(_("Password"), [required(), length(min=6)])
    confirm_password = PasswordField(_("Confirm Password"),
                                     [equal_to("password")])
    submit = SubmitField(_("Sign Up"))
