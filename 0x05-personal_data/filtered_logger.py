#!/usr/bin/env python3
""" This module creates a filter_datum function """
from time import strftime
from typing import List
from datetime import date, datetime
import logging
import mysql.connector
import os
import re
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Creates an instance of RedactingFormatter class """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """ Formats the record into specified self.FORMAT """
        return filter_datum(
            self.fields, self.REDACTION, super().format(record),
            self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Returns the log message obfuscated """
    for field in fields:
        message = re.sub(
            f"(?<={field}=).*?(?={separator})", redaction, message)
    return message


def get_logger() -> logging.Logger:
    """ Returns a Logger object """
    new_logger = logging.getLogger("user_data")
    new_logger.setLevel(logging.INFO)
    new_logger.propagate = False
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    ch.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    new_logger.addHandler(ch)
    return new_logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Returns a connector to the holberton database """
    user_name = os.getenv("PERSONAL_DATA_DB_USERNAME")
    if not user_name:
        user_name = "root"
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD")
    if not password:
        password = ""
    host = os.getenv("PERSONAL_DATA_DB_HOST")
    if not host:
        host = "localhost"
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")
    cnx = mysql.connector.connect(
        user=user_name, password=password, host=host, database=db_name)
    return cnx


def main():
    """Obtain a database connection and retrieve all rows from users table"""
    formatter = RedactingFormatter(PII_FIELDS)
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    ud_logger = get_logger()
    for row_dict in cursor:
        log_message = ""
        for k, v in row_dict.items():
            if not isinstance(v, datetime):
                kv_string = k + "=" + v + ";"
            else:
                kv_string = k + "=" + v.strftime("%Y-%m-%d %H:%M:%S") + ";"
            log_message += kv_string
        new_lr = logging.LogRecord(
            "user_data", logging.INFO, None, None, log_message, None, None)
        ud_logger.handle(new_lr)
        print(formatter.format(new_lr))
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
