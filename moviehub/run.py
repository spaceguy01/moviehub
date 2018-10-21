from app import create_app,db
from app.auth.models import User

if __name__== '__main__':
    flask_app = create_app('prod')

    with flask_app.app_context():
        db.create_all()
        if not User.query.filter_by(user_name='joon').first():
            User.create_user(user='joon',email='joonyi@gmail.com',password='secret')

    flask_app.run()