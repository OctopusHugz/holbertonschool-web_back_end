#!/usr/bin/env python3
""" This module creates a filter_datum function """
from typing import List, Tuple
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

    def __init__(self, fields: Tuple) -> None:
        """ Creates an instance of RedactingFormatter class """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """ Formats the record into specified self.FORMAT """
        record.asctime = self.formatTime(record)
        record.message = filter_datum(self.fields, self.REDACTION,
                                      record.getMessage(), self.SEPARATOR)
        return self.formatMessage(record)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Returns the log message obfuscated """
    return [message := re.sub(f"(?<={field}=).*?(?={separator})", redaction,
                              message) for field in fields][-1]


def get_logger() -> logging.Logger:
    """ Returns a Logger object """
    new_logger = logging.getLogger("user_data")
    new_logger.setLevel(logging.INFO)
    new_logger.propagate = False
    new_logger.addHandler(logging.StreamHandler(RedactingFormatter))
    return new_logger


def get_db() -> mysql.connector.connect:
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
