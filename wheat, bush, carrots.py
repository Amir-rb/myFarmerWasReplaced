#clean map first
clear()
do_a_flip()


def wood():
	harvest()
	plant(Entities.Bush)
	# use_item(Items.Fertilizer)

	if can_harvest():
		harvest()
		plant(Entities.Bush)

	move(North)
	
def carrot_and_wheat():
	if get_ground_type() != Grounds.Grassland:  
		harvest()
		till()
		plant(Entities.Grass)
	else:
		harvest()
		till()
		plant(Entities.Carrot)
	
	move(North)  

def water_the_tile():
	if get_water() <= 0.5:
		use_item(Items.Water)

def is_even(num):
	return num % 2 == 0

#MAIN method
while True:
	# planing loop
	for i in range(get_world_size()):
		if i < (get_world_size()/2) and can_harvest():  
			wood()        
		elif can_harvest():
			carrot_and_wheat()
		else:
			pass
	move(East)
