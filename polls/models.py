from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    category_name = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Candidate(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='static/images')
    num_of_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Vote(models.Model):
    voter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                              related_name="votes")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name="votes")

    def __str__(self):
        return f"{self.voter} - {self.category}"
