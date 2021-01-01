from django.db import models
from account.models import Account
from datetime import date

# Create your models here.
class Exercise(models.Model):
    KIND_CHOICES = [
            ('G', 'General'),
            ('C', 'Cardio'),
            ('Y', 'Yoga'),
    ]
    title = models.CharField(max_length=128)
    kind = models.CharField(max_length=1, choices=KIND_CHOICES, default='G')
    description = models.CharField(max_length=1024)
    difficulty = models.IntegerField(default=3)

    def toObject(self):
        return {'title': self.title , 'kind': self.get_kind_display(), 'description': self.description, 'percentage': 0, 'difficulty': self.difficulty}


class JoinExercise(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateField()