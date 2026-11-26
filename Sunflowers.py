#sunflower used for power
# planting like carrots or pumpkins
# > 10 harvest biggest one
# use measure() 

from Movement import move_to
from Helper import *

clear()

#variables
_world_size = get_world_size()

# other vars
_min_size = 7


#plant first per row
def Plant_row():
	for i in range(_world_size):
		if get_ground_type() != Grounds.Soil:
			till()
		
		use_item(Items.Water)
		plant_cell(Entities.Sunflower)

		#get entity value aka num petals and cords
		x, y, value = get_pos_x(), get_pos_y(), measure()
		
		# get target key
		target_key = value - _min_size

		if target_key in _entity_dic:
			_entity_dic[target_key].append((x,y))
			

		move(North)
		

while True:
	# set var after every loop
	_entity_dic = {}
	for i in range(9):
		_entity_dic[i] = []

	
	#plant sunflowers  
	for row in range(_world_size * 1): #full field once
		Plant_row()
		move(East)

	# wait for everything to grow
	wait(1)

	# move through from most to least
	for key in range(8, -1, -1):
		list = _entity_dic[key]
	
		for (x,y) in  list:
			move_to(x, y)
			harvest()

	move_to(0,0)