import os

basedir = os.path.abspath(os.path.dirname(__file__))
UPLOADED_IMAGES_DEST = os.path.join(basedir, "app", "static", "uploads")

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secret_of_super_keys")
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
