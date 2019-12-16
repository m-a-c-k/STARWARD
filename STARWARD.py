# generate random integer values
from random import randint
import random
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

	playingField = {'numbPlanets' : 0,} 

#Build Phase -----------------------------------------------------------
	


#Discovery Phase -------------------------------------------------------	
	playingField['numbPlanets'] = Planet_Draw()
	field = range(playingField['numbPlanets'])
	
	print("Drawing Planets...")
	print("New Planet # : ", playingField.get('numbPlanets'))
	planet_sample = random.choices(PLANETS, k=playingField.get('numbPlanets'))
	for i in field:
		print(planet_sample[i])
	
#Launch Phase ----------------------------------------------------------
	explore = input("Would you like to explore an available planet? y/n ")
	
	
	roll = input("roll dice? y/n ")
	if(roll == 'y'):
		print("You rolled a : ", roll_dice_6s())
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



