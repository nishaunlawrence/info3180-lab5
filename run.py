from flask import Flask, request, jsonify, send_from_directory, make_response
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create the Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'default-key-for-dev'
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')

# Ensure uploads directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Mock movies database with a sample movie
movies = [
    {
        "id": 1,
        "title": "Sample Movie",
        "description": "This is a sample movie description for testing.",
        "poster": "sample.jpg"
    }
]

# Add CORS headers
@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,X-CSRFToken')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/api/v1/movies', methods=['POST', 'OPTIONS'])
def add_movie():
    logger.debug(f"Received request: {request.method} to /api/v1/movies")
    logger.debug(f"Headers: {request.headers}")
    
    if request.method == 'OPTIONS':
        return make_response(), 200
        
    # Simple mock implementation
    logger.debug(f"Form data: {request.form}")
    logger.debug(f"Files: {request.files}")
    
    if 'title' not in request.form or 'description' not in request.form or 'poster' not in request.files:
        return jsonify({"errors": [{"field": "general", "message": "Missing required fields"}]}), 400
    
    title = request.form['title']
    description = request.form['description']
    poster = request.files['poster']
    
    # Save the poster file
    poster_filename = poster.filename
    poster.save(os.path.join(app.config['UPLOAD_FOLDER'], poster_filename))
    
    # Create a new movie 
    movie_id = len(movies) + 1
    new_movie = {
        "id": movie_id,
        "title": title,
        "description": description,
        "poster": poster_filename
    }
    movies.append(new_movie)
    
    logger.debug(f"Added new movie: {new_movie}")
    
    return jsonify({
        "message": "Movie Successfully added",
        "title": title,
        "poster": poster_filename,
        "description": description
    }), 201

@app.route('/api/v1/movies', methods=['GET', 'OPTIONS'])
def get_movies():
    logger.debug(f"Received request: {request.method} to /api/v1/movies")
    
    if request.method == 'OPTIONS':
        return make_response(), 200
        
    logger.debug(f"Returning movies: {movies}")
    return jsonify({"movies": [{"id": movie["id"], "title": movie["title"], "description": movie["description"], "poster": f"http://localhost:5001/api/v1/posters/{movie['poster']}"} for movie in movies]})

@app.route('/api/v1/posters/<filename>', methods=['GET', 'OPTIONS'])
def get_poster(filename):
    logger.debug(f"Received request for poster: {filename}")
    
    if request.method == 'OPTIONS':
        return make_response(), 200
        
    if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
        # Create a placeholder file if the sample.jpg doesn't exist
        if filename == 'sample.jpg' and not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], 'sample.jpg')):
            with open(os.path.join(app.config['UPLOAD_FOLDER'], 'sample.jpg'), 'w') as f:
                f.write('placeholder')
    
    return send_from_directory('uploads', filename)

@app.route('/api/v1/csrf-token', methods=['GET', 'OPTIONS'])
def get_csrf():
    logger.debug(f"Received request: {request.method} to /api/v1/csrf-token")
    
    if request.method == 'OPTIONS':
        return make_response(), 200
        
    return jsonify({'csrf_token': 'dummy-token'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
