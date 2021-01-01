from django.shortcuts import render
from .models import Exercise, JoinExercise
import json
from django.core import serializers
from django.http import HttpRequest, HttpResponse
from account.models import Account
import datetime
from datetime import timedelta

# Create your views her

def get_exercise(request, username):
    history = JoinExercise.objects.filter(completed=False)
    history_id = [i.exercise.id for i in history]
    new_exercises = Exercise.objects.exclude(id__in=history_id)

    data={'success':False}
    data['success']=True
    data['history'] = [i.toObject() for i in history]
    data['new_exercises'] = [i.toObject() for i in new_exercises]
    
    #data['all'] = [i.toObject() for i in all_exercise]
    #data['new_exercises'] = new_exercises
    return HttpResponse(json.dumps(data), content_type='application/json')


def update_exercise(request):
    data ={'success': False}
    if request.method == 'POST':
        username = request.POST['username']
        current_date = datetime.datetime.now()
        users = Account.objects.filter(username=username)
        if len(users) > 0:
            user = users[0]
            last_date = user.last_exercise
            if compare_date(last_date, current_date):
                new_record = JoinExercise(user = user, date = current_date)
                new_record.save()
                if compare_date(last_date, current_date - timedelta(days=1)):
                    user.no_consecutive_day += 1
                else:
                    user.no_consecutive_day = 1
                user.last_exercise = current_date
                user.save()
            
            data['success'] = True
    else:
        data['message'] = 'method not supported'
    return HttpResponse(json.dumps(data), content_type='application/json')


def get_date(request, username):
    data = {'succes': False}
    if (request.method == 'GET'):
        users = Account.objects.filter(username = username)
        user = users[0]
        records = JoinExercise.objects.filter(user = user).order_by('date')
        dates = [record.date.strftime('%Y-%m-%d') for record in records]
        data['dates'] = dates
        data['no_consecutive'] = user.no_consecutive_day
        data['succes'] = True
    else:
        data['message'] = 'method not supported'
    return HttpResponse(json.dumps(data), content_type='application/json')

def compare_date(date1, date2):
    return date1.day == date2.day and date1.month == date2.month and date1.year == date2.year