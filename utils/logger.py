import logging

loggers = {}

def get_logger(logger_name):
    try:
        global loggers

        if loggers.get(logger_name):
            return loggers.get(logger_name)
        else:
            logger = logging.getLogger('bot_logger')

            file_handler = logging.FileHandler('error.log')
            file_handler.setLevel(logging.ERROR)

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            loggers[logger_name] = logger
            return logger

    except Exception as e:
        print(e)
