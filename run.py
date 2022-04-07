from app import create_app, db
from app.auth.models import User

if __name__ == '__main__':
    flask_app = create_app('dev')

    with flask_app.app_context():
        db.create_all()

        if not User.query.filter_by(user_name="bambi").first():
            User.create_user(user="bambi",
                             email="abadareem@gmail.com",
                             password="squishyfos")

    flask_app.run()
