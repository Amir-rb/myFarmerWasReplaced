clear ()

_world_size = get_world_size() * get_world_size()
_pos = 0
_unsuccess_grown = 0
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
		_unsuccess_grown += 1



while True:
	
	
	if _pos >= _world_size:
		_pos = 0
		
		if _unsuccess_grown == 0:
			harvest()
			
		_unsuccess_grown = 0
		
	
	
	plant_pumpkin()
		
	move(East)
