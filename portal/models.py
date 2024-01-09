from django.db import models


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.title} The Event'


class Registration(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}  The Registration'
