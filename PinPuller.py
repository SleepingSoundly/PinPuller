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
import random
import bs4 from BeautifulSoup

def get_username():

	return


def get_boardname():
	return


def pull_boardnames(username, board_soup):
	# http://www.pinterest.com/liahoag/ (username) (search by name as opposed to username?)
	# search the html document for "h3 class = "boardName"" (matched?)
	# url is <a href = "username/boardname"> (spaces are '-'), called boardLinkWrapper

	return

def pull_pins(pin_soup):
	# search each pin (need some way of loading all the information from the page)
	# <div class="pinWrapper">, has an image and meta. (how do you display pictures?)


	return


def main():



	return


if __name__ =='__main__':
	main()
