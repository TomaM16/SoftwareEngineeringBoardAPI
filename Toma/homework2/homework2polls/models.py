from django.db import models

class Car(models.Model):
    color = models.CharField(max_length=100)
    made = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=50)
    description = models.TextField()

class Board(models.Model):
    carrier = models.CharField(max_length=40)
    time = models.CharField(max_length=20)
    destination = models.CharField(max_length=50)
    train = models.IntegerField()
    status = models.CharField(max_length=20)