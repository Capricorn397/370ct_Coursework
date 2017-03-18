import threading
from threading import Thread
import time
from random import randint
import random
cv = threading.Condition()
end = True #Variable to keep program running
runs = 1 #Run counter for the 5m run
checkStop = False #Variable for checking if checker is starting or stopping rover
moving = True #Variable for checking if rover is vectoring
selectedWheel = 0 #Chosen wheel to try fixes on
helpSelect = False #Variable to chose to call for help
fixThreads = False #Variable to select the fixing threads
rock = False #Variable denoting if rock error
fix = '' #Fix number for selecting the order of fixes tried
fiveMRun = False #Variable to show it is the 5m run
runChecker = [] #Array of wheels affected by the 5m run
log = [] #The log array that is Outputted

"""Wheel Class Used to create and store information for each wheel"""
class Wheel():
	"""Create Class Objects"""
	def __init__(self, wheel, wheelState, target):
		self.wheel = wheel
		self.target = target
		self.wheelState = wheelState
	"""Define default output string"""
	def __str__(self):
		out = ' Wheel:' + str(self.wheel) + ' wheelState:' + str(self.wheelState) + ' target:' + str(self.target)
		return(out)

	"""Generate an error on the wheel"""
	def error(self):
		log.append('has an error')
		self.wheelState = False
		self.wheel = False
		self.target = randint(1,4)

	"""Generate a rock error on the wheel"""
	def rock(self):
		log.append('has encountered a rock')
		self.wheelState = False
		self.wheel = False
		self.target = 3
"""Create the 6 wheels as class instances"""
w1 = Wheel(True, True, 0)
w2 = Wheel(True, True, 0)
w3 = Wheel(True, True, 0)
w4 = Wheel(True, True, 0)
w5 = Wheel(True, True, 0)
w6 = Wheel(True, True, 0)

"""Main Menu Thread"""
def mainMenu():
	global end
	global runChecker
	global runs
	global fiveMRun
	global rock
	while end == True:
		if runs == 1 or runs == 2: #If not in middle of 5m run
			print('---MAIN MENU---') #Output main menu choices
			print('1 - Generate Random Error')
			print('2 - Generate Multiple Errors')
			print('3 - Generate Rock Error')
			print('4 - 5m Run')
			print('5 - Output Log')
			print('6 - EXIT')
		if runs > 1: #If in 5m run
			runs = runs - 1 #Reduce runs to reach lmit of 5m
		if runs == 1: #If 5m not happening
			inp = int(input()) #Input selection
		if inp == 1: #If 1 inputted
			if runs == 1:
				cv.acquire()
			log.append('Generating Error on one wheel') #Add to log
			randomError() #Generate random error
			if runs <= 2: #If 5m run ending
				fiveMRun = False #Stop 5m run
				cv.notifyAll()
				cv.release()
		if inp == 2: #If 2 inputted
			cv.acquire()
			log.append('Generate Error on multiple wheels') #Add to log
			num = int(input('Select Number of wheels to affect:')) #Select amount of errors
			while num != 0: #While still errors to create
				randomError() #Generate random error
				num = num - 1 #Take 1 from amount of errors to create
			cv.notifyAll()
			cv.release()
		if inp == 3: #If 3 inputted
			cv.acquire()
			log.append('Generating Rock Error') #Add to log
			rock = True #Show rock error is happening
			randomError() #Generate error
			rock = False #Stop rock error reoccuring
			cv.notifyAll()
			cv.release()
		if inp == 4: #If 4 inputted
			log.append('5m Run With Random Errors') #Add to log
			if runs == 1:
				cv.acquire()
			runs = 7 #Set amount of runs left
			runChecker = [1,2,3,4,5,6] #Create array to stop repeating errors
			inp = 1 #Select input to create errors
			fiveMRun = True #Select that 5m run is happening
		if inp == 5: #If 5 inputted
			with open('log.txt', 'w') as file_handler: #Open log.txt file
    				for item in log: #For each log item
        				file_handler.write("{}\n".format(item)) #Write each item to log
			print("Outputted Log To File...") #Print complete message
		if inp == 6: #If 6 inputted
			print('Exiting....') #Print exit message
			end = False #End all threads
		else:
			("Error not a valid input")

"""Wheel 1 checker"""
def wheel1():
	while end == True:
		global helpSelect
		global selectedWheel
		global fixThreads
		global fix
		if helpSelect == False and fixThreads == False: #If no fixing occuring
			cv.acquire() #Acquire
			if w1.wheel == False: #If error on wheel
				selectedWheel = 1 #Set selected wheel to one
				if w1.wheelState == False: #If state is error
					fixThreads = True #Set to only fix threads
					fix = 1 #Start at first fixes
			cv.notifyAll() #Notify
			cv.release() #Release
			time.sleep(1)

