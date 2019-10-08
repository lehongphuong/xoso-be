# https://devcenter.heroku.com/articles/clock-processes-python

import datetime
from scrapinghub import ScrapinghubClient
import logging 

from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler() 
 
@sched.scheduled_job(trigger='interval', minute='1')
def jobRuning00():
    # Enter ScrapingHub
    # Enter ScrapingHub
    apikey = '40f9881d52794d7bb09b9f5ee6d12a3e'  # your API key as a string
    client = ScrapinghubClient(apikey)
    projectID = 410647
    project = client.get_project(projectID)

    # get spider
    spiderID = 'quotes'
    spider = project.spiders.get(spiderID) 
    spider.jobs.run()  
 

sched.start()
  