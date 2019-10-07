from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# from .models import User
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
import requests
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse

from django.core import serializers

import json

# https://scrapy.org/ 

# from models import User
from . import models

from django.db import connection

from scrapinghub import ScrapinghubClient
import logging

import schedule
import time 

# from apscheduler.schedulers.blocking import BlockingScheduler
# sched = BlockingScheduler()

def index(request):
    return render(request, "index.html", {"users": 1})


# *********************************************
# begin common 

# convert cursor to json data
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


# execute query sql with cursor
def executeQuery(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        data = dictfetchall(cursor)
    return data

def getDataXoso():
    # Enter ScrapingHub
    apikey = '40f9881d52794d7bb09b9f5ee6d12a3e'  # your API key as a string
    client = ScrapinghubClient(apikey)
    projectID = 410647
    project = client.get_project(projectID)

    # get spider
    spiderID = 'quotes'
    spider = project.spiders.get(spiderID)

    jobs_summary = spider.jobs.iter()
    job_keys = [j['key'] for j in jobs_summary]

    print(job_keys)
    for job_key in job_keys:
        job = project.jobs.get(job_key)

        # Check to see if the job was completed
        if job.metadata.get(u'close_reason') == u'finished':
            for item_aggelia in job.items.iter():
                return item_aggelia  

# @sched.scheduled_job('interval', minutes=1)
# def jobRuning():
#     # Enter ScrapingHub
#     # Enter ScrapingHub
#     apikey = '40f9881d52794d7bb09b9f5ee6d12a3e'  # your API key as a string
#     client = ScrapinghubClient(apikey)
#     projectID = 410647
#     project = client.get_project(projectID)

#     # get spider
#     spiderID = 'quotes'
#     spider = project.spiders.get(spiderID) 
#     spider.jobs.run() 

# def jobSchedule():
#     schedule.every(1).minutes.do(jobRuning)

#     while True:
#         schedule.run_pending()
#         time.sleep(1)


# sched.start()
 
# end common
# *********************************************


# *********************************************
# begin Company
@api_view(['POST'])
@parser_classes((JSONParser,))
# get all data from xoso
def readDataXoSo(request, format=None): 
    print(getDataXoso())
    data = getDataXoso()

    return Response([{"result": data}])

@api_view(['POST'])
@parser_classes((JSONParser,))
def startJob(request, format=None): 
    jobSchedule()

    return Response([{"result": "ok"}])

# *********************************************
# end Company


# *********************************************
# begin Company
@api_view(['POST'])
@parser_classes((JSONParser,))
# get all data from Company
def createDataCompany(request, format=None):
    data = json.loads(json.dumps(request.data))
    obj = models.Company(**data)
    obj.save()
    return Response([{"id": obj.id, "result": "ok"}])


@api_view(['POST'])
@parser_classes((JSONParser,))
# get all data from Company
def readDataCompany(request, format=None):
    return Response(serializers.serialize("json", models.Company.objects.all()))


@api_view(['POST'])
@parser_classes((JSONParser,))
# get update data from Company
def updateDataCompany(request, format=None):
    data = json.loads(json.dumps(request.data))
    models.Company(**data).save()
    return Response({"result": "ok"})


@api_view(['POST'])
@parser_classes((JSONParser,))
# get delete data from Company
def deleteDataCompany(request, format=None):
    data = json.loads(json.dumps(request.data))
    models.Company(**data).delete()
    return Response({"result": "ok"})


@api_view(['POST'])
@parser_classes((JSONParser,))
# get delete data from Company
def findDataCompany(request, format=None):
    return Response(serializers.serialize("json", models.Company.objects.filter(pk=request.data['pk'])))


@api_view(['POST'])
@parser_classes((JSONParser,))
# get data acengy of company
def searchDataAgencyOfCompany(request, format=None):
    return Response(serializers.serialize("json", models.Company.objects.filter(idParent=request.data['company'])))


# end Company
# ********************************************* 