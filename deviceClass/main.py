#!/bin/env python
import device

# Add API Credentials
apiCredentials = {
    'company': 'lmkendallshearman',
    'accessid': 'uSzNM8LS94XIy3R47dTy',
    'accesskey': 'lma__%{D8{^)6~C75t6mt63R-_=63~R24Khx_Gqve]CR7qebc^~)^zy7]w3fuw^ILZjgzODM1M2ItNTcxMS00YzFjLTgwYjYtMWU5NTVkNjU1OTE1L049l8h'
}

#Device Data Payload
deviceDict = ''

d1 = device.Device(apiCredentials)
#response = w1.add(apiCredentials,websiteDict)
response = d1.get(apiCredentials)


print(response.status_code)
print(response.content)