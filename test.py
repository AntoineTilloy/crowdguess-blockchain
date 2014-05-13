import httplib,urllib
import json
   
HOSTNAME = 'blockchain.info'
url='/merchant/5ea4b688-da07-4d3b-8fe8-90baf14df521/'

method='balance?'
#method='new_address?'

values={
	'password' :'',
	'label' : 'second test address'
}

headers = {
	'User-Agent': 'python',
	'Content-Type': 'application/x-www-form-urlencoded',
}

values = urllib.urlencode(values)
conn = httplib.HTTPSConnection(HOSTNAME)
conn.request('POST',url+method,values,headers)
response = conn.getresponse()
response=response.read()
response=json.loads(response)
print response['balance']