"""Wheel 2 checker"""
def wheel2():
	while end == True:
		global helpSelect
		global selectedWheel
		global fixThreads
		global fix
		if helpSelect == False and fixThreads == False: #If no fixing occuring
			cv.acquire() #Acquire
			if w2.wheel == False: #If error on wheel
				selectedWheel = 2 #Set selected wheel to two
				if w2.wheelState == False: #If state is error
					fixThreads = True #Set to only fix threads
					fix = 1 #Start at first fix
			cv.notifyAll() #Notify
			cv.release() #Release
			time.sleep(1)

"""Wheel 3 checker"""
def wheel3():
	while end == True:
		global helpSelect
		global fix
		global fixThreads
		global selectedWheel
		if helpSelect == False and fixThreads == False: #If no fixing occuring
			cv.acquire() #Acquire
			if w3.wheel == False: #If error on wheel
				selectedWheel = 3 #Set selected wheel to three
				if w3.wheelState == False: #If state is error
					fixThreads = True #Set to only fix threads
					fix = 1 #Start at first fix
			cv.notifyAll() #Notify
			cv.release() #Release
			time.sleep(1)

"""Wheel 4 checker"""
def wheel4():
	while end == True:
		global helpSelect
		global fix
		global fixThreads
		global selectedWheel
		if helpSelect == False and fixThreads == False: #If no fixing occuring
			cv.acquire() #Acquire
			if w4.wheel == False: #If error on wheel
				selectedWheel = 4 #Set selected wheel to four
				if w4.wheelState == False: #If state is error
					fixThreads = True #Set to only fix threads
					fix = 1 #Start at first fix
			cv.notifyAll() #Notify
			cv.release() #Release
			time.sleep(1)

"""Wheel 5 clicker"""
def wheel5():
	while end == True:
		global helpSelect
		global fix
		global fixThreads
		global selectedWheel
		if helpSelect == False and fixThreads == False: #If no fixing occuring
			cv.acquire() #Acquire
			if w5.wheel == False: #If error on wheel
				selectedWheel = 5 #Set selected wheel to five
				if w5.wheelState == False: #If state is error
					fixThreads = True #Set to only fix threads
					fix = 1 #Start at first fix
			cv.notifyAll() #Notify
			cv.release() #Release
			time.sleep(1)

"""Wheel 6 clicker"""
def wheel6():
	while end == True:
		global helpSelect
		global fix
		global fixThreads
		global selectedWheel
		if helpSelect == False and fixThreads == False: #If no fixing occuring
			cv.acquire() #Acquire
			if w6.wheel == False: #If error on wheel
				selectedWheel = 6 #Set selected wheel to six
				if w6.wheelState == False: #If state is error
					fixThreads = True #Set to only fix threads
					fix = 1 #Start at first fix
			cv.notifyAll() #Notify
			cv.release() #Release
			time.sleep(1)

"""Movement Checker Thread"""
def checker():
	global checkStop
	global moving
	global fix
	global helpSelect
	while end == True:
		if helpSelect == False: #If not calling home
			cv.acquire() #Acquire
			if (moving == False) and (w1.wheel == True and w2.wheel == True and w3.wheel == True and w4.wheel == True and w5.wheel == True and w6.wheel == True): #If not moving and all wheels fine
				moving = True #Start moving
				checkStop = False #Set checking to false
				log.append('Starting') #Add to log
			if w1.wheel == False or w2.wheel == False or w3.wheel == False or w4.wheel == False or w5.wheel == False or w6.wheel == False: #If any wheel has an error
				if checkStop == False: #If checking is false
					checkStop = True #Set checking to true
					moving = False #Stop moving
					log.append('Stopped') #Add to log
			cv.notifyAll() #Notify
			cv.release() #Release
			time.sleep(.1)

