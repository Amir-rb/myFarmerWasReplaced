harvest()

world_size = get_world_size()

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
		
move_to(0, 0)