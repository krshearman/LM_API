#!/bin/env python
import device

# Add API Credentials
apiCredentials = {
    'company': '',
    'accessid': '',
    'accesskey': ''
}

#Device Data Payload
deviceDict = ''

d1 = device.Device(apiCredentials)
#response = w1.add(apiCredentials,websiteDict)
response = d1.get(apiCredentials)


print(response.status_code)
print(response.content)