# -*- coding: utf-8 -*-
"""
Iotdashboard project
Django 1.10.1
Python 2.7.6

Author: Sahin MERSIN

Demo: http://iotdashboard.pythonanywhere.com
Source: https://github.com/electrocoder/iotdashboard

https://iothook.com/
http://mesebilisim.com

Licensed under the Apache License, Version 2.0 (the "License").
You may not use this file except in compliance with the License.
A copy of the License is located at

http://www.apache.org/licenses/
"""

import requests
import json
import time


headers = {'Content-type': 'application/json'}

# url = 'http://localhost:8000/api/v1/datas/'
url = 'http://iotdashboard.pythonanywhere.com/api/v1/datas/'


auth=('admin', 'Aa1234567890')

for i in range(100):
    data={
        'api_key':'4a463be3b35f452882199810e720ee3a401bb754',
        'value_1':i*10,
        }

    data_json = json.dumps(data)
    response = requests.post(url, data=data_json, headers=headers, auth=auth)
    print(response)
    print(response.json())
    time.sleep(5)
