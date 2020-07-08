import json
import os

import json


def parse():
    with open('/Users/simonthomas/formtest/django_forms/myapp/static/my_config.json') as f:
        data = json.loads(f.read())

    return data



