from django.db import models

# Create your models here.

class loginForm(models.Model):
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username  