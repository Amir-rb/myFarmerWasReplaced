#do trees with div (%) and is even

from Movement import move_to
from Helper import *

#variables
world_size = get_world_size()

# start procedure here
if get_ground_type() == Grounds.Grassland:
		clear()
else:
	move_to(0,0)


#functions
def plant_row(arr1, arr2):
	x = get_pos_x()
	
	for i in range(world_size):
		y = get_pos_y()
		
		if get_entity_type() == Entities.Grass:
			till()
		
		if is_even(x) == 0:
			if is_even(y) == 0:
				plant_cell(arr1)
				
			else:
				plant_cell(arr2)
				
		elif is_even(x) != 0:
			if is_even(y) != 0:
				plant_cell(arr1)
			else:
				plant_cell(arr2)
	
	
		move(North)





#first pass and plant
for i in range(world_size):
	plant_row(Entities.Tree, Entities.Bush)
	move(East)


# program loop
while True:
	move_to(0,0)

	for i in range(world_size):
		for j in range(world_size):
			
			entity = get_entity_type()
			
			# if not entity:
			# 	plant(Entities.Grass)
		
			plant_cell(entity)

			# Water() #water grounds
		
		
			move(North)
		
		move(East)