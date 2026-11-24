#sunflower used for power
# planting like carrots or pumpkins
# > 10 harvest biggest one
# use measure() 

from Movement import move_to

clear()

#variables
_world_size = get_world_size()
_entity_list = []
_sorted_list = []


#plant first per row
def Plant_row():
    global _entity_list
    
    for i in range(_world_size):
        if get_ground_type() != Grounds.Soil:
            till()
        
        plant(Entities.Sunflower)
        
        #get entity value aka num petals
        x, y = get_pos_x(), get_pos_y()
        _entity_list.append((measure(), (x, y)))
        
        move(North)
        
def sort_list(list):
    #sort petal number
    n = len(list)
    for i in range(n - 1):
        
        swapped = False
        
        for j in range(n - i -1):
            if list[j][0] < list[j + 1][0]:
                list[j], list[j + 1] = list[j + 1], list[j]
                
                swapped = True
                
        if not swapped:
            break
            
    return list

#plant sunflowers
for row in range(_world_size * 1): #full field once
    Plant_row()
    move(East)

_sorted_list = sort_list(_entity_list)

for value, (x, y) in _sorted_list:

    move_to(x,y)
    harvest()

move_to(0,0)