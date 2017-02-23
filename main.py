import threading
from threading import Thread
import time
cv = threading.Condition()
end = True

class Rover():
	"""Create Class Objects"""
	def __init__(self, wheel = [], position = []):
		self.wheel = wheel
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

def mainMenu():
	global end
	while end == True:
		print('---MAIN MENU---')
		print('1 - NOT_MADE')
		print('2 - NOT_MADE')
		print('3 - NOT_MADE')
		print('4 - NOT_MADE')
		print('5 - EXIT')
		inp = int(input("Please Enter A Number - "))
		if inp == 1:
			print('ERROR NOT MADE')
			print(' ')
		if inp == 2:
			print('ERROR NOT MADE')
			print(' ')
		if inp == 3:
			print('ERROR NOT MADE')
			print(' ')
		if inp == 4:
			print('ERROR NOT MADE')
			print(' ')
		if inp == 5:
			print('Exiting....')
			end = False
		else:
			("Error not a valid input")

def wheel1():
	while end == True:
		cv.acquire()
		#print('1')
		cv.notifyAll()
		cv.release()
		time.sleep(.3)

def wheel2():
	while end == True:
		cv.acquire()
		#print('2')
		cv.notifyAll()
		cv.release()
		time.sleep(.3)

def wheel3():
	while end == True:
		cv.acquire()
		#print('3')
		cv.notifyAll()
		cv.release()
		time.sleep(.3)

def wheel4():
	while end == True:
		cv.acquire()
		#print('4')
		cv.notifyAll()
		cv.release()
		time.sleep(.3)

def wheel5():
	while end == True:
		cv.acquire()
		#print('5')
		cv.notifyAll()
		cv.release()
		time.sleep(.3)

def wheel6():
	while end == True:
		cv.acquire()
		#print('6')
		cv.notifyAll()
		cv.release()
		time.sleep(.3)


Main = Thread(target=mainMenu, args=())
"""Antenna = Thread(target= , args=())"""
Wheel1 = Thread(target=wheel1, args=())
Wheel2 = Thread(target=wheel2, args=())
Wheel3 = Thread(target=wheel3, args=())
Wheel4 = Thread(target=wheel4, args=())
Wheel5 = Thread(target=wheel5, args=())
Wheel6 = Thread(target=wheel6, args=())
Main.start()
Wheel1.start()
Wheel2.start()
Wheel3.start()
Wheel4.start()
Wheel5.start()
Wheel6.start()
