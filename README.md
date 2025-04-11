# INFO3180 Lab 5 - VueJS and Flask API

This project integrates a VueJS frontend with a Flask backend API, allowing users to add their favorite movies to a database and display them on a page.

## Setup Instructions

### Prerequisites
- Python 3.8 or later
- Node.js and npm
- SQLite (included in the project, no separate installation needed)

### Initial Setup

1. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

2. **Install Python dependencies**:
   ```bash
   pip install flask flask-sqlalchemy flask-migrate flask-wtf python-dotenv werkzeug
   ```

3. **Install Node.js dependencies**:
   ```bash
   npm install
   ```

4. **Initialize the database**:
   ```bash
   python initialize_db.py
   ```

### Running the Application

1. **Start the Flask backend server**:
   ```bash
   flask --app app --debug run
   ```

2. **In a separate terminal, start the VueJS development server**:
   ```bash
   npm run dev
   ```

3. **Access the application**:
   - Open your browser and go to `http://localhost:5173/movies/create` to add movies
   - Go to `http://localhost:5173/movies` to view your movies

## Project Structure

- `app/forms.py` - Contains the MovieForm class for form validation
- `app/models.py` - Contains the Movie database model
- `app/views.py` - Contains Flask routes including the API endpoints
- `src/components/MovieForm.vue` - VueJS component for the movie form
- `src/views/AddMovieFormView.vue` - VueJS page that displays the movie form
- `src/views/MoviesView.vue` - VueJS page that displays the list of movies

## API Endpoints

- `GET /api/v1/csrf-token` - Get a CSRF token for form submission
- `POST /api/v1/movies` - Add a new movie
- `GET /api/v1/movies` - Get all movies
- `GET /api/v1/posters/<filename>` - Get a movie poster

## Troubleshooting

- If you encounter database errors, ensure the `movies.db` file is created in the app directory
- If you get CSRF errors, ensure you're fetching and using the CSRF token in your form submission
- Check browser console for any JavaScript errors
- Check terminal for any Flask backend errors
