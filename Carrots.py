from Movement import move_to

clear()


for i in range(get_world_size()):
	for j in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			harvest()
			till()
			plant(Entities.Carrot)
		move(North)

	move(East)

while True:
	for i in range(get_world_size()):
		
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
			
		
			
		if (get_ground_type() == Grounds.Soil):
			plant(Entities.Carrot)

		move(North)
	
	move(East)

