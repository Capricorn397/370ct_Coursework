import threading
from threading import Thread
import time
cv = threading.Condition()
end = True
checkStop = False

class Rover():
	"""Create Class Objects"""
	def __init__(self, wheel, wheelState, position = []):
		self.wheel = wheel
		self.position = position
		self.wheelState = wheelState

	"""Casts outputs"""
	def __repr__(self):
		return "This is the output"

	def error(self):
		if self.wheelState == 'Error':
			self.wheel = False
	def wheelUp(self):
		return "This is the output"

	def wheelDown(self):
		return "This is the output"

	def wheelRight(self):
		return "This is the output"

	def wheelLeft(self):
		return "This is the output"

	def forward(self, position):
		return "This is the output"

	def reverse(self, position):
		return "This is the output"

	def stop(self):
		return "This is the output"

	def callHome(self, antenna):
		return "This is the output"

w1 = Rover(True, 'Fine', [1,2,3])
w2 = Rover(True, 'Fine', [1,2,3])
w3 = Rover(True, 'Fine', [1,2,3])
w4 = Rover(True, 'Fine', [1,2,3])
w5 = Rover(True, 'Fine', [1,2,3])
w6 = Rover(True, 'Fine', [1,2,3])

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
		if w1.wheel == False:
			'check wheelState'
			'Run Fix type based on Wheelstate'
		w1.error()
		cv.notifyAll()
		cv.release()
		time.sleep(.3)

def wheel2():
	while end == True:
		cv.acquire()
		#print('2')
		if w2.wheel == False:
			'check wheelState'
			'Run Fix type based on Wheelstate'
		w2.error()
		cv.notifyAll()
		cv.release()
		time.sleep(.3)

def wheel3():
	while end == True:
		cv.acquire()
		#print('3')
		if w3.wheel == False:
			'check wheelState'
			'Run Fix type based on Wheelstate'
		w3.error()
		cv.notifyAll()
		cv.release()
		time.sleep(.3)

def wheel4():
	while end == True:
		cv.acquire()
		#print('4')
		if w4.wheel == False:
			'check wheelState'
			'Run Fix type based on Wheelstate'
		w4.error()
		cv.notifyAll()
		cv.release()
		time.sleep(.3)

def wheel5():
	while end == True:
		cv.acquire()
		#print('5')
		if w5.wheel == False:
			'check wheelState'
			'Run Fix type based on Wheelstate'
		w5.error()
		cv.notifyAll()
		cv.release()
		time.sleep(.3)

def wheel6():
	while end == True:
		cv.acquire()
		#print('6')
		if w6.wheel == False:
			'check wheelState'
			'Run Fix type based on Wheelstate'
		w6.error()
		cv.notifyAll()
		cv.release()
		time.sleep(.3)

def checker():
	global checkStop
	while end == True:
		cv.acquire()
		if w1.wheel or w2.wheel or w3.wheel or w4.wheel or w5.wheel or w6.wheel == False:
			if checkStop == False:
				w1.wheel = False
				w2.wheel = False
				w3.wheel = False
				w4.wheel = False
				w5.wheel = False
				w6.wheel = False
				checkStop = True
				print('Stopped')
		cv.notifyAll()
		cv.release()
		time.sleep(.3)

Main = Thread(target=mainMenu, args=())
Checker = Thread(target=checker , args=())
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
Checker.start()
