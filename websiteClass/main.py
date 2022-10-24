#!/bin/env python3

import website

# Add API Credentials
apiCredentials = {
    'company': 'lmkendallshearman',
    'accessid': 'uSzNM8LS94XIy3R47dTy',
    'accesskey': 'lma__%{D8{^)6~C75t6mt63R-_=63~R24Khx_Gqve]CR7qebc^~)^zy7]w3fuw^ILZjgzODM1M2ItNTcxMS00YzFjLTgwYjYtMWU5NTVkNjU1OTE1L049l8h'
}

#Website Data Payload
websiteDict = {"groupId":"4","pollingInterval":"5","useDefaultLocationSetting":True,"useDefaultAlertSetting":True,"isInternal":False,"type":"webcheck","name":"LastTest102322","description":"","schema":"http","domain":"logicmonitor.com","pageLoadAlertTimeInMS":"30000","transition":"1","globalSmAlertCond":"0","overallAlertLevel":"warn","individualAlertLevel":"warn","triggerSSLStatusAlert":False,"triggerSSLExpirationAlert":False,"ignoreSSL":True,"alertExpr":"","individualSmAlertEnable":False,"testLocation":{"all":True,"smgIds":[2,4,3,5,6]},"steps":[{"useDefaultRoot":True,"url":"","HTTPVersion":"1.1","HTTPMethod":"GET","followRedirection":True,"fullpageLoad":False,"requireAuth":False,"matchType":"plain","path":"","keyword":"","invertMatch":"false","statusCode":"","type":"config","HTTPBody":"","auth":{"type":"basic","domain":"","userName":"","password":""},"postDataEditType":"raw","HTTPHeaders":""}],"properties":[]}

w1 = website.Website(apiCredentials)
#response = w1.add(apiCredentials,websiteDict)
response = w1.get(apiCredentials)
#response = w1.delete(apiCredentials, 32)
#response = w1.patch(apiCredentials, 26, {"name":"LM_Test_0925"})
#response = w1.put(apiCredentials, 31, websiteDict)

print(response.status_code)
print(response.content)