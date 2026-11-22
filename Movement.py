def move_to(target_x, target_y):
	while get_pos_x() < target_x:
		move(East)
	while get_pos_x() > target_x:
		move(West)
		
	while get_pos_y() < target_y:
		move(North)
	while get_pos_y() > target_y:
		move(South)