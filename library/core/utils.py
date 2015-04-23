import re
import json
from unicodedata import normalize
from datetime import datetime, date
from email.utils import formatdate
# from calendar import timegm
# from user_agents import parse
import requests
import os
import string
import random
import inspect


def to_dict(obj):
    """
    Converts a given object to a dictionary

    :param obj: The obj to be converted

    :returns: items
    :rtype: dict

    """

    items = vars(obj)
    # items = obj_dict.items()

    return items