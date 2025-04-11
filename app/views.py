from flask import request, jsonify, send_from_directory
from app import app, db
from app.forms import MovieForm
from app.models import Movie
from flask_wtf.csrf import generate_csrf
import os

# Ensure uploads directory exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

def form_errors(form):
    """Return a list of form errors"""
    error_messages = []
    for field, errors in form.errors.items():
        for error in errors:
            error_messages.append({
                "field": field,
                "message": error
            })
    return error_messages

@app.route('/api/v1/movies', methods=['POST'])
def add_movie():
    form = MovieForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        poster = form.poster.data

        # Save the poster file
        poster_filename = poster.filename
        poster.save(os.path.join('uploads', poster_filename))

        # Create a new movie instance
        new_movie = Movie(title=title, description=description, poster=poster_filename)
        db.session.add(new_movie)
        db.session.commit()

        return jsonify({
            "message": "Movie Successfully added",
            "title": title,
            "poster": poster_filename,
            "description": description

        }), 201
    else:
        return jsonify({"errors": form_errors(form)}), 400

@app.route('/api/v1/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify({"movies": [{"id": movie.id, "title": movie.title, "description": movie.description, "poster": f"/api/v1/posters/{movie.poster}"} for movie in movies]})

@app.route('/api/v1/posters/<filename>')
def get_poster(filename):
    return send_from_directory('uploads', filename)

@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})
