from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import User


class Moderator(User):

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Moderator, self).save()
