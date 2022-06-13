from apscheduler.schedulers.background import BackgroundScheduler
from scheduled_job import job, mailing

def start():
    scheduler = BackgroundScheduler(timezone='Asia/Tashkent')
    scheduler.add_job(job.alert_clients, 'cron', hour=5, minute=13, second=1)
    scheduler.add_job(mailing.send_message, 'interval', minutes=5)
    scheduler.start()