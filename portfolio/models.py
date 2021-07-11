from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    git = models.CharField(max_length=100)
    demo = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    introduction = models.TextField()
    def __str__(self):
        return self.title