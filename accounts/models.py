from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    voted_president = models.BooleanField(default=False)
    voted_vice_president = models.BooleanField(default=False)
    voted_secretary = models.BooleanField(default=False)
    voted_treasurer = models.BooleanField(default=False)
    voted_wocom = models.BooleanField(default=False)
