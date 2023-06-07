from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Candidate(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    image = models.ImageField()
    num_of_votes = models.IntegerField()

    def __str__(self):
        return self.name
