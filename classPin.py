###############################################################
#				PinPuller 
#					class: pin, board, user
#
#
###############################################################
from bs4 import BeautifulSoup

import requests




class pin:
	def __init__(self, t, p, disc):
		self.title = t
		self.p_url = p
		self.d = disc

		# <div class="pinWrapper">??


class board:
	def __init__(self, t, b, p):
		self.title = t
		self.b_url = b
		self.p_url = p
		self.pins =  []
		return

	def print_board(self):
		print self.title, self.b_url, self.p_url

class user:
	def __init__(self, username):

		# go out with name and check if it's real, populate the variable
		self.name = username
		self.u_url = "http://www.pinterest.com/" + username

		#go out and parse html to find board names
		self.boards = []
		r = requests.get(self.u_url)
		data = r.text
		soup = BeautifulSoup(data)
		titles = []
		urls = []
		pics = []

		for link in soup.find_all('img'):
			if(link.get('alt')):
				title_s = link.get('alt')
				titles.append((title_s.split(' / '))[0])
				pics.append(link.get('href'))

		for link in soup.find_all('a', 'boardLinkWrapper'):
			urls.append(link.get('href'))

		for i in range(0, len(urls) - 1):
			self.boards.append(board(titles[i], urls[i], pics[i]))

		return

	def print_boards(self):
		for i in self.boards:
			i.print_board()
			print "\n"
		return 0
				