"""Random Error Wheel Selector"""
def randomError():
	global helpSelect
	global rock
	global fiveMRun
	global runChecker
	if helpSelect == False: #If not calling home
		if fiveMRun == False: #If not in 5m run
			wheelSelect = int(input('Select Wheel:')) #User input to select wheel
		else:
			wheelSelect = random.choice(runChecker) #Randomly select wheel
			runChecker.remove(wheelSelect) #Remove selected from list so no repeat wheel for errors in 5m run
		if wheelSelect == 1:
			log.append('Wheel 1') #Add to log
			if rock == True: #If rock error
				w1.rock()
			else: #If random error
				w1.error()
		if wheelSelect == 2:
			log.append('Wheel 2') #Add to log
			if rock == True: #If rock error
				w2.rock()
			else: #If random error
				w2.error()
		if wheelSelect == 3:
			log.append('Wheel 3') #Add to log
			if rock == True: #If rock error
				w3.rock()
			else: #If random error
				w3.error()
		if wheelSelect == 4:
			log.append('Wheel 4') #Add to log
			if rock == True: #If rock error
				w4.rock()
			else: #If random error
				w4.error()
		if wheelSelect == 5:
			log.append('Wheel 5') #Add to log
			if rock == True: #If rock error
				w5.rock()
			else: #If random error
				w5.error()
		if wheelSelect == 6:
			log.append('Wheel 6') #Add to log
			if rock == True: #If rock error
				w6.rock()
			else: #If random error
				w6.error()

"""Wheel up fix thread"""
def wheelUpThread():
	global helpSelect
	global fix
	global selectedWheel
	while end == True:
		if helpSelect == False: #If not callng for help
			if fix == 1: #If on correct fix set
				cv.acquire() #Acquire
				log.append('Up Fixes For Wheel ' + str(selectedWheel)) #Add to log
				if selectedWheel == 1: #If wheel 1 being fixed
					if w1.target == 1: #If error is correct for this fix
						w1.wheelState = True #Fix Wheel
						w1.wheel = True
						log.append('Wheel 1 Up Fix') #Add to log
				if selectedWheel == 2: #If wheel 2 being fixed
					if w2.target == 1: #If error is correct for this fix
						w2.wheelState = True #Fix Wheel
						w2.wheel = True
						log.append('Wheel 2 Up Fix') #Add to log
				if selectedWheel == 3: #If wheel 3 being fixed
					if w3.target == 1: #If error is correct for this fix
						w3.wheelState = True #Fix Wheel
						w3.wheel = True
						log.append('Wheel 3 Up Fix') #Add to log
				if selectedWheel == 4: #If wheel 4 being fixed
					if w4.target == 1: #If error is correct for this fix
						w4.wheelState = True #Fix Wheel
						w4.wheel = True
						log.append('Wheel 4 Up Fix') #Add to log
				if selectedWheel == 5: #If wheel 5 being fixed
					if w5.target == 1: #If error is correct for this fix
						w5.wheelState = True #Fix Wheel
						w5.wheel = True
						log.append('Wheel 5 Up Fix') #Add to log
				if selectedWheel == 6: #If wheel 6 being fixed
					if w6.target == 1: #If error is correct for this fix
						w6.wheelState = True #Fix Wheel
						w6.wheel = True
						log.append('Wheel 6 Up Fix') #Add to log
				fix = 2 #Start next fix set
				cv.notifyAll() #Notify
				cv.release() #Release

def wheelDownThread():
	global helpSelect
	global fix
	global selectedWheel
	while end == True:
		if helpSelect == False: #If not calling for help
			if fix == 2: #If on correct fix set
				cv.acquire() #Acquire
				log.append('Down Fixes For Wheel ' + str(selectedWheel))
				if selectedWheel == 1: #If wheel 1 being fixed
					if w1.target == 2: #If error is correct for this fix
						w1.wheelState = True #Fix Wheel
						w1.wheel = True
						log.append('Wheel 1 Down Fix') #Add to log
				if selectedWheel == 2: #If wheel 2 being fixed
					if w2.target == 2: #If error is correct for this fix
						w2.wheelState = True #Fix Wheel
						w2.wheel = True
						log.append('Wheel 2 Down Fix') #Add to log
				if selectedWheel == 3: #If wheel 3 being fixed
					if w3.target == 2: #If error is correct for this fix
						w3.wheelState = True #Fix Wheel
						w3.wheel = True
						log.append('Wheel 3 Down Fix') #Add to log
				if selectedWheel == 4: #If wheel 4 being fixed
					if w4.target == 2: #If error is correct for this fix
						w4.wheelState = True #Fix Wheel
						w4.wheel = True
						log.append('Wheel 4 Down Fix') #Add to log
				if selectedWheel == 5: #If wheel 5 being fixed
					if w5.target == 2: #If error is correct for this fix
						w5.wheelState = True #Fix Wheel
						w5.wheel = True
						log.append('Wheel 5 Down Fix') #Add to log
				if selectedWheel == 6: #If wheel 6 being fixed
					if w6.target == 2: #If error is correct for this fix
						w6.wheelState = True #Fix Wheel
						w6.wheel = True
						log.append('Wheel 6 Down Fix') #Add to log
				fix = 3 #Start next fix set
				cv.notifyAll() #Notify
				cv.release() #Release

