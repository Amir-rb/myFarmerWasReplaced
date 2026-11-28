from Movement import move_to

clear()

#variables
_pos = 0
_unsuccess_grown = []

def do_row():
	for i in range(get_world_size()):
		
		if get_ground_type() != Grounds.soil:
			till()
		
		scan_block()
		plant(Entities.Pumpkin)
		move(North)

def scan_block():
	global _unsuccess_grown 
	global _pos 
	
	
	if not (get_entity_type() != Entities.Dead_Pumpkin):
		# log pos
		_unsuccess_grown.append((get_pos_x(), get_pos_y()))
		Water() # water

def Water():
	if get_water() < 0.5:
			use_item(Items.Water)


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
				# Water() # water if can
				plant(Entities.Pumpkin)
				list.append((x, y))
		
		_unsuccess_grown = list

		#check list empty and entity type is pumpkin
		if (not _unsuccess_grown) and (can_harvest()):

			#do a flip for timing
			for i in range(1): # keep it a 4 for timing / solved???? maybe just 1 for now
				do_a_flip()

			harvest() #harvest big
			move_to(0,0) #move to start
			break #exit the loop