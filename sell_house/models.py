from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=CASCADE)
    name=CharField(max_length=50)
    email=CharField(max_length=50)
    phone=CharField(max_length=50)

    def __str__(self) -> str:
        return self.name




class House(models.Model):
    name=CharField(max_length=20)
    area=CharField(max_length=50)
    photo=CharField(max_length=1000)


    def __str__(self):
        return self.name


class Post(models.Model):
    caption=CharField(max_length=200,null=True)
    User=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    House = models.ForeignKey(House, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.caption
