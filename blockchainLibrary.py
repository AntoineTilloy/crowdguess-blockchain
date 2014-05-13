import httplib,urllib
import json

def sendAPIRequest(guid,password,method,label="not specified",address="not specified",amount=0,confirmations=0):
	HOSTNAME = 'blockchain.info'
	url='/merchant/'+guid+'/'
	values={
		'password' :password,
		'label' : label,
		'address':address,
		'amount':amount,
		'note':'sent from crowdguess',
		'confirmations':confirmations,
	}
	headers = {
		'User-Agent': 'python',
		'Content-Type': 'application/x-www-form-urlencoded',
	}

	values = urllib.urlencode(values)
	try:
		conn = httplib.HTTPSConnection(HOSTNAME)
		conn.request('POST',url+method+"?",values,headers)
		response = conn.getresponse()
		response = response.read()
		response=json.loads(response)
	except:
		print "https connection error"
		response=None

	return response

class Wallet:

	def __init__(self,guid,password):
		self.guid=guid
		self.password=password

	def sendPayment(self,address,amount):
		status=sendAPIRequest(self.guid,self.password,"payment",address=address,amount=amount)
		return status
	def createAddress(self,name):
		response=sendAPIRequest(self.guid,self.password,"new_address",label=name)
		return response
	def getBalance(self):
		response=sendAPIRequest(self.guid,self.password,"balance")
		return response
	def listAddress(self,confirmations=0):
		response=sendAPIRequest(self.guid,self.password,"list",confirmations)
		return response
