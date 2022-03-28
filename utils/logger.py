import os
import logging

loggers = {}

def get_logger(logger_name, logging_level):
    try:
        global loggers

        if loggers.get(logger_name):
            return loggers.get(logger_name)
        else:
            logger = logging.getLogger('bot_logger')
            
            if logging_level == logging.INFO:
                file_handler = logging.FileHandler(os.environ.get('LOG_PATH', 'info.log'))
            else:
                file_handler = logging.FileHandler(os.environ.get('LOG_PATH', 'error.log'))

            file_handler.setLevel(logging_level)

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            loggers[logger_name] = logger
            return logger

    except Exception as e:
        print(e)
