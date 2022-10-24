#!/bin/env python
import makerequest
import json


class Device:
    def __init__(self, apicredentials:dict):
        self.company = apicredentials["company"]
        self.accesskey = apicredentials["accesskey"]
        self.accessid = apicredentials["accessid"]

    @classmethod
    def add(cls, apicredentials: dict, devicedict):
        # Request Info for Adding Website
        resourcepath = '/device/devices'
        # Convert Python Dict to JSON String.
        deviceData = json.dumps(devicedict)
        # Make request
        response = makerequest.makerequest(apicredentials, resourcepath, httpverb="POST", data=deviceData)
        return response

    @classmethod
    def get(cls, apicredentials: dict):
        resourcepath = '/device/devices'
        response = makerequest.makerequest(apicredentials, resourcepath, httpverb="GET", data='')
        return response