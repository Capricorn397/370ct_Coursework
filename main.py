import threading
from threading import Thread
import time
from random import randint
cv = threading.Condition()
end = True
checkStop = False
moving = True

class Rover():
	"""Create Class Objects"""
	def __init__(self, wheel, wheelState, target):
		self.wheel = wheel
		self.target = target
		self.wheelState = wheelState

	"""Casts outputs"""
	def __repr__(self):
		return "This is the output"

	def error(self):
		selector = randint(0,1)
		if selector == 0:
			print('is now FreeWheeling')
			self.wheelState = 'FreeWheeling'
			self.wheel = False
		if selector == 1:
			print('is now Sinking')
			self.wheelState = 'Sinking'
			self.wheel = False

	def wheelUp(self):
		self.wheel = True
		self.wheelState = 'Fine'
		print('Wheel Up Fix')
		return

	def wheelDown(self):
		self.wheel = True
		self.wheelState = 'Fine'
		print('Wheel Down Fix')
		return


	def callHome(self):
		return "This is the output"

w1 = Rover(True, 'Fine', 0)
w2 = Rover(True, 'Fine', 0)
w3 = Rover(True, 'Fine', 0)
w4 = Rover(True, 'Fine', 0)
w5 = Rover(True, 'Fine', 0)
w6 = Rover(True, 'Fine', 0)

def mainMenu():
	global end
	while end == True:
		"""print('---MAIN MENU---')
		print('1 - Generate Random Error')
		print('2 - NOT_MADE')
		print('3 - NOT_MADE')
		print('4 - NOT_MADE')
		print('5 - EXIT')"""
		#inp = int(input("Please Enter A Number - "))
		inp = int(input())
		if inp == 1:
			print('Generating Error on one wheel')
			randomError()
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
			if w1.wheelState == 'FreeWheeling':
				w1.wheelDown()
			if w1.wheelState == 'Sinking':
				w1.wheelUp()
			else:
				w1.wheel = True
		cv.notifyAll()
		cv.release()
		time.sleep(1)

def wheel2():
	while end == True:
		cv.acquire()
		#print('2')
		if w2.wheel == False:
			if w2.wheelState == 'FreeWheeling':
				w2.wheelDown()
			if w2.wheelState == 'Sinking':
				w2.wheelUp()
			else:
				w2.wheel = True
		cv.notifyAll()
		cv.release()
		time.sleep(1)

def wheel3():
	while end == True:
		cv.acquire()
		#print('3')
		if w3.wheel == False:
			if w3.wheelState == 'FreeWheeling':
				w3.wheelDown()
			if w3.wheelState == 'Sinking':
				w3.wheelUp()
			else:
				w3.wheel = True
		cv.notifyAll()
		cv.release()
		time.sleep(1)

def wheel4():
	while end == True:
		cv.acquire()
		#print('4')
		if w4.wheel == False:
			if w4.wheelState == 'FreeWheeling':
				w4.wheelDown()
			if w4.wheelState == 'Sinking':
				w4.wheelUp()
			else:
				w4.wheel = True
		cv.notifyAll()
		cv.release()
		time.sleep(1)

def wheel5():
	while end == True:
		cv.acquire()
		#print('5')
		if w5.wheel == False:
			if w5.wheelState == 'FreeWheeling':
				w5.wheelDown()
			if w5.wheelState == 'Sinking':
				w5.wheelUp()
			else:
				w5.wheel = True
		cv.notifyAll()
		cv.release()
		time.sleep(1)

def wheel6():
	while end == True:
		cv.acquire()
		#print('6')
		if w6.wheel == False:
			if w6.wheelState == 'FreeWheeling':
				w6.wheelDown()
			if w6.wheelState == 'Sinking':
				w6.wheelUp()
			else:
				w6.wheel = True
		cv.notifyAll()
		cv.release()
		time.sleep(1)

def checker():
	global checkStop
	global moving
	while end == True:
		cv.acquire()
		if (moving == False) and (w1.wheel == True or w2.wheel == True or w3.wheel == True or w4.wheel == True or w5.wheel == True or w6.wheel == True):
			moving = True
			checkStop = False
			print('Starting')
		if w1.wheel == False or w2.wheel == False or w3.wheel == False or w4.wheel == False or w5.wheel == False or w6.wheel == False:
			if checkStop == False:
				w1.wheel = False
				w2.wheel = False
				w3.wheel = False
				w4.wheel = False
				w5.wheel = False
				w6.wheel = False
				checkStop = True
				moving = False
				print('Stopped')
		cv.notifyAll()
		cv.release()
		time.sleep(.3)

def randomError():
	wheelSelect = randint(1,6)
	if wheelSelect == 1:
		print('Wheel 1')
		w1.error()
	if wheelSelect == 2:
		print('Wheel 2')
		w2.error()
	if wheelSelect == 3:
		print('Wheel 3')
		w3.error()
	if wheelSelect == 4:
		print('Wheel 4')
		w4.error()
	if wheelSelect == 5:
		print('Wheel 5')
		w5.error()
	if wheelSelect == 6:
		print('Wheel 6')
		w6.error()

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
