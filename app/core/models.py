from django.db import models
# Below this we are going to import the abstact base user, base user manager and permission mixin.
# These are required to extent the user model.
from django.contrib.auth.models import AbstractBaseuser, BaseUserManager \
                                    PermissionMixin
# Now we import the user manager class
# Is the class that provides the helper functions for creating a user or creating a super user.
class UserManager(BaseUserManager)
    # The last parameter says take any of the extra parameter passed in. It adds more flexibility.
    def create_user(self, email, password=None, **extra_fields):
        """ Creates and saves a new user """
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.
