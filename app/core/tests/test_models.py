# We are going to use create user function to crate a user
# Then verify that user has been created.
from django.test import TestCase
# you can import the user model directly but importing this way
# helps in changing the user model dynamic way. You can change all by chaning one.
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """ Test crating a new user with an email is successful """
        # Getting username and password we are verify the account exists.
        email = 'test@londonappdev.com'
        password = 'Testpass123'
        # This is calling the create user function on the user manager from the user model.
        user = get_user_model().objects.create_user(
        email = email,
        password = password
        )
        # making sure that the user was created correctly.
        self.assertEqual(user.email,email)
        #Since the password is encripted.We can't check the password in the same way as this.
        self.assertTrue(user.check_password(password))
