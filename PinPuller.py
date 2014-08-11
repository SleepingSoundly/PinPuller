###############################################################
#				PinPuller 
#	-username
#	-pick board
#	-list pin discriptions
#
#	TODO?
# 		-randomly pick a pin (good for food)
# 		-orginize by color of something (good for clothes)
#		-orginize by date/season of pin (clothes)
#		-offer checklist? idk I'm just spitballing here
# 		-maybe output images n shit to an html file for viewing?
#					-webbrowser.open("file:///" + os.path.abspath(filename))
# 		-eventually, I want this thing communicating with a server at home
# 		-and also on an app =D
#
###############################################################



import os
import classPin
from urlparse import urlparse
import httplib

def check_user(u):
	url = "http://www.pinterest.com/" + u
	p = urlparse(url)
	conn = httplib.HTTPConnection(p.netloc)
	conn.request('Head', p.path)
	resp = conn.getresponse()
	print resp.status	
	return (resp.status < 400)



def main():
	print "--------------------------------------------------------\n"
	print "-                       PIN PULLER                     -\n"
	print "-                                                      -\n"
	print "-                       I was bored                    -\n"
	print "-                                                      -\n"
	print "-                                                      -\n"
	print "--------------------------------------------------------\n\n\n\n"


	print "Please give a username or full name that you use to access Pinterest:\n"

	while True:

		username = raw_input()
		print "searching for you...."
		if (check_user(username) == False):
			print "either you don't exist or you typo-ed, try again: \n"
		else:
			break

	#huzzah we have a valid user
	#print boards? CLASS TIME AAAAH YEAH


	u = classPin.user(username)
	u.print_boards()
	return


if __name__ =='__main__':
	main()
