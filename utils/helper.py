import logging
from datetime import datetime

from utils.telegram import send_message, get_updates
from utils.db import SqliteConnection
from utils.telegram import send_daily_report_message, send_sticker
from utils.logger import get_logger


error_logger = get_logger('error_logger', logging.ERROR)
info_logger = get_logger('info_logger', logging.INFO)


def get_update_query(table, id, key, value):
    query= f"""
        UPDATE {table}
        SET
        {key} = {value}
        WHERE id = {id}
    """
    return query

def ask_meal(meal_type):
    try:
        message_id = send_message(f'Have you eaten {meal_type}?')
        if message_id:
            query = get_update_query('message_ids', 1, meal_type, message_id)
            sqlite_client = SqliteConnection()
            sqlite_client.update_record(query)
    except Exception as e:
        error_logger.exception(f'Exception occured while running ask_meal!!!')
   
def ask_syrup(syrup_number):
    try:
        message_id = send_message(f'Have you drank the syrup?')
        if message_id:
            query = get_update_query('message_ids', 1, syrup_number, message_id)
            sqlite_client = SqliteConnection()
            sqlite_client.update_record(query)
    except Exception as e:
        error_logger.exception(f'Exception occured while running ask_syrup!!!')
    
def ask_medicine(tablet):
    try:
        message_id = send_message(f'Have you eaten your {tablet} tablets?')
        if message_id:
            query = get_update_query('message_ids', 1, tablet, message_id)
            sqlite_client = SqliteConnection()
            sqlite_client.update_record(query)
    except Exception as e:
        error_logger.exception(f'Exception occured while running ask_medicine!!!')
    
def get_last_offset():
    try:
        query = 'SELECT offset FROM offset WHERE id = 1'
        sqlite_client = SqliteConnection()
        results = sqlite_client.get_records(query)
        for item in results:
            return item[0]
    except Exception as e:
        error_logger.exception(f'Exception occured while running get_last_offset!!!')

def update_last_offset(offset):
    try:
        query = f'UPDATE offset SET offset = {str(offset)}'
        sqlite_client = SqliteConnection()
        results = sqlite_client.update_record(query)
    except Exception as e:
        error_logger.exception(f'Exception occured while running get_last_offset!!!')


def get_message_ids():
    try:
        values = ('breakfast', 'lunch', 'dinner', 'syrup_1', 'syrup_2', 'iron', 'vitamin', 'regular')
        query = 'SELECT * FROM message_ids WHERE id = 1'
        sqlite_client = SqliteConnection()
        results = sqlite_client.get_records(query)
        keys = results[0][1:]
        message_id_mapping = dict(zip(keys, values))
        return message_id_mapping
    except Exception as e:
        error_logger.exception(f'Exception occured while running get_message_ids!!!')


def send_analysis_data(data):
    try:
        message = ''
        for k, v in data.items():
            message = message + k.title() + ': ' + v.title() + '\n'
        send_daily_report_message(message)
    except Exception as e:
        error_logger.exception(f'Exception occured while running send_analysis_data!!!')

def store_data():
    try:
        keys = ['breakfast', 'lunch', 'dinner', 'syrup_1', 'syrup_2', 'iron', 'vitamin', 'regular']
        data = {}
        offset = get_last_offset()
        last_offset = None
        info_logger.info(offset)
        results = get_updates(offset)
        info_logger.info(results)
        message_id_mapping = get_message_ids()
        info_logger.info(message_id_mapping)

        for item in results:
            message_details = item.get('message')
            last_offset = item.get('update_id', offset)
            if message_details:
                text = message_details.get('text', 'Unknown')
                source_message_details = message_details.get('reply_to_message')
                if source_message_details:
                    source_message_id = str(source_message_details['message_id'])
                    if source_message_id in message_id_mapping:
                        data[message_id_mapping[source_message_id]] = text
        ordered_data = []
        for key in keys:
            ordered_data.append(data.get(key, 'Unknown'))
        ordered_data.append(str(datetime.now().date()))
        ordered_data = tuple(ordered_data)
        query = f"INSERT INTO records VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        sqlite_client = SqliteConnection()
        sqlite_client.insert_record(query, ordered_data)
        send_analysis_data(data)
        update_last_offset(last_offset)
        send_sticker()
        info_logger.info(last_offset)
    except Exception as e:
        error_logger.exception(f'Exception occured while running store_data!!!')

