import mysql.connector
import os
from dotenv import load_doenv

load_doenv

class Database:
    @staticmethod 
    def get_connetion():
        return mysql.onnector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )