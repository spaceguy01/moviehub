# app/moviehub/__init__.py

from flask import Blueprint

main = Blueprint('main', __name__, template_folder = 'templates')

from app.moviehub import routes