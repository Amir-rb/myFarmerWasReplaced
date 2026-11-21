



while True:
	for i in range(get_world_size()):
		
		
		change_hat(Hats.Green_Hat)
		
		if can_harvest():
			harvest() 
		elif not can_harvest():
			till()
		
		move(North)

	move(East)

