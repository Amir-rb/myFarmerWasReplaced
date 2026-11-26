# North and south on map greater than or equals in size
# south and west on the map less than or equals to in size

# harvest at (0,0)

#size = measure()

#swap(direction)

from Helper import *
from Movement import *

# move to (0,0)
move_to(0,0)

#defs





# main while area
list = []
#first planing 
for x in range(world_size):
    
    row = []
    for y in range(world_size):
        plant_cell(Entities.Cactus)
        
        row.append(measure())
        
        
        move(North)
        
    list.append(row)
    move(East)

#swapping
for a in range(world_size):
    n = len(list[a])
    for i in range(n -1):
        for j in range(n - i - 1):
            if list