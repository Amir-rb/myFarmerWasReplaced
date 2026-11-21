clear()
num = 0

while True:
	harvest()
	till()
	
	if get_ground_type() == Grounds.Soil:
		plant(Entities.Carrot)
		move(North)
	elif get_ground_type() == Grounds.Grassland:
		plant(Entities.Grass)
		move(North)
	
	num += 1
	
	if num == get_world_size():
		move(East)
		num = 0