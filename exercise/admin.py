from django.contrib import admin

# Register your models here.
from exercise.models import Exercise, JoinExercise

admin.site.register(Exercise)
admin.site.register(JoinExercise)