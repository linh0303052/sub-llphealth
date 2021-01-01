from django.shortcuts import render
from .models import Exercise, JoinExercise
import json
from django.core import serializers
from django.http import HttpRequest, HttpResponse
from account.models import Account
import datetime, timedelta

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
        last_date = user[0].last_exercise

        if last_date != current_date:
            new_record = JoinExercise(user = user[0], date = current_date)
            new_record.save()
            if last_date = current_date - timedelta(days=1):
                user[0].no_consecutive_day += 1
            else:
                user[0].no_consecutive_day = 1
            last_date = current_date
            
        data['success'] = True
    else:
        data['message'] = 'method not supported'
    return HttpResponse(json.dumps(data), content_type='application/json')


def get_date(request, username):
    data = {'succes': False}
    if (request.method == 'GET'):
        user = Account.objects.filter(username = username)
        records = JoinExercise.objects.filter(user = user[0])
        dates = [record.date for record in records]
        data['dates'] = dates
        data['no_consecutive'] = user[0].no_consecutive_day
    else:
        data['message'] = 'method not supported'
    return HttpResponse(json.dumps(data), content_type='application/json')

