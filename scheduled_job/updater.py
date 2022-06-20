from apscheduler.schedulers.background import BackgroundScheduler
from scheduled_job import job, mailing, birthday

def start():
    scheduler = BackgroundScheduler(timezone='Asia/Tashkent')
    scheduler.add_job(job.alert_clients, 'cron', hour=12, minute=15, second=1)
    scheduler.add_job(birthday.send_congragulation, 'cron', hour=12, minute=15, second=21)
    scheduler.add_job(mailing.send_message, 'interval', minutes=7)
    scheduler.start()