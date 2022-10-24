#!/bin/env python
import requests
import hashlib
import base64
import hmac
import time


def makerequest(apicredentials: dict, resourcepath: str, queryparams: str = '', httpverb: str = '', data: str = ''):

    # Get current time in milliseconds
    epoch = str(int(time.time() * 1000))
    # Construct URL
    url = f'https://{apicredentials["company"]}.logicmonitor.com/santaba/rest{resourcepath}{queryparams}'
    # Cat Request details
    requestvars = httpverb + epoch + data + resourcepath
    # Construct Signature
    signature = base64.b64encode((hmac.new(apicredentials["accesskey"].encode(), msg=requestvars.encode(),
                                           digestmod=hashlib.sha256).hexdigest()).encode())
    # Constuct Headers
    auth = f'LMv1 {apicredentials["accessid"]}:{signature.decode()}:{epoch}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth, 'X-Version': '3'
    }
    # Make Request
    if httpverb == 'GET':
        response = requests.get(url, data=data, headers=headers)
    elif httpverb == 'PUT':
        response = requests.put(url, data=data, headers=headers)
    elif httpverb == 'PATCH':
        response = requests.patch(url, data=data, headers=headers)
    elif httpverb == 'POST':
        response = requests.post(url, data=data, headers=headers)
    elif httpverb == 'DELETE':
        response = requests.delete(url, data=data, headers=headers)
    else:
        print(f'ERROR: Invalid httpverb: {httpverb}')

    if response.status_code == requests.codes.OK:
        return response
    else:
        response.raise_for_status()