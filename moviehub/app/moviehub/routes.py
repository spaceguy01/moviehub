from app.moviehub import main
from app import db
from app.moviehub.models import Studio, Movie
from flask import render_template, flash, request, redirect, url_for
from flask_login import login_required
from app.moviehub.forms import EditMovieForm, CreateMovieForm


@main.route('/')
def display_movies():
    movies =  Movie.query.all()
    return render_template('home.html', movies=movies)

@main.route('/display/studio/<studio_id>')
def display_studio(studio_id):

    studio = Studio.query.filter_by(id=studio_id).first()
    studio_movies = Movie.query.filter_by(stud_id = studio.id).all()

    return render_template('studio.html', studio=studio, studio_movies=studio_movies)


@main.route('/delete/movie/<movie_id>',methods=['GET','POST'])
@login_required
def delete_movie(movie_id):
    movie = Movie.query.get(movie_id)

    if request.method == 'POST':
        db.session.delete(movie)
        db.session.commit()
        flash('Movie deleted successfully!')
        return redirect(url_for('main.display_movies'))
    return render_template('delete_movie.html', movie=movie, movie_id=movie.id)


@main.route('/edit/movie/<movie_id>', methods=['GET','POST'])
@login_required
def edit_movie(movie_id):
    movie = Movie.query.get(movie_id)
    form = EditMovieForm(obj=movie)

    if form.validate_on_submit():
        movie.title = form.title.data
        movie.director = form.director.data
        movie.rating = form.rating.data
        movie.runtime = form.runtime.data
        movie.cast = form.movie.data
        movie.genre = form.genre.data
        movie.year = form.year.data
        movie.storyline = form.storyline.data
        movie.stud_id = form.stud_id.data
        movie.image = form.image.data

        db.session.add(movie)
        flash("Movie has been edited successfully!")
        return redirect(url_for('main.display_movies'))
    return render_template('edit_movie.html', form=form)

@main.route('/create/movie/<stud_id>', methods=['GET','POST'])
@login_required
def create_movie(stud_id):
    form = CreateMovieForm()
    form.stud_id.data = stud_id # pre-populates stud_id

    if form.validate_on_submit():
        movie = Movie(title=form.movie.data, director=form.director.data, rating=form.rating.data,
                    runtime=form.runtime.data, cast=form.cast.data,genre=form.genre.rating.data,
                    year=form.year.data, storyline=form.storyline.data,image=form.image.data, stud_id=form.stud_id.data)
        db.session.add(movie)
        db.session.commit()
        flash("Move added successfully")

        return redirect(url_for('main.display_studio', stud_id=stud_id))
    return render_template('create_movie.html', form=form, stud_id=stud_id)
