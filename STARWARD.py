# generate random integer values
from random import randint
import random
import PySimpleGUI as sg
sg.change_look_and_feel('DarkBlue13')  

# generate some integers
#for _ in range(10):
#       value = randint(1, 12)
#       print(value)

#dict field = {numberPlanets}

def main():
#setup -----------------------------------------------------------------
	PLANETS = [
	 {'position' : 1, 'name' : 'bluePlanet',   'risk': '1'},
	 {'position' : 2, 'name' : 'greenPlanet',  'risk': '2'},
	 {'position' : 3, 'name' : 'yellowPlanet', 'risk': '3'},
	 {'position' : 4, 'name' : 'orangePlanet', 'risk': '4'},
	 {'position' : 5, 'name' : 'redPlanet',    'risk': '5'} ]
	 
	PLAYERS = [
	 {'player':1, 'ships' : 2, 'power' : 2, 'risk': '1'},
	 {'player':2, 'ships' : 2, 'power' : 2, 'risk': '2'},
	 {'player':3, 'ships' : 2, 'power' : 2, 'risk': '3'},
	 {'player':4, 'ships' : 2, 'power' : 2, 'risk': '4'} ]

	playingFieldSize = 0

#Build Phase -----------------------------------------------------------
	


#Discovery Phase -------------------------------------------------------	
	playingFieldSize = Planet_Draw()
	field = range(playingFieldSize)
	
	print("Drawing Planets...")
	print("New Planet # : ", playingFieldSize)
	planet_sample = random.choices(PLANETS, k=playingFieldSize)
	for i in field:
		print(planet_sample[i])
	
#Launch Phase ----------------------------------------------------------
	explore = input("Would you like to explore an available planet? y/n ")
	if (explore == "y"):
		planetChoice1 = input("Which planets will you explore first? \n(blue, green, yellow, orange or red : ")
		if (planetChoice1 == "blue"):
			sg.popup("Navigating to Blue Planet")
			print("Navigating to Blue Planet")
		if (planetChoice1 == "green"):
			print("Navigating to Green Planet")
			sg.popup("Navigating to Green Planet")
		if (planetChoice1 == "yellow"):
			print("Navigating to Yellow Planet")
			sg.popup("Navigating to Yellow Planet")
		if (planetChoice1 == "orange"):
			print("Navigating to Orange Planet")
			sg.popup("Navigating to Orange Planet")
		if (planetChoice1 == "red"):
			print("Navigating to Red Planet")
			sg.popup("Navigating to Red Planet")

	roll = input("roll dice? y/n ")
	if(roll == 'y'):
		roll_result = roll_dice_6s()
		print("You rolled a : ", roll_result)
		sg.popup("You rolled a : ", roll_result)
	else: 
		print("roll declined")
		exit

#Conflict Phase --------------------------------------------------------


#Encounter Phae --------------------------------------------------------
	
	
def roll_dice_6s():
	roll_result = randint(1,12)
	return roll_result
	
def Planet_Draw():
	numbPlanets = randint(1,9)
	return numbPlanets
	
def Planet_Explore():
	pass


if __name__ == "__main__":
	main()



