from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from scheduled_job import job, mailing, birthday, due_date

def start():
    scheduler = BackgroundScheduler(timezone='Asia/Tashkent')
    scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
    register_events(scheduler)
    scheduler.add_job(job.alert_clients, 'cron', hour=8, minute=0, second=0)
    scheduler.add_job(birthday.send_congragulation, 'cron', hour=9, minute=21, second=21)
    scheduler.add_job(mailing.send_message, 'interval', minutes=7)
    scheduler.add_job(job.refresh_ytt_sub_gived, 'cron', day=1)
    scheduler.add_job(due_date.check_expires, 'cron', day=1)
    scheduler.start()