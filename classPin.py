###############################################################
#				PinPuller 
#					class: pin, board, user
#
#
###############################################################
from bs4 import BeautifulSoup
import string
import requests

def filter_print(str):
	return (''.join)([c for c in str if ord(c) > 31 or ord(c) == 9])


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
		self.disc = ""
		self.pins =  []
		return

	def populate_pins():
		return


	def add_discription(str_disc):
		self.disc = str_disc

	def print_board(self):
		print self.title, self.b_url, self.p_url, "\n"

	def print_board_title(self):
		print self.title
	def print_board_url(self):
		print self.b_url	
	def print_board_pic(self):
		print self.p_url





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

		for link in soup.find_all('img', 'boardCover'):
			if(link.get('alt')):
				title_s = link.get('alt')
				titles.append(filter(lambda x: x in string.printable, (title_s.split(' / '))[0]))  #error?
				pics.append(link.get('src')) # the url isn't in this tag, where is it?
				

		for link in soup.find_all('a', 'boardLinkWrapper'):
			urls.append(link.get('href'))

		for i in range(0, len(urls) - 1):
			self.boards.append(board(titles[i], urls[i], pics[i]))

		return

	def print_boards(self):
		for i in self.boards:
			i.print_board_title()
		return 0

	def board_exists(self, i):
		for s in range(0, len(self.boards) - 1):
			if (self.boards[s].title).lower() == i.lower():
				return True

		return False
				




