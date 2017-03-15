import threading
from threading import Thread
import time
from random import randint
import random
cv = threading.Condition()
end = True
runs = 1
checkStop = False
moving = True
selectedWheel = 0
helpSelect = False
fixThreads = False
fix = ''
fiveMRun = False
runChecker = []
log = []

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
		log.append('has an error')
		self.wheelState = False
		self.wheel = False
		self.target = randint(1,4)

w1 = Rover(True, True, 0)
w2 = Rover(True, True, 0)
w3 = Rover(True, True, 0)
w4 = Rover(True, True, 0)
w5 = Rover(True, True, 0)
w6 = Rover(True, True, 0)

def mainMenu():
	global end
	global runChecker
	global runs
	global fiveMRun
	while end == True:
		if runs == 1:
			print('---MAIN MENU---')
			print('1 - Generate Random Error')
			print('2 - Generate Multiple Errors')
			print('3 - Generate Rock Error')
			print('4 - 5m Run')
			print('5 - Output Log')
			print('6 - EXIT')
		if runs > 1:
			runs = runs - 1
		if runs == 1:
			inp = int(input())
		if inp == 1:
			if runs == 1:
				cv.acquire()
			log.append('Generating Error on one wheel')
			randomError()
			if runs <= 2:
				fiveMRun = False
				cv.notifyAll()
				cv.release()
		if inp == 2:
			cv.acquire()
			log.append('Generate Error on multiple wheels')
			num = int(input('Select Number of wheels to affect:'))
			while num != 0:
				randomError()
				num = num - 1
			cv.notifyAll()
			cv.release()
		if inp == 3:
			log.append('ERROR NOT MADE')
		if inp == 4:
			log.append('5m Run With Random Errors')
			if runs == 1:
				cv.acquire()
			runs = 7
			runChecker = [1,2,3,4,5,6]
			inp = 1
			fiveMRun = True
		if inp == 5:
			with open('log.txt', 'w') as file_handler:
    				for item in log:
        				file_handler.write("{}\n".format(item))
			print("Outputted Log To File...")
		if inp == 6:
			print('Exiting....')
			end = False
		else:
			("Error not a valid input")

def wheel1():
	while end == True:
		global helpSelect
		global selectedWheel
		global fixThreads
		global fix
		if helpSelect == False and fixThreads == False:
			cv.acquire()
			if w1.wheel == False:
				selectedWheel = 1
				if w1.wheelState == False:
					fixThreads = True
					fix = 1
			cv.notifyAll()
			cv.release()
			time.sleep(1)

def wheel2():
	while end == True:
		global helpSelect
		global selectedWheel
		global fixThreads
		global fix
		if helpSelect == False and fixThreads == False:
			cv.acquire()
			if w2.wheel == False:
				selectedWheel = 2
				if w2.wheelState == False:
					fixThreads = True
					fix = 1
			cv.notifyAll()
			cv.release()
			time.sleep(1)

def wheel3():
	while end == True:
		global helpSelect
		global fix
		global fixThreads
		global selectedWheel
		if helpSelect == False and fixThreads == False:
			cv.acquire()
			if w3.wheel == False:
				selectedWheel = 3
				if w3.wheelState == False:
					fixThreads = True
					fix = 1
			cv.notifyAll()
			cv.release()
			time.sleep(1)

def wheel4():
	while end == True:
		global helpSelect
		global fix
		global fixThreads
		global selectedWheel
		if helpSelect == False and fixThreads == False:
			cv.acquire()
			if w4.wheel == False:
				selectedWheel = 4
				if w4.wheelState == False:
					fixThreads = True
					fix = 1
			cv.notifyAll()
			cv.release()
			time.sleep(1)

def wheel5():
	while end == True:
		global helpSelect
		global fix
		global fixThreads
		global selectedWheel
		if helpSelect == False and fixThreads == False:
			cv.acquire()
			if w5.wheel == False:
				selectedWheel = 5
				if w5.wheelState == False:
					fixThreads = True
					fix = 1
			cv.notifyAll()
			cv.release()
			time.sleep(1)

def wheel6():
	while end == True:
		global helpSelect
		global fix
		global fixThreads
		global selectedWheel
		if helpSelect == False and fixThreads == False:
			cv.acquire()
			if w6.wheel == False:
				selectedWheel = 6
				if w6.wheelState == False:
					fixThreads = True
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
				log.append('Starting')
			if w1.wheel == False or w2.wheel == False or w3.wheel == False or w4.wheel == False or w5.wheel == False or w6.wheel == False:
				if checkStop == False:
					checkStop = True
					moving = False
					log.append('Stopped')
			cv.notifyAll()
			cv.release()
			time.sleep(.1)

def randomError():
	global helpSelect
	global fiveMRun
	global runChecker
	if helpSelect == False:
		if fiveMRun == False:
			wheelSelect = int(input('Select Wheel:'))
		else:
			wheelSelect = random.choice(runChecker)
			runChecker.remove(wheelSelect)
		if wheelSelect == 1:
			log.append('Wheel 1')
			w1.error()
		if wheelSelect == 2:
			log.append('Wheel 2')
			w2.error()
		if wheelSelect == 3:
			log.append('Wheel 3')
			w3.error()
		if wheelSelect == 4:
			log.append('Wheel 4')
			w4.error()
		if wheelSelect == 5:
			log.append('Wheel 5')
			w5.error()
		if wheelSelect == 6:
			log.append('Wheel 6')
			w6.error()

