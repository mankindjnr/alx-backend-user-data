#!/usr/bin/env python3
import re
import logging
from typing import List
"""regex to replace a specific word in a string"""

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    return re.sub(r'{}(?={})'.format('|'.join(fields), re.escape(separator)), redaction, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str] = None):
        """init method"""
        self.fields = list(fields)
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """format method"""
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
