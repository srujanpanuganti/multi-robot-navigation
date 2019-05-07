import numpy as np
import matplotlib.pyplot as plt

class display:

    def __init__(self,start_position,goal_position,min_x,min_y,max_x,max_y):

        self.start_position = start_position
        self.goal_position = goal_position
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y


    def display_map(self,node_path,visited_node,obs_list):

        node_path_array = np.asarray(node_path)
        # print('node path',node_path_array.shape)

        display_arrary = np.asarray(obs_list)
        visited_node_array = np.asarray(visited_node)
        plt.figure(figsize=(111,101))

        plt.plot(display_arrary[:,0],display_arrary[:,1],'y+', label = 'obstacles')
        plt.plot(self.start_position[0],self.start_position[1],'bo',label = 'start position')
        plt.plot(self.goal_position[0],self.goal_position[1],'go',label = 'goal position')
        plt.plot(node_path_array[:,0],node_path_array[:,1],'ro',label = 'path')
        plt.plot(visited_node_array[:,0],visited_node_array[:,1],'b+', label = 'explored nodes')

        plt.xlim(self.min_x,self.max_x)
        plt.ylim(self.min_y,self.max_y)
        plt.grid(True)
        plt.legend()
        plt.show()
