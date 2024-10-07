from super_sly_designs.app import app
from .models import BlogPost, db
from flask import render_template, send_from_directory, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

# Mock user data (replace with proper user model/database integration)
users = {
    "admin": {
        "username": "admin",
        "password": generate_password_hash("password")  # Hash of 'password'
    }
}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            flash("You need to be logged in to access this page.", "danger")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

@app.errorhandler(404)
@app.route('/404')
def page_not_found(error):
  print(error)
  return render_template('404.html', title='404 Not Found!')

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')

@app.route('/blog')
def blog():
    # Fetch all blog posts from the database
    posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).all()
    return render_template('blog.html', title="Blog", posts=posts)

@app.route('/add-post', methods=['GET', 'POST'])
@login_required
def add_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author')
        if not title or not content or not author:
            flash('All fields are required!', 'danger')
        else:
            new_post = BlogPost(title=title, content=content, author=author, excerpt=content[:150], url='#')
            db.session.add(new_post)
            db.session.commit()
            flash('New post added successfully!', 'success')
            return redirect(url_for('blog'))
    return render_template('add_post.html', title='Add New Post')

@app.route('/blog/<int:post_id>')
def view_post(post_id):
    # Fetch the post by ID
    post = BlogPost.query.get_or_404(post_id)
    return render_template('view_post.html', title=post.title, post=post)

@app.route('/blog/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.content = request.form.get('content')
        post.author = request.form.get('author')
        if not post.title or not post.content or not post.author:
            flash('All fields are required!', 'danger')
        else:
            db.session.commit()
            flash('Post updated successfully!', 'success')
            return redirect(url_for('view_post', post_id=post.id))
    return render_template('edit_post.html', title='Edit Post', post=post)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            session['user'] = user['username']
            flash('Login successful!', 'success')
            return redirect(url_for('blog'))
        flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html', title='Login')

@app.route('/logout')
@login_required
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'images/favicon.ico')