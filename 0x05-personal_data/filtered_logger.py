#!/usr/bin/env python3
""" This module creates a filter_datum function """
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Returns the log message obfuscated """
    return re.sub(f"(?<={fields}=).*?(?={separator})", redaction, message)
