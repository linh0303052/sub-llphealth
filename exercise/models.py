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
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_query_name='joinexercise')
    percentage = models.FloatField(default=0)
    completed = models.BooleanField(default=False)
    last_join = models.DateField(auto_now=True)
    def toObject(self):
        return {'title': self.exercise.title , 'kind': self.exercise.get_kind_display(), 'description': self.exercise.description, 
        'percentage': self.percentage, 'difficulty': self.exercise.difficulty}