def wheelUpThread():
	global helpSelect
	global fix
	global selectedWheel
	while end == True:
		if helpSelect == False:
			if fix == 1:
				cv.acquire()
				log.append('Up Fixes For Wheel ' + str(selectedWheel))
				if selectedWheel == 1:
					if w1.target == 1:
						w1.wheelState = True
						w1.wheel = True
						log.append('Wheel 1 Up Fix')
				if selectedWheel == 2:
					if w2.target == 1:
						w2.wheelState = True
						w2.wheel = True
						log.append('Wheel 2 Up Fix')
				if selectedWheel == 3:
					if w3.target == 1:
						w3.wheelState = True
						w3.wheel = True
						log.append('Wheel 3 Up Fix')
				if selectedWheel == 4:
					if w4.target == 1:
						w4.wheelState = True
						w4.wheel = True
						log.append('Wheel 4 Up Fix')
				if selectedWheel == 5:
					if w5.target == 1:
						w5.wheelState = True
						w5.wheel = True
						log.append('Wheel 5 Up Fix')
				if selectedWheel == 6:
					if w6.target == 1:
						w6.wheelState = True
						w6.wheel = True
						log.append('Wheel 6 Up Fix')
				fix = 2
				cv.notifyAll()
				cv.release()

def wheelDownThread():
	global helpSelect
	global fix
	global selectedWheel
	while end == True:
		if helpSelect == False:
			if fix == 2:
				cv.acquire()
				log.append('Down Fixes For Wheel ' + str(selectedWheel))
				if selectedWheel == 1:
					if w1.target == 2:
						w1.wheelState = True
						w1.wheel = True
						log.append('Wheel 1 Down Fix')
				if selectedWheel == 2:
					if w2.target == 2:
						w2.wheelState = True
						w2.wheel = True
						log.append('Wheel 2 Down Fix')
				if selectedWheel == 3:
					if w3.target == 2:
						w3.wheelState = True
						w3.wheel = True
						log.append('Wheel 3 Down Fix')
				if selectedWheel == 4:
					if w4.target == 2:
						w4.wheelState = True
						w4.wheel = True
						log.append('Wheel 4 Down Fix')
				if selectedWheel == 5:
					if w5.target == 2:
						w5.wheelState = True
						w5.wheel = True
						log.append('Wheel 5 Down Fix')
				if selectedWheel == 6:
					if w6.target == 2:
						w6.wheelState = True
						w6.wheel = True
						log.append('Wheel 6 Down Fix')
				fix = 3
				cv.notifyAll()
				cv.release()

def rockFix():
	global helpSelect
	global fix
	global fixThreads
	global selectedWheel
	while end == True:
		if helpSelect == False:
			if fix == 3:
				cv.acquire()
				log.append('Rock Fixes For Wheel ' + str(selectedWheel))
				if selectedWheel == 1:
					if w1.target == 3:
						w1.wheelState = True
						w1.wheel = True
						log.append('Wheel 1 Down Fix')
				if selectedWheel == 2:
					if w2.target == 3:
						w2.wheelState = True
						w2.wheel = True
						log.append('Wheel 2 Down Fix')
				if selectedWheel == 3:
					if w3.target == 3:
						w3.wheelState = True
						w3.wheel = True
						log.append('Wheel 3 Down Fix')
				if selectedWheel == 4:
					if w4.target == 3:
						w4.wheelState = True
						w4.wheel = True
						log.append('Wheel 4 Down Fix')
				if selectedWheel == 5:
					if w5.target == 3:
						w5.wheelState = True
						w5.wheel = True
						log.append('Wheel 5 Down Fix')
				if selectedWheel == 6:
					if w6.target == 3:
						w6.wheelState = True
						w6.wheel = True
						log.append('Wheel 6 Down Fix')
				fix = 0
				fixThreads = False
				if selectedWheel == 1:
					if w1.wheel != True:
						helpSelect = True
						fixThreads = True
				if selectedWheel == 2:
					if w2.wheel != True:
						helpSelect = True
						fixThreads = True
				if selectedWheel == 3:
					if w3.wheel != True:
						helpSelect = True
						fixThreads = True
				if selectedWheel == 4:
					if w4.wheel != True:
						helpSelect = True
						fixThreads = True
				if selectedWheel == 5:
					if w5.wheel != True:
						helpSelect = True
						fixThreads = True
				if selectedWheel == 6:
					if w6.wheel != True:
						helpSelect = True
						fixThreads = True
				cv.notifyAll()
				cv.release()

def callForHelp():
	global helpSelect
	global end
	global selectedWheel
	global fix
	while end == True:
		if helpSelect == True:
			cv.acquire()
			log.append('Rover Cannot Fix Itself And Is Calling For Assistance For Wheel ' + str(selectedWheel))
			"""
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
			end = False"""
			if selectedWheel == 1:
				w1.wheel = True
				w1.wheelState = True
				w1.target = 0
			if selectedWheel == 2:
				w2.wheel = True
				w2.wheelState = True
				w2.target = 0
			if selectedWheel == 3:
				w3.wheel = True
				w3.wheelState = True
				w3.target = 0
			if selectedWheel == 4:
				w4.wheel = True
				w4.wheelState = True
				w4.target = 0
			if selectedWheel == 5:
				w5.wheel = True
				w5.wheelState = True
				w5.target = 0
			if selectedWheel == 6:
				w6.wheel = True
				w6.wheelState = True
				w6.target = 0
			helpSelect = False
			fixThreads = False
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
RockFixer = Thread(target=rockFix, args=())
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
RockFixer.start()
Help.start()
