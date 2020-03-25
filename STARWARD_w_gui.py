# generate random integer values
from random import randint
import pygame 
import sys, random, pygame
import numpy as np
from pygame.locals import *



def main():
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((400, 300))
	pygame.display.set_caption('-----STARWARD-----')
#setup -----------------------------------------------------------------
	PLANETS = [
	 {'position' : 1, 'name' : 'bluePlanet',   'risk': 1},
	 {'position' : 2, 'name' : 'greenPlanet',  'risk': 2},
	 {'position' : 3, 'name' : 'yellowPlanet', 'risk': 3},
	 {'position' : 4, 'name' : 'orangePlanet', 'risk': 4},
	 {'position' : 5, 'name' : 'redPlanet',    'risk': 5} ]
	 
	PLAYERS = [
	 {'player':1, 'ships' : 2, 'power' : 2, 'planets_occupied': 0},
	 {'player':3, 'ships' : 2, 'power' : 2, 'planets_occupied': 0},
	 {'player':2, 'ships' : 2, 'power' : 2, 'planets_occupied': 0},
	 {'player':4, 'ships' : 2, 'power' : 2, 'planets_occupied': 0} ]

	playingFieldSize = 0
	

#Build Phase -----------------------------------------------------------
	


#Discovery Phase -------------------------------------------------------
	while (True):	
	
		playingFieldSize = Planet_Draw()
		field = range(playingFieldSize)

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()
		
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
				print("Navigating to Blue Planet")
				print("\nrisk = ",PLANETS[0]['risk'])
				chosen_planet = PLANETS[0]
				
			if (planetChoice1 == "green"):
				print("Navigating to Green Planet")
				print("\nrisk = ",PLANETS[1]['risk'])
				chosen_planet = PLANETS[1]
				
			if (planetChoice1 == "yellow"):
				print("Navigating to Yellow Planet")
				print("\nrisk = ",PLANETS[2]['risk'])
				chosen_planet = PLANETS[2]
				
			if (planetChoice1 == "orange"):
				print("Navigating to Orange Planet")
				print("\nrisk = ",PLANETS[3]['risk'])
				chosen_planet = PLANETS[3]
				
			if (planetChoice1 == "red"):
				print("Navigating to Red Planet")
				print("\nrisk = ",PLANETS[4]['risk'])
				chosen_planet = PLANETS[4]
	
		print("\nChosen Planet : {}\n".format(chosen_planet))
	
		roll = input("roll dice? y/n ")
		if(roll == 'y'):
			roll_result = roll_dice_6s()
			print("You rolled a : ", roll_result)
		else:
			print("roll declined")
			exit
	
		Planet_Explore (roll_result, chosen_planet)
		
		print("-------------------------------------------")
		print("\n\twhile loop completed\n")
		print("-------------------------------------------\n")
		#pygame.quit()
		#sys.exit()
	

#Conflict Phase --------------------------------------------------------


#Encounter Phae --------------------------------------------------------
	
	
def roll_dice_6s():
	roll_result = randint(1,9)
	return roll_result
	
def Planet_Draw():
	numbPlanets = randint(1,9)
	return numbPlanets
	
def Planet_Explore(rr, cp):
	if (rr < cp['risk']):
		print("\n\t---Ship Destoryed on Entry---\n")
		
	else: 
		print("\n\t---Planet Exploration Successful---\n")
	
	

def easygrid():
    grid = np.zeros((5,5), dtype=int) 
    print("\n",grid)

if __name__ == "__main__":
	easygrid()
	main()



