from django.db import models

# Create your models here.
class Login(models.Model):
    image = models.ImageField(upload_to='login/',null=False)