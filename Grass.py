from Helper import *
from Movement import *

#vars
world_size = get_world_size()

while True:
	move_to(0,0)
	
	for x in range(world_size):
		for y in range(world_size):
			plant_cell(Entities.Grass)
			move(North)
			
		move(East)