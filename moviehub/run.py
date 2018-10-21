from app import create_app,db
from app.auth.models import User
from sqlalchemy import exc

flask_app = create_app('prod')

with flask_app.app_context():
    db.create_all()
    try:
        if not User.query.filter_by(user_name='joon').first():
            User.create_user(user='joon',email='joonyi@gmail.com',password='secret')

    except IntegrityError:
            flask_app.run()
