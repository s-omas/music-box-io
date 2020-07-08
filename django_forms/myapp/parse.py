import json
import os

import json


def parse():
    with open('/Users/simonthomas/music-box-io1/django_forms/myapp/static/schema/schema.json') as f:
        data = json.loads(f.read())

    return data



print(parse())
