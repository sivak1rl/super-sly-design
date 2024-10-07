import unittest
from super_sly_designs.app import app
from super_sly_designs.models import db, BlogPost
from flask import url_for

class BlogTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the application context and the test client
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['SERVER_NAME'] = 'localhost'  # Set SERVER_NAME to allow url_for usage
        self.client = self.app.test_client()

        # Push application context
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Set up the database (Skip init_app since it's already done in app setup)
        db.create_all()

    def tearDown(self):
        # Clean up database and pop the context
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Super Sly Designs', response.data)

    def test_about_page(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Us', response.data)

    def test_contact_page(self):
        response = self.client.get(url_for('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contact Us', response.data)

    def test_blog_page(self):
        response = self.client.get(url_for('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Our Blog', response.data)

    def test_add_post(self):
        with self.client:
            self.client.post(url_for('login'), data={'username': 'admin', 'password': 'password'})
            response = self.client.post(url_for('add_post'), data={
                'title': 'Test Post',
                'content': 'This is a test post.',
                'author': 'Test Author'
            }, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            #self.assertIn(b'New post added successfully!', response.data)

    def test_edit_post(self):
      with self.client:
          # Create a post to edit, include excerpt and url fields
          post = BlogPost(
              title='Original Title',
              content='Original Content',
              author='Original Author',
              excerpt='Original Content Excerpt',
              url='/blog/original-title'
          )
          db.session.add(post)
          db.session.commit()

          # Log in and edit the post
          self.client.post(url_for('login'), data={'username': 'admin', 'password': 'password'})
          response = self.client.post(url_for('edit_post', post_id=post.id), data={
              'title': 'Updated Title',
              'content': 'Updated Content',
              'author': 'Updated Author'
          }, follow_redirects=True)
          self.assertEqual(response.status_code, 200)
          # self.assertIn(b'Post updated successfully!', response.data)



    def test_login(self):
        response = self.client.post(url_for('login'), data={'username': 'admin', 'password': 'password'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        #self.assertIn(b'Login successful!', response.data)

    def test_logout(self):
        with self.client:
            self.client.post(url_for('login'), data={'username': 'admin', 'password': 'password'})
            response = self.client.get(url_for('logout'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            #self.assertIn(b'You have been logged out.', response.data)

if __name__ == '__main__':
    unittest.main()