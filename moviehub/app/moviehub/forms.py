from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextField
from wtforms.validators import DataRequired

class EditMovieForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    director = StringField('Director', validators = [DataRequired()])
    rating = StringField('Rating : R, PG-13, PG, G', validators = [DataRequired()])
    runtime = IntegerField('Runtime in minutes', validators=[DataRequired()])
    cast = StringField('Cast', validators=[DataRequired()])
    genre = StringField('Genre',validators=[DataRequired()])
    year = IntegerField('Year',validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])
    storyline = TextField('Storyline', validators=[DataRequired()])
    stud_id = IntegerField('Studio Id', validators=[DataRequired()])
    submit = SubmitField('Update')


class CreateMovieForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    director = StringField('Director', validators = [DataRequired()])
    rating = StringField('Rating : R, PG-13, PG, G', validators = [DataRequired()])
    runtime = IntegerField('Runtime in minutes', validators=[DataRequired()])
    cast = StringField('Cast', validators=[DataRequired()])
    genre = StringField('Genre',validators=[DataRequired()])
    year = IntegerField('Year',validators=[DataRequired()])
    storyline = TextField('Storyline', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])
    stud_id = StringField('Studio Id', validators=[DataRequired()])
    submit = SubmitField('Update')
