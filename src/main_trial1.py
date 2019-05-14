from map import map
from search import search
from robot import robot
from visualize import display

resolution = 10

M = map([11.1,10.1],resolution,(0.354/2),0.1)

obstacle_set, obstacle_list = M.obstacle_set_create()
# print(obstacle_set)

R = robot((0.354/2),4,5,M,resolution)
# print(R.rad)

Path = search([0,0],[-40,-40],M,R)

velocities , path = Path.A_star()
D = display(Path.start_position, Path.goal_position, M.x_min,M.y_min,M.x_max,M.y_max)
D.display_map(path,Path.visited_node,obstacle_list)




#M = map([11.1,10.1],resolution,(0.354/2),0.1)

#obstacle_set, obstacle_list = M.obstacle_set_create()
# print(obstacle_set)

R1 = robot((0.354/2),4,5,M,resolution)
# print(R.rad)

Path1 = search([3,3],[-40,-40],M,R1)

velocities1 , path1 = Path1.A_star()

D1 = display(Path1.start_position, Path1.goal_position, M.x_min,M.y_min,M.x_max,M.y_max)
D1.display_map(path1,Path1.visited_node,obstacle_list)




#M = map([11.1,10.1],resolution,(0.354/2),0.1)

# obstacle_set, obstacle_list = M.obstacle_set_create()
# print(obstacle_set)

R2 = robot((0.354/2),4,5,M,resolution)
# print(R.rad)

Path2 = search([5,5],[-40,-40],M,R2)

velocities2 , path2 = Path2.A_star()
D2 = display(Path2.start_position, Path2.goal_position, M.x_min,M.y_min,M.x_max,M.y_max)
D2.display_map(path2,Path2.visited_node,obstacle_list)
