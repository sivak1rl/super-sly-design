import os
from flask_migrate import Migrate
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Create the instance directory if it doesn't exist
instance_path = os.path.join(app.config["BASE_DIR"], "instance")
if not os.path.exists(instance_path):
    os.makedirs(instance_path)

# Initialize database and migration
from .models import db

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    # Create the database tables if they do not exist
    db.create_all()

from . import routes, models
