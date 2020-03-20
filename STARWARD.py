# generate random integer values
from random import randint
import random
#import PySimpleGUI as sg
#sg.change_look_and_feel('DarkBlue13')



def main():
#setup -----------------------------------------------------------------
	PLANETS = [
	 {'position' : 1, 'name' : 'bluePlanet',   'risk': 1},
	 {'position' : 2, 'name' : 'greenPlanet',  'risk': 2},
	 {'position' : 3, 'name' : 'yellowPlanet', 'risk': 3},
	 {'position' : 4, 'name' : 'orangePlanet', 'risk': 4},
	 {'position' : 5, 'name' : 'redPlanet',    'risk': 5} ]
	 
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
		planetChoice1 = input("Which planets will you explore first? \n(blue, green, yellow, orange or red) : ")
		if (planetChoice1 == "blue"):
			#sg.popup("Navigating to Blue Planet")
			print("Navigating to Blue Planet")
			print("\nrisk = ",PLANETS[1]['risk'])
			chosen_planet = PLANETS[1]
			
		if (planetChoice1 == "green"):
			print("Navigating to Green Planet")
			print("\nrisk = ",PLANETS[2]['risk'])
			#sg.popup("Navigating to Green Planet")
			chosen_planet = PLANETS[2]
			
		if (planetChoice1 == "yellow"):
			print("Navigating to Yellow Planet")
			print("\nrisk = ",PLANETS[3]['risk'])
			#sg.popup("Navigating to Yellow Planet")
			chosen_planet = PLANETS[3]
			
		if (planetChoice1 == "orange"):
			print("Navigating to Orange Planet")
			print("\nrisk = ",PLANETS[4]['risk'])
			#sg.popup("Navigating to Orange Planet")
			chosen_planet = PLANETS[4]
			
		if (planetChoice1 == "red"):
			print("Navigating to Red Planet")
			print("\nrisk = ",PLANETS[5]['risk'])
			#sg.popup("Navigating to Red Planet")
			chosen_planet = PLANETS[5]
	
	print("\nChosen Planet : {}\n".format(chosen_planet))
	
	roll = input("roll dice? y/n ")
	if(roll == 'y'):
		roll_result = roll_dice_6s()
		print("You rolled a : ", roll_result)
		#sg.popup("You rolled a : ", roll_result)
		
	else:
		print("roll declined")
		exit

#Conflict Phase --------------------------------------------------------


#Encounter Phae --------------------------------------------------------
	
	
def roll_dice_6s():
	roll_result = randint(2,12)
	return roll_result
	
def Planet_Draw():
	numbPlanets = randint(1,9)
	return numbPlanets
	
def Planet_Explore():
	pass

def easygrid():
    list = [[1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25]
            ]
    for i in list:
        print(i)


if __name__ == "__main__":
	easygrid()
	main()



