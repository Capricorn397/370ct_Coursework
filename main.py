import threading
from threading import Thread
import time
from random import randint
cv = threading.Condition()
end = True
checkStop = False
moving = True
selectedWheel = 0
helpSelect = False
fix = ''

class Rover():
	"""Create Class Objects"""
	def __init__(self, wheel, wheelState, target):
		self.wheel = wheel
		self.target = target
		self.wheelState = wheelState

	def __str__(self):
		out = ' Wheel:' + str(self.wheel) + ' wheelState:' + str(self.wheelState) + ' target:' + str(self.target)
		return(out)

	def error(self):
		print('has an error')
		self.wheelState = False
		self.wheel = False
		self.target = randint(1,2)

w1 = Rover(True, True, 0)
w2 = Rover(True, True, 0)
w3 = Rover(True, True, 0)
w4 = Rover(True, True, 0)
w5 = Rover(True, True, 0)
w6 = Rover(True, True, 0)

def mainMenu():
	global end
	while end == True:
		"""print('---MAIN MENU---')
		print('1 - Generate Random Error')
		print('2 - Generate Multiple Errors')
		print('3 - NOT_MADE')
		print('4 - NOT_MADE')
		print('5 - EXIT')"""
		#inp = int(input("Please Enter A Number - "))
		inp = int(input())
		if inp == 1:
			print('Generating Error on one wheel')
			randomError()
		if inp == 2:
			cv.acquire()
			print('Generate Error on multiple wheels')
			num = int(input('Select Number of wheels to affect:'))
			while num != 0:
				randomError()
				num = num - 1
			cv.notifyAll()
			cv.release()
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
		global helpSelect
		global selectedWheel
		global fix
		if helpSelect == False:
			cv.acquire()
			#print('1')
			if w1.wheel == False:
				selectedWheel = 1
				if w1.wheelState == False:
					fix = 1
			cv.notifyAll()
			cv.release()
			time.sleep(1)

def wheel2():
	while end == True:
		global helpSelect
		global selectedWheel
		global fix
		if helpSelect == False:
			cv.acquire()
			#print('2')
			if w2.wheel == False:
				selectedWheel = 2
				if w2.wheelState == False:
					fix = 1
			cv.notifyAll()
			cv.release()
			time.sleep(1)

def wheel3():
	while end == True:
		global helpSelect
		global fix
		global selectedWheel
		if helpSelect == False:
			cv.acquire()
			#print('3')
			if w3.wheel == False:
				selectedWheel = 3
				if w3.wheelState == False:
					fix = 1
			cv.notifyAll()
			cv.release()
			time.sleep(1)

def wheel4():
	while end == True:
		global helpSelect
		global fix
		global selectedWheel
		if helpSelect == False:
			cv.acquire()
			#print('4')
			if w4.wheel == False:
				selectedWheel = 4
				if w4.wheelState == False:
					fix = 1
			cv.notifyAll()
			cv.release()
			time.sleep(1)

def wheel5():
	while end == True:
		global helpSelect
		global fix
		global selectedWheel
		if helpSelect == False:
			cv.acquire()
			#print('5')
			if w5.wheel == False:
				selectedWheel = 5
				if w5.wheelState == False:
					fix = 1
			cv.notifyAll()
			cv.release()
			time.sleep(1)

def wheel6():
	while end == True:
		global helpSelect
		global fix
		global selectedWheel
		if helpSelect == False:
			cv.acquire()
			#print('6')
			if w6.wheel == False:
				selectedWheel = 6
				if w6.wheelState == False:
					fix = 1
			cv.notifyAll()
			cv.release()
			time.sleep(1)

def checker():
	global checkStop
	global moving
	global fix
	global helpSelect
	while end == True:
		if helpSelect == False:
			cv.acquire()
			if (moving == False) and (w1.wheel == True and w2.wheel == True and w3.wheel == True and w4.wheel == True and w5.wheel == True and w6.wheel == True):
				moving = True
				checkStop = False
				print('Starting')
			if w1.wheel == False or w2.wheel == False or w3.wheel == False or w4.wheel == False or w5.wheel == False or w6.wheel == False:
				if checkStop == False:
					checkStop = True
					moving = False
					print('Stopped')
			cv.notifyAll()
			cv.release()
			time.sleep(.1)

