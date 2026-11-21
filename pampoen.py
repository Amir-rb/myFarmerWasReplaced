clear ()

_world_size = get_world_size() * get_world_size()
_pos = 0
_unsuccess_grown = []
_success_grown = 0




def plant_pumpkin():
	global _pos
	
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

	if _pos >= _world_size:
		_pos = 0
		
		while len(_unsuccess_grown) >= 1 :
			list = []
			
			for x, y in _unsuccess_grown:
				move_to(x, y)
				
				if get_entity_type() != Entities.Pumpkin:
					plant(Entities.Pumpkin)
					list.append((x,y))
				
				
				
				
				
			_unsuccess_grown = list
			
		
	
		move_to(0,0)
		harvest()
			
		
		
	
	
	plant_pumpkin()
		
	move(East)