#!/bin/env python
import makerequest
import json


class Website:
    def __init__(self, apicredentials:dict):
        self.company = apicredentials["company"]
        self.accesskey = apicredentials["accesskey"]
        self.accessid = apicredentials["accessid"]

    @classmethod
    def add(cls, apicredentials:dict, websitedict):
        # Request Info for Adding Website
        resourcepath = '/website/websites'
        # Convert Python Dict to JSON String.
        websiteData = json.dumps(websitedict)
        # Make request
        response = makerequest.makerequest(apicredentials, resourcepath, httpverb="POST", data=websiteData)
        return response

    @classmethod
    def get(cls, apicredentials: dict):
        resourcepath = '/website/websites'
        response = makerequest.makerequest(apicredentials, resourcepath, httpverb="GET", data='')
        return response

    @classmethod
    def delete(cls, apicredentials: dict, idnum: int):
        resourcepath = f'/website/websites/{idnum}'  # end of resource path is the id of website to be deleted
        response = makerequest.makerequest(apicredentials, resourcepath, httpverb="DELETE", data='')
        return response

    @classmethod
    def patch(cls, apicredentials: dict, idnum: int, prop: dict):
        resourcepath = f'/website/websites/{idnum}'  # end of resource path is the id of website to be patched
        stringDict = json.dumps(prop)
        response = makerequest.makerequest(apicredentials, resourcepath, httpverb="PATCH", data=stringDict)
        return response

    @classmethod
    def put(cls, apicredentials: dict, idnum: int, websitedata: dict):
        resourcepath = f'/website/websites/{idnum}'
        websiteData = json.dumps(websitedata)
        response = makerequest.makerequest(apicredentials, resourcepath, httpverb="PATCH", data=websiteData)
        return response






