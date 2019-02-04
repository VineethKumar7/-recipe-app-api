from django.db import models
# Below this we are going to import the abstact base user, base user manager and permission mixin.
# These are required to extent the user model.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
# Now we import the user manager class
# Is the class that provides the helper functions for creating a user or creating a super user.
class UserManager(BaseUserManager):
    # The last parameter says take any of the extra parameter passed in. It adds more flexibility.
    def create_user(self, email, password=None, **extra_fields):
        """ Creates and saves a new user """
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
         # 'using=self._db' used for multiple database. And its good practice.
        user.save(using=self._db)
        return user

# Now we have the manager class. Now we are going to create our modelself.
class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model that supports using email instead of username"""
    # We build on the django bild in model.
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length= 255)
    # Is used for user active indicator
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default=False)
    # We are going to assign the user manager
    objects = UserManager()
    # We customize the username as Email address.
    
