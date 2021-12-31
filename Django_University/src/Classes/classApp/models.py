from django.db import models

# Create your models here.
class djangoClasse(models.Model):
    # the blank is saying the site can have blank spaces, but the null is saying we can't
    # have blank stuff in the database
    title = models.CharField(max_length=200, default="", blank=True)
    courseNumber = models.IntegerField()
    instructor = models.CharField(max_length=50, default="", blank=True)
    duration = models.FloatField()

    object = models.Manager()

    def __str__(self):
        return self.title