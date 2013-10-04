import urllib2
from BeautifulSoup import *
mdn = raw_input("Enter Your Reliance MDN!!")
request  = urllib2.Request("http://www.rcom.co.in/rcom/Netconnect/Netconnect_Authentication.jsp?MDN=+"mdn)
try:
	response = urllib2.urlopen(request)
	soup = BeautifulSoup(response)
 	#soup.tag gives the content of that tag:) I want the content from td p which is strong
	message = soup.td.p.strong
	# message = message.string # conver to string 
	message = str (message)
	print message
	cut = message.split("RCONNECT Bal is ",1)
	cutdata = cut[1]
	balance = cutdata[:cutdata.index(",")]
	print "Your balance is",balance
	print "Happy Browsing:)"
	#print message
except urllib2.URLError:
	print "Unable to connect to the site"
	print "Check your internet connection"
