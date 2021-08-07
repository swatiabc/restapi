from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User',related_name='article',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
