from apscheduler.schedulers.background import BackgroundScheduler
import requests
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)

def start():
    try:
        scheduler = BackgroundScheduler()
        scheduler.add_job(send_request, 'interval', minutes=2880)
        scheduler.start()
        logger.info('Scheduler started successfully!')
    except Exception as e:
        logger.error('Scheduler not started! Error: %s', e)

def send_request():
    try:
        response = requests.post('http://127.0.0.1:8000/scrap/')
        logger.info('API called successfully! Response: %s', response.json())
    except Exception as e:
        logger.error('Error while calling API! Error: %s', e)