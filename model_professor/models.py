from django.db import models

class Professor(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=300)
    subject = models.CharField(max_length=100)
    rating = models.FloatField()
    experience = models.IntegerField()

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField()
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
