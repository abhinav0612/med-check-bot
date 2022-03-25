import utils.constants as Constants

import requests

from utils.logger import get_logger

error_logger = get_logger('error_logger')


def send_message(message):
    try:
        url = '/'.join([Constants.BASE_URL, Constants.API_TOKEN, 'sendMessage'])
        headers = {'Content-Type': 'application/json'}
        payload = {
            "chat_id": Constants.CHAT_ID,
            "text": message,
            "reply_markup": {
                "keyboard": [
                    [
                        {
                            "text": "Yes"
                        },
                        {
                            "text": "No"
                        }
                    ]
                ],
                "one_time_keyboard": True
            }
        }

        resp = requests.post(url=url, headers=headers, json=payload)
        if resp.status_code == 200:
            return resp.json()['result']['message_id']
        else:
            error_logger.error(f'Error occured while running send_message!!!')
            return None
    except Exception as e:
        error_logger.exception(f'Exception occured while running send_message!!!')


def send_daily_report_message(message):
    try:
        url = '/'.join([Constants.BASE_URL, Constants.API_TOKEN, 'sendMessage'])
        headers = {'Content-Type': 'application/json'}
        payload = {
            "chat_id": Constants.CHAT_ID,
            "text": message
        }

        resp = requests.post(url=url, headers=headers, json=payload)
        if resp.status_code == 200:
            return resp.json()['result']['message_id']
        else:
            error_logger.error(f'Error occured while running send_daily_report_message!!!')
            # TODO
            return None
    except Exception as e:
        error_logger.exception(f'Exception occured while running send_daily_report_message!!!')



def get_updates(offset):
    try:
        url = '/'.join([Constants.BASE_URL, Constants.API_TOKEN, 'sendMessage'])
        headers = {'Content-Type': 'application/json'}
        payload = {
            "offset": offset
        }

        resp = requests.post(url=url, headers=headers, json=payload)
        if resp.status_code == 200:
            return resp.json()['result']
        else:
            error_logger.error(f'Error occured while running get_updates!!!')
            # TODO
            return None
    except Exception as e:
        error_logger.exception(f'Exception occured while running get_updates!!!')
