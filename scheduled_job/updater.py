from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from scheduled_job import job, mailing, birthday

def start():
    scheduler = BackgroundScheduler(timezone='Asia/Tashkent')
    scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
    register_events(scheduler)
    scheduler.add_job(job.alert_clients, 'cron', hour=8, minute=0, second=0)
    scheduler.add_job(birthday.send_congragulation, 'cron', hour=9, minute=21, second=21)
    scheduler.add_job(mailing.send_message, 'interval', minutes=7)
    scheduler.start()