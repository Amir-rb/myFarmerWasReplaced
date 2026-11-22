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


# def move_to(target_x, target_y):
#     	while get_pos_x() < target_x:
# 		move(East)
# 	while get_pos_x() > target_x:
# 		move(West)
		
# 	while get_pos_y() < target_y:
# 		move(North)
# 	while get_pos_y() > target_y:
# 		move(South)
		
# move_to(0, 0)