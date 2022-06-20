from apscheduler.schedulers.background import BackgroundScheduler
from scheduled_job import job, mailing, birthday

def start():
    scheduler = BackgroundScheduler(timezone='Asia/Tashkent')
    scheduler.add_job(job.alert_clients, 'cron', hour=11, minute=44, second=1)
    scheduler.add_job(birthday.send_congragulation, 'cron', hour=11, minute=44, second=21)
    scheduler.add_job(mailing.send_message, 'interval', minutes=7)
    scheduler.start()