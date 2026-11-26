# helper methods
def plant_cell(arr):
	harvest()
	plant(arr)

def is_even(n):
	return n % 2 == 0

def wait(n):
	for i in range(n):
		do_a_flip()

def Water():
	use_item(Items.Water)