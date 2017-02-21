from threading import Thread
from threading import Lock
import threading
lock = Lock()
cv = threading.Condition()

class Rover():
	"""Create Class Objects"""
	def __init__(self, w1 = [], w2 = [], w3 = [], w4 = [], w5 = [], w6 = [], position = []):
		self.w1 = w1
		self.w2 = w2
		self.w3 = w3
		self.w4 = w4
		self.w5 = w5
		self.w6 = w6
		self.position = position

	"""Casts outputs"""
	def __repr__(self):
		return "This is the output"

	def wheelUp(self, wheel):
		return "This is the output"

	def wheelDown(self, wheel):
		return "This is the output"

	def wheelRight(self, wheel):
		return "This is the output"

	def wheelLeft(self, wheel):
		return "This is the output"

	def forward(self, position):
		return "This is the output"

	def reverse(self, position):
		return "This is the output"

	def stop(self):
		return "This is the output"

	def callHome(self, antenna):
		return "This is the output"

instance = Rover()

def mainMenu():
	x = 0
	while x == 0:
		print('---MAIN MENU---')
		print('1 - NOT_MADE')
		print('2 - NOT_MADE')
		print('3 - NOT_MADE')
		print('4 - NOT_MADE')
		print('5 - EXIT')
		inp = input("Please Enter A Number - ")
		if inp == '1':
			print('ERROR NOT MADE')
			print(' ')
		if inp == '2':
			print('ERROR NOT MADE')
			print(' ')
		if inp == '3':
			print('ERROR NOT MADE')
			print(' ')
		if inp == '4':
			print('ERROR NOT MADE')
			print(' ')
		if inp == '5':
			print('Exiting....')
			x = 1
		else:
			("Error not a valid input")


Main = Thread(target=mainMenu, args=())
"""Antenna = Thread(target= , args=())
Wheel1 = Thread(target= , args=())
Wheel2 = Thread(target= , args=())
Wheel3 = Thread(target= , args=())
Wheel4 = Thread(target= , args=())
Wheel5 = Thread(target= , args=())
Wheel6 = Thread(target= , args=())"""
Main.start()
