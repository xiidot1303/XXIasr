from apscheduler.schedulers.background import BackgroundScheduler
from scheduled_job import job

def start():
    scheduler = BackgroundScheduler(timezone='Asia/Tashkent')
    scheduler.add_job(job.alert_clients, 'cron', hour=5, minute=13, second=1)
    # scheduler.add_job(job.alert_clients, 'interval', minutes=0.1)
    scheduler.start()