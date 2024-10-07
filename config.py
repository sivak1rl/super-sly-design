import os

basedir = os.path.abspath(os.path.dirname(__file__))
UPLOADED_IMAGES_DEST = os.path.join(basedir, "app", "static", "uploads")

class Config:
    SECRET_KEY = "secret_of_super_keys"
    SQLALCHEMY_DATABASE_URI = "app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_IMAGES_DEST = UPLOADED_IMAGES_DEST
