import atexit

from utils.helper import ask_meal, ask_syrup, ask_medicine, store_data
from utils.logger import get_logger

from apscheduler.schedulers.background import BackgroundScheduler

error_logger = get_logger('error_logger')

if __name__ == '__main__':

    try:
        scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
        
        # Schedule jobs
        scheduler.add_job(func=ask_meal, args=['breakfast'], trigger='cron', hour='12')
        scheduler.add_job(func=ask_meal, args=['lunch'], trigger='cron', hour='16')
        scheduler.add_job(func=ask_meal, args=['dinner'], trigger='cron', hour='22')

        scheduler.add_job(func=ask_syrup, args=['syrup_1'], trigger='cron', hour='17', minute='5')
        scheduler.add_job(func=ask_syrup, args=['syrup_2'], trigger='cron', hour='22', minute='5')

        scheduler.add_job(func=ask_medicine, args=['Iron'], trigger='cron', hour='14')
        scheduler.add_job(func=ask_medicine, args=['Vitamin D'], trigger='cron', hour='22', minute='10')

        scheduler.add_job(func=ask_medicine, args=['treatment'], trigger='cron', hour='12', minute='15')

        scheduler.add_job(func=store_data, trigger='cron', hour='22', minute='45')


        scheduler.start()
        scheduler.print_jobs()

        atexit.register(lambda: scheduler.shutdown())
    except Exception as e:
        error_logger.exception(f'Exception occured while running med check!!!')