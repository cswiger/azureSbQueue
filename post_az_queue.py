#!/usr/local/bin/python3
import urllib.request
import json
from urllib.parse import urljoin
from urllib.error import URLError
from urllib.error import HTTPError
import sys
import sas

# put your azure sb queue details here
sbNamespace = 'chucks'
sbEntityPath = 'chucks'
sharedAccessKey = b'sharedAccessKey'
sharedAccessKeyName = 'chucks'

environment = 'https://chucks.servicebus.Windows.net'
sessionUrl = urljoin(environment,'/chucks/messages')

reqBody = {'temp' : '' }
reqBody['temp'] = sys.argv[1]

data = json.dumps(reqBody).encode('utf-8')

headers = {}
headers['Content-type'] = "application/atom+xml;type=entry;charset=utf-8"
headers['Authorization'] = sas.sas(sbNamespace,sbEntityPath,sharedAccessKey,sharedAccessKeyName)
req = urllib.request.Request(sessionUrl, data, headers)
try:
   response = urllib.request.urlopen(req)
   print(response.status)
except HTTPError as httperror:
   print(httperror.reason)
except URLError as urlerror:
   print(urlerror.reason)


