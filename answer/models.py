from django.db import models
from django.conf import settings

class Question(models.Model):
    title = models.CharField(max_length=100)
    counter = models.FloatField()

    def __str__(self):
        return self.title
    
class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    