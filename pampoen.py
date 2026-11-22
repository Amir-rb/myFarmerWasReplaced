clear ()

_world_size = get_world_size() * get_world_size()
_pos = 0
_unsuccess_grown = []
_row_count = 0


def do_row():
	global _pos
	global _row_count

	_row_count = 0
	
	for i in range(get_world_size()):
		
		if get_ground_type() != Grounds.soil:
			till()
		
		
		scan_block()
		plant(Entities.Pumpkin)
		
		_pos += 1	
		move(North)
		
	
		
def scan_block():
	global _unsuccess_grown 
	global _pos 
	
	
	if not (get_entity_type() != Entities.Dead_Pumpkin):
		# log pos
		_unsuccess_grown.append((get_pos_x(), get_pos_y()))
		
		
		


# moving around
def move_to(target_x, target_y):
	while get_pos_x() < target_x:
		move(East)
	while get_pos_x() > target_x:
		move(West)
		
	while get_pos_y() < target_y:
		move(North)
	while get_pos_y() > target_y:
		move(South)





while True:
	#pass through everything to plant then scan
	for i in range(get_world_size() * 2): # 2 full passes
		do_row()
		move(East)


	while True:
		list = []
	
		#unsuccess loop through and re plant unsuccess
		for x, y in _unsuccess_grown:
			move_to(x, y)
	
			if get_entity_type() != Entities.Pumpkin:
				plant(Entities.Pumpkin)
				list.append((x, y))
		
			_unsuccess_grown = list
		
		#debugging
		# print (_unsuccess_grown)
		# print(len(_unsuccess_grown))

		#check list empty and entity type is pumpkin
		if not _unsuccess_grown:

			#do a flip for timing
			for i in range(4): # keep it a 4 for timing
				do_a_flip()

			harvest() #harvest big
			move_to(0,0) #move to start
			break #exit the loop

