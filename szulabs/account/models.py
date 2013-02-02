from flask.ext.login import UserMixin

from szulabs.extensions import db, login_manager, bcrypt


class UserAccount(db.Model, UserMixin):
    """The user account of person or organization."""

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, index=True)
    nickname = db.Column(db.Unicode(20), unique=True)
    hashed_password = db.Column(db.String(60))

    class query_class(db.Query):

        def get_by_email(self, email):
            """Gets user account by email."""
            return self.filter_by(email=email).first()

    def change_password(self, new_password):
        """Changes user's account password."""
        self.hashed_password = bcrypt.generate_password_hash(new_password, 10)

    def check_password(self, input_value):
        """Checks input value is correct password or not."""
        return bcrypt.check_password_hash(self.hashed_password, input_value)

    def get_id(self):
        """Implemented."""
        return self.user_id


@login_manager.user_loader
def load_user(user_id):
    """Loads account model by user's account id."""
    return UserAccount.query.get(user_id)
