from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BlogPost(db.Model):
    __tablename__ = 'blog_posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.now())
    excerpt = db.Column(db.String(300), nullable=False)
    url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<BlogPost {self.title}>"
