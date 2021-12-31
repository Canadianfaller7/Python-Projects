from django.db import models

# Create your models here.
class djangoClasse(models.Model):
    title = models.CharField(max_length=200, default="", blank=True, null=False)
    courseNumber = models.IntegerField()
    instructor = models.CharField(max_length=50, default="", blank=True, null=False)
    duration = models.FloatField()

    object = models.Manager()

    def __str__(self):
        return self.title