def rockFix():
	global helpSelect
	global fix
	global fixThreads
	global selectedWheel
	while end == True:
		if helpSelect == False: #If not calling for help
			if fix == 3: #If on correct fix set
				cv.acquire() #Acquire
				log.append('Rock Fixes For Wheel ' + str(selectedWheel))
				if selectedWheel == 1: #If wheel 1 being fixed
					if w1.target == 3: #If error is correct for this fix
						w1.wheelState = True #Fix Wheel
						w1.wheel = True
						log.append('Wheel 1 Rock Fix') #Add to log
				if selectedWheel == 2: #If wheel 2 being fixed
					if w2.target == 3: #If error is correct for this fix
						w2.wheelState = True #Fix Wheel
						w2.wheel = True
						log.append('Wheel 2 Rock Fix') #Add to log
				if selectedWheel == 3: #If wheel 3 being fixed
					if w3.target == 3: #If error is correct for this fix
						w3.wheelState = True #Fix Wheel
						w3.wheel = True
						log.append('Wheel 3 Rock Fix') #Add to log
				if selectedWheel == 4: #If wheel 4 being fixed
					if w4.target == 3: #If error is correct for this fix
						w4.wheelState = True #Fix Wheel
						w4.wheel = True
						log.append('Wheel 4 Rock Fix') #Add to log
				if selectedWheel == 5: #If wheel 5 being fixed
					if w5.target == 3: #If error is correct for this fix
						w5.wheelState = True #Fix Wheel
						w5.wheel = True
						log.append('Wheel 5 Rock Fix') #Add to log
				if selectedWheel == 6: #If wheel 6 being fixed
					if w6.target == 3: #If error is correct for this fix
						w6.wheelState = True #Fix Wheel
						w6.wheel = True
						log.append('Wheel 6 Rock Fix') #Add to log
				fix = 0 #Reset fixes
				fixThreads = False #Allow other threads to run
				if selectedWheel == 1: #If selected wheel
					if w1.wheel != True: #Is not fixed
						helpSelect = True #Set to call for help
						fixThreads = True #Set to only fixing threads
				if selectedWheel == 2: #If selected wheel
					if w2.wheel != True: #If selected wheel
						helpSelect = True #Is not fixed
						fixThreads = True #Set to only fixing threads
				if selectedWheel == 3: #If selected wheel
					if w3.wheel != True: #Is not fixed
						helpSelect = True #Set to call for help
						fixThreads = True #Set to only fixing threads
				if selectedWheel == 4: #If selected wheel
					if w4.wheel != True: #Is not fixed
						helpSelect = True #Set to call for help
						fixThreads = True #Set to only fixing threads
				if selectedWheel == 5: #If selected wheel
					if w5.wheel != True: #Is not fixed
						helpSelect = True #Set to call for help
						fixThreads = True #Set to only fixing threads
				if selectedWheel == 6: #If selected wheel
					if w6.wheel != True: #Is not fixed
						helpSelect = True #Set to call for help
						fixThreads = True #Set to only fixing threads
				cv.notifyAll() #Notify
				cv.release() #Release

"""Call for help thread"""
def callForHelp():
	global helpSelect
	global end
	global selectedWheel
	global fix
	while end == True:
		if helpSelect == True: #If calling for help
			cv.acquire() #Acquire
			log.append('Rover Cannot Fix Itself And Is Calling For Assistance For Wheel ' + str(selectedWheel)) #Add to log
			if selectedWheel == 1: #If 1 is selected wheel
				w1.wheel = True #Fix Wheel
				w1.wheelState = True
				w1.target = 0
			if selectedWheel == 2: #If 2 is selected wheel
				w2.wheel = True #Fix Wheel
				w2.wheelState = True
				w2.target = 0
			if selectedWheel == 3: #If 3 is selected wheel
				w3.wheel = True #Fix Wheel
				w3.wheelState = True
				w3.target = 0
			if selectedWheel == 4: #If 4 is selected wheel
				w4.wheel = True #Fix Wheel
				w4.wheelState = True
				w4.target = 0
			if selectedWheel == 5: #If 5 is selected wheel
				w5.wheel = True #Fix Wheel
				w5.wheelState = True
				w5.target = 0
			if selectedWheel == 6: #If 6 is selected wheel
				w6.wheel = True #Fix Wheel
				w6.wheelState = True
				w6.target = 0
			helpSelect = False #Stop calling for help
			fixThreads = False #Allow non fixing threads to run
			cv.notify() #Notify
			cv.release() #Release

"""Define the threads"""
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

"""Start the threads"""
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
