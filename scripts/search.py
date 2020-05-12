from robot import robot
from map import maps
import queue
import numpy as np
import sys
import os

class search:
    def __init__(self,start_position,goal_position,map_supplied : maps,robot_supplied : robot,s_no,initial_theta = 0):

        self.robot = robot_supplied
        self.start_position = start_position
        self.goal_position = goal_position
        self.initial_theta = initial_theta
        self.serial = s_no

        self.map = map_supplied

        self.nodes_list = []
        self.nodes_list.append([self.start_position])
        self.start_position_theta = [self.start_position[0],self.start_position[1],self.initial_theta]

        self.q = queue.PriorityQueue()
        self.q.put([0, self.start_position_theta])

        self.node_check_set = set([])            #visited nodes
        self.node_check_set.add(str(self.start_position))

        self.node_info_dict = self.node_info_list(self.map.x_min,self.map.y_min,self.map.x_max,self.map.y_max)
        self.node_info_dict[str(self.start_position)] = 0

        self.node_info_parent_dict = {}
        self.node_info_velocities = {}

        self.visited_node = []
        self.is_a_vaid_input = self.valid_start_goal()
        self.goal_reached = False
        self.goal_obtained = []

        # self.current_node = self.start_position

    ## to check if the node is visited
    def is_visited_check(self,node):
        return str(node) in self.node_check_set


    def node_info_list(self,min_x,min_y,max_x,max_y):
        loc = []
        for i in range(int(min_x),int(max_x),1):
            for j in range(int(min_y),int(max_y),1):
                loc.append([i,j])
        distance = {}
        for node in loc:
            distance[str(node)] = 9999999
        return distance


    def valid_start_goal(self):
        status = True
        if self.map.is_obstacle(self.start_position) or self.map.is_obstacle(self.goal_position):
            status = False
            sys.exit('either the start_position or your goal position is in obstacle space, enter a valid input')
        return status


    def cost_to_go(self,current_node):

        x1 = current_node[0]
        y1 = current_node[0]

        x2 = self.goal_position[0]
        y2 = self.goal_position[0]

        d = np.sqrt((x2-x1)**2 + (y2-y1)**2)

        return d

    def A_star(self):

        iter1 = 0

        while not self.q.empty() and self.is_a_vaid_input == True:# and :

            node = self.q.get()      ##[0, [15, 20, 0]] --> [cost, [x,y,theta]]
            # print('node in while',node)

            x_new = node[1][0]
            y_new = node[1][1]
            theta_new = node[1][2]
            node_pos = [node[1][0],node[1][1]]

            iter1+=1
            # print(iter1)

            if [int(node[1][0]),int(node[1][1])] == self.goal_position:
                print('goal reached',iter1)
                self.goal_obtained = [node[1][0],node[1][1]]
                self.goal_reached = True
                break
            explored_nodes = self.robot.action_set(x_new,y_new,theta_new)

            # action = np.array([new_x,new_y,new_theta,new_cost,action[0],action[1]])
            for action in explored_nodes:

                # print(action)  ##[1.98308572 3.1073315  1.72727273 0.19       0.         5.        ]
                action_pos = [action[0],action[1]]
                action_theta = action[2]
                action_cost = action[3]
                action_velocities = [action[4],action[5],action_cost]

                if self.is_visited_check(action_pos) == False:

                    if self.map.is_obstacle(action_pos) == False:
                        self.node_check_set.add(str([int(action_pos[0]),int(action_pos[1])])) ## marked as visited --> added to visited nodes ## str([d(act[0]),d(act[1])])
                        self.visited_node.append(action_pos)
                        # print(str([int(action_pos[0]),int(action_pos[1])]))
                        cost = action_cost + self.node_info_dict[str([int(action_pos[0]),int(action_pos[1])])] + self.cost_to_go(action_pos)
                        self.node_info_dict[str([int(action_pos[0]),int(action_pos[1])])] = cost
                        self.q.put([cost,[action[0],action[1],action_theta]])
                        self.node_info_parent_dict[str(action_pos)] = node_pos#--> parent is updated to the node info
                        # displayArray =updateAndDisplay(displayArray,[int(action[0]/displayRes),int(action[1]/displayRes)],3)
                        self.node_info_velocities[str(action_pos)] = action_velocities


                else:
                    if self.map.is_obstacle(action_pos) == False:
                        temp = action_cost + self.node_info_dict[str(node_pos)]
                        if self.node_info_dict[str(action_pos)] > temp:
                            self.node_info_dict[str(action_pos)] = temp + self.cost_to_go(action_pos)
                            self.node_info_parent_dict[str(action_pos)] = node_pos           #--> parent is updated to the node info
                            self.node_info_velocities[str(action_pos)] = action_velocities

        node_path = []
        node_velocities_list = []

        if self.is_a_vaid_input == True:
            if self.goal_reached:

                node_path.append(self.goal_obtained)
                parent = self.node_info_parent_dict[str(self.goal_obtained)]

                while parent != self.start_position:
                    node_velocities_list.append(self.node_info_velocities[str(parent)])
                    parent =  self.node_info_parent_dict[str(parent)]
                    node_path.append(parent)
                node_path.reverse()
                node_velocities_list.reverse()
                    # displayArray =updateAndDisplay(displayArray,[int(parent[0]/displayRes),int(parent[1]/displayRes)],5)

                # self.display_map(self.start_position,goal_obtained,node_path,self.visited_node,obs_list)

            else:
                print('goal not reached')
        else:
            print('enter a valid input')

        node_vel_arr = np.asarray(node_velocities_list)
        node_path_arr = np.asarray(node_path)


        # with open('node_path.txt', 'w') as node_path_file:
        #
        #     for i in node_path_arr:
        #         t = np.empty([1,2])
        #         t[0:,] = i
        #         np.savetxt(node_path_file,t,delimiter='\t')
        #

        velocity_list = []
        for velocity in node_vel_arr:
            # print(velocity[0],velocity[1])
            lin_x = (self.robot.rad/2)*(velocity[0] + velocity[1])
            lin_y = (self.robot.rad/2)*(velocity[0] + velocity[1])
            lin_z = 0

            ang_x = 0
            ang_y = 0
            ang_z = (self.robot.rad/self.robot.len)*(velocity[0]- velocity[1])

            velocity_list.append([lin_x,lin_y,lin_z,ang_x,ang_y,ang_z])


        velocity_array = np.asarray(velocity_list)

        base_name = 'converted_velocities'
        suffix = '.txt'

        fname = os.path.join(base_name + str(self.serial) + suffix)

        # print(fname)

        with open(fname, 'w') as velocities_file:

            for i in velocity_array:
                p = np.empty([1,6])
                p[0:,] = i
                np.savetxt(velocities_file,p,delimiter='\t')


        return velocity_list,node_path


