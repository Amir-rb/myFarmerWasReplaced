# North and south on map greater than or equals in size
# south and west on the map less than or equals to in size

# harvest at (0,0)

#size = measure()

#swap(direction)

from Helper import *
from Movement import *

# move to (0,0)
move_to(0,0)

# main while area
#first planting 
while True:
	list = []
	
	for x in range(world_size):
		
		row = []
		for y in range(world_size):
			if get_ground_type() != Grounds.Soil:
				till()
			
			plant_cell(Entities.Cactus)
		
			# row.append(measure())
		
		
			move(North)
		
		# list.append(row)
		move(East)


	#sort row West => East
	for a in range(world_size):

		move_to(0, a)
	
		for i in range(world_size - 1):
			swapped = False
			for j in range(world_size - i - 1):
				if measure() > measure(East):
					swap(East)
					swapped = True
			
				move(East)
			if not swapped:
				break
		
			move_to(0,a)

	#sort South => north
	for a in range(world_size):
	
		move_to(a, 0)
	
		for i in range(world_size -1):
		
			swapped = False
		
			for j in range(world_size - i - 1):
				if measure() > measure(North):
					swap(North)
					swapped = True
				
				move(North)
		
			if not swapped:
				break
		
			move_to(a, 0)
		
	move_to(0,0)

	harvest()