# (C) Datadog, Inc. 2010-2016
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

import requests

def retrieve_json(url):
    r = requests.get(url)
    r.raise_for_status()
    return r.json()
