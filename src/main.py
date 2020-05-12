from map import maps
from search import search
from robot import robot
from visualize import display

resolution = 10

velocity_lists = []

M = maps([11.1,10.1],resolution,(0.354/2),0.1)

obstacle_set, obstacle_list = M.obstacle_set_create()
# print(obstacle_set)

R1 = robot((0.354/2),4,5,M,resolution)
# print(R.rad)

print('generating path for robot1..')

# Path1 = search([-20,-10],[-40,-40],M,R1)
Path1 = search([-40,20],[0,40],M,R1,1)

velocities1 , path1 = Path1.A_star()
D1 = display(Path1.start_position, Path1.goal_position, M.x_min,M.y_min,M.x_max,M.y_max)

# velocity_lists.append(velocities1)

# D1.display_map(path1,Path1.visited_node,obstacle_list)



R2 = robot((0.354/2),4,5,M,resolution)

print('generating path for robot2..')

# Path2 = search([0,20],[-25,-10],M,R2)
Path2 = search([20,40],[50,35],M,R2,2)

velocities2 , path2 = Path2.A_star()

D2 = display(Path2.start_position, Path2.goal_position, M.x_min,M.y_min,M.x_max,M.y_max)
# D2.display_map(path2,Path2.visited_node,obstacle_list)

# velocity_lists.append(velocities2)


R3 = robot((0.354/2),4,5,M,resolution)

print('generating path for robot3..')

# Path3 = search([10,-10],[25,25],M,R3)
Path3 = search([10,0],[40,-30],M,R3,3)

velocities3 , path3 = Path3.A_star()
D3 = display(Path3.start_position, Path3.goal_position, M.x_min,M.y_min,M.x_max,M.y_max)
# D3.display_map(path3,Path3.visited_node,obstacle_list)

# velocity_lists.append(velocities3)


R4 = robot((0.354/2),4,5,M,resolution)

print('generating path for robot4..')

# Path4 = search([20,0],[0,40],M,R4)
Path4 = search([-40,-40],[20,-10],M,R4,4)

velocities4 , path4 = Path4.A_star()
D4 = display(Path4.start_position, Path4.goal_position, M.x_min,M.y_min,M.x_max,M.y_max)
# D4.display_map(path4,Path4.visited_node,obstacle_list)

# velocity_lists.append(velocities4)

R5 = robot((0.354/2),4,5,M,resolution)

print('generating path for robot5..')

# Path5 = search([-45,-10],[-30,20],M,R5)
Path5 = search([20,-20],[45,-20],M,R5,5)

velocities5 , path5 = Path5.A_star()
D5 = display(Path5.start_position, Path5.goal_position, M.x_min,M.y_min,M.x_max,M.y_max)
# D5.display_map(path5,Path5.visited_node,obstacle_list)

# velocity_lists.append(velocities5)

# print(velocity_lists)

# print('generated paths for all robots')
