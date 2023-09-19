from django.db import models


# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=1000)

    def __str__(self):
        return self.question
