from apscheduler.schedulers.blocking import BlockingScheduler
from dataETL import etl

sched = BlockingScheduler()
sched.add_job(etl, 'cron', day_of_week='mon-sun', hour=1)

sched.start()