def randomError():
	global helpSelect
	if helpSelect == False:
		wheelSelect = int(input('Select Wheel:'))
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

def wheelUpThread():
	global helpSelect
	global fix
	while end == True:
		if helpSelect == False:
			if fix == 1:
				cv.acquire()
				global selectedWheel
				print('Trying wheel up fixes')
				if selectedWheel == 1:
					if w1.target == 1:
						w1.wheelState = True
						w1.wheel = True
						print('Wheel 1 Up Fix')
				if selectedWheel == 2:
					if w2.target == 1:
						w2.wheelState = True
						w2.wheel = True
						print('Wheel 2 Up Fix')
				if selectedWheel == 3:
					if w3.target == 1:
						w3.wheelState = True
						w3.wheel = True
						print('Wheel 3 Up Fix')
				if selectedWheel == 4:
					if w4.target == 1:
						w4.wheelState = True
						w4.wheel = True
						print('Wheel 4 Up Fix')
				if selectedWheel == 5:
					if w5.target == 1:
						w5.wheelState = True
						w5.wheel = True
						print('Wheel 5 Up Fix')
				if selectedWheel == 6:
					if w6.target == 1:
						w6.wheelState = True
						w6.wheel = True
						print('Wheel 6 Up Fix')
				fix = 2
				cv.notifyAll()
				cv.release()

def wheelDownThread():
	global helpSelect
	global fix
	while end == True:
		if helpSelect == False:
			if fix == 2:
				cv.acquire()
				print('Trying wheel down fixes')
				global selectedWheel
				if selectedWheel == 1:
					if w1.target == 2:
						w1.wheelState = True
						w1.wheel = True
						print('Wheel 1 Down Fix')
				if selectedWheel == 2:
					if w2.target == 2:
						w2.wheelState = True
						w2.wheel = True
						print('Wheel 2 Down Fix')
				if selectedWheel == 3:
					if w3.target == 2:
						w3.wheelState = True
						w3.wheel = True
						print('Wheel 3 Down Fix')
				if selectedWheel == 4:
					if w4.target == 2:
						w4.wheelState = True
						w4.wheel = True
						print('Wheel 4 Down Fix')
				if selectedWheel == 5:
					if w5.target == 2:
						w5.wheelState = True
						w5.wheel = True
						print('Wheel 5 Down Fix')
				if selectedWheel == 6:
					if w6.target == 2:
						w6.wheelState = True
						w6.wheel = True
						print('Wheel 6 Down Fix')
				fix = 0
				cv.notifyAll()
				cv.release()

def callForHelp():
	global helpSelect
	global end
	global fix
	while end == True:
		if helpSelect == True:
			cv.acquire()
			print('Rover Cannot Fix Itself And Is Calling For Assistance')
			"""w1.wheelState = w2.wheelState = w3.wheelState = w4.wheelState = w5.wheelState = w6.wheelState = True
			w1.wheel = w2.wheel = w3.wheel = w4.wheel = w5.wheel = w6.wheel = True
			w1.target = w2.target = w3.target = w4.target = w5.target = w6.target = 0
			helpSelect = False
			fix = 0
			print('Assistance helped rover continue')"""
			print('Wheel 1 - ')
			print(w1)
			print('Wheel 2 - ')
			print(w2)
			print('Wheel 3 - ')
			print(w3)
			print('Wheel 4 - ')
			print(w4)
			print('Wheel 5 - ')
			print(w5)
			print('Wheel 6 - ')
			print(w6)
			cv.notify()
			cv.release()

Main = Thread(target=mainMenu, args=())
Checker = Thread(target=checker , args=())
Wheel1 = Thread(target=wheel1, args=())
Wheel2 = Thread(target=wheel2, args=())
Wheel3 = Thread(target=wheel3, args=())
Wheel4 = Thread(target=wheel4, args=())
Wheel5 = Thread(target=wheel5, args=())
Wheel6 = Thread(target=wheel6, args=())
WheelUp = Thread(target=wheelUpThread, args=())
WheelDown = Thread(target=wheelDownThread, args=())
Help = Thread(target=callForHelp, args=())
Main.start()
Wheel1.start()
Wheel2.start()
Wheel3.start()
Wheel4.start()
Wheel5.start()
Wheel6.start()
Checker.start()
WheelUp.start()
WheelDown.start()
Help.start()
