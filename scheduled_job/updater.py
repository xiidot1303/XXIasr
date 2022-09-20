from apscheduler.schedulers.background import BackgroundScheduler
from scheduled_job import job, mailing, birthday

def start():
    scheduler = BackgroundScheduler(timezone='Asia/Tashkent')
    scheduler.add_job(job.alert_clients, 'cron', hour=5, minute=13, second=1)
    scheduler.add_job(birthday.send_congragulation, 'cron', hour=7, minute=21, second=21)
    scheduler.add_job(mailing.send_message, 'interval', minutes=0.07)
    scheduler.start()