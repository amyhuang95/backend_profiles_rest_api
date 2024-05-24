"""
This module contains database models for the 'profiles_api' application. 
"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """
    Customized manager for user profiles.
    """

    def create_user(self, email, name, password=None):
        """
        Create a new user profile.
        """
        if not email:
            raise ValueError('User must have an email address.')

        # normalize the second half of the email address
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)  # encrypt password
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """
        Create and save a new superuser with given details.
        """
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Customized model for users in the system. User will use their email address
    for authentication instead of using username. 

    Attributes:
        email (str): The email of the user.
        name (str): The name of the user.
        is_active (boolean): Whether the user is active. Default is active. 
        is_staff (boolean): Whether the user is a staff. Default is not a staff.
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'  # change the default authentication field to email
    # user also needs to provide their name for authentication
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        Retrieve full name of user.
        """
        return self.name

    def get_short_name(self):
        """
        Retrieve short name of user.
        """
        return self.name

    def __str__(self):
        """
        Return string representation of user.
        """
        return f'{self.name}: {self.email}'
