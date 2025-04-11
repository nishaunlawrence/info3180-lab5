import os
from app import app, db
from app.models import Movie

# Create the directory for migration files if it doesn't exist
if not os.path.exists('migrations'):
    os.system('flask db init')

# Create a migration
os.system('flask db migrate -m "Initial migration"')

# Apply the migration
os.system('flask db upgrade')

print("Database initialized successfully.")
