import os
import sqlite3

import constants as Constants

from logger import get_logger


error_logger = get_logger('error_logger')


class SqliteConnection:

    def __init__(self):
        self.path = Constants.DB_PATH
        self.connection = sqlite3.connect(self.path)
    
    def create_table(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.close()
        except Exception as e:
            error_logger.exception(f'Exception occured while running create_table!!!')
    def insert_record(self, query, values):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
        except Exception as e:
            error_logger.exception(f'Exception occured while running insert_record!!!')
    
    def update_record(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            error_logger.exception(f'Exception occured while running update_record!!!')
    
    def get_records(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            error_logger.exception(f'Exception occured while running get_records!!!')
    
    