import numpy as np
import matplotlib.pyplot as plt


class maps:
    def __init__(self,map_size,resolution,robot_radius,clearance):
        self.map_size = map_size
        self.res = resolution
        self.robot_radius = robot_radius + clearance


        self.x_offset = map_size[0]/2 * self.res
        self.y_offset = map_size[1]/2 * self.res


        self.x_offset = map_size[0]/2 * self.res
        self.y_offset = map_size[1]/2 * self.res

        self.x_max = map_size[0] * self.res - self.x_offset
        self.y_max = map_size[1] * self.res - self.y_offset

        self.x_min = -self.x_offset
        self.y_min = -self.y_offset

        self.obstacle_list = []
        self.obs_set = set([])



        rect1 = self.rect_offset(np.multiply([[1.4995 - robot_radius,9.1 + robot_radius],[3.0985 + robot_radius,7.501 - robot_radius]],self.res))

        rect2 = self.rect_offset(np.multiply([[4.38 - robot_radius,4.98 + robot_radius],[5.29 + robot_radius,3.15 - robot_radius]], self.res))

        rect3 = self.rect_offset(np.multiply([[4.74 - robot_radius,1.87 + robot_radius],[7.48 + robot_radius,0.35 - robot_radius]], self.res))

        rect4 = self.rect_offset(np.multiply([[5.29 - robot_radius,3.41 + robot_radius],[7.12 + robot_radius,2.65 - robot_radius]], self.res))

        rect5 = self.rect_offset(np.multiply([[6.85 - robot_radius,0.35 + robot_radius],[11.1,0]], self.res))

        rect6 = self.rect_offset(np.multiply([[7.44 - robot_radius,6.97 + robot_radius],[11.1,6.21 - robot_radius]], self.res))

        rect7 = self.rect_offset(np.multiply([[7.79 - robot_radius,0.93 + robot_radius],[8.96 + robot_radius,0.35]], self.res))

        rect8 = self.rect_offset(np.multiply([[7.845 - robot_radius,3.84 + robot_radius],[9.365 + robot_radius,2.67 - robot_radius]], self.res))

        rect9 = self.rect_offset(np.multiply([[8.32 - robot_radius,10.1],[9.18 + robot_radius,8.27 - robot_radius]], self.res))

        rect10 = self.rect_offset(np.multiply([[9.27 - robot_radius,1.11 + robot_radius],[11.1,0.35]], self.res))

        rect11 = self.rect_offset(np.multiply([[9.83 - robot_radius,10.1],[10.26 + robot_radius,9.19 - robot_radius]], self.res))

        rect12 = self.rect_offset(np.multiply([[10.19 - robot_radius,4.485 + robot_radius],[11.1,3.625 - robot_radius]], self.res))

        rect13 = self.rect_offset(np.multiply([[10.52 - robot_radius,5.655 + robot_radius],[11.1,4.485]], self.res))

        rect14 = self.rect_offset(np.multiply([[10.52 - robot_radius,2.9525 + robot_radius],[11.1,1.7825 - robot_radius]], self.res))

        c1 = self.cir_offset(np.multiply([3.9,9.6], self.res))
        c1_rad = 0.405* self.res + robot_radius

        # print(c1)
        # print(cir_offset(c1))

        c2 = self.cir_offset(np.multiply([4.38,7.36], self.res))
        c2_rad = 0.405* self.res + robot_radius

        c3 = self.cir_offset(np.multiply([4.38,2.74], self.res))
        c3_rad = 0.405* self.res + robot_radius

        c4 = self.cir_offset(np.multiply([3.9,0.405], self.res))
        c4_rad = 0.405* self.res + robot_radius

        c5 = self.cir_offset(np.multiply([1.4995,8.3005], self.res))
        c5_rad = 0.7995* self.res + robot_radius

        c6 = self.cir_offset(np.multiply([3.0985,8.3005], self.res))
        c6_rad = 0.7995* self.res + robot_radius

        grid = np.multiply([map_size[0],map_size[1]], self.res)

        self.rectangles = [rect1,rect2,rect3,rect4,rect5,rect6,rect7,rect8,rect9,rect10,rect11,rect12,rect13,rect14]
        # self.rectangles = [rect2,rect3,rect7,rect10,rect11,rect14]
        self.circles = [[c1,c1_rad],[c2,c2_rad],[c3,c3_rad],[c4,c4_rad],[c5,c5_rad],[c6,c6_rad]]
        # self.circles = [[c2,c2_rad],[c4,c4_rad],[c6,c6_rad]]


    def is_point_in_rect(self,points,rect_coordinates):        # points = [0,0]    ## rect1 = [[1,4],[4,2]]
        x = points[0]
        y = points[1]

        a = rect_coordinates[0][0]
        b = rect_coordinates[0][1]

        c = rect_coordinates[1][0]
        d = rect_coordinates[1][1]

        if x >= a and x <= c and y <= b and y >= d:
            return True
        else:
            return False

    def rect_offset(self,rect_coords):           ## rect1 = [[1,4],[4,2]]

        x1 =  rect_coords[0][0] - self.x_offset
        x2 =  rect_coords[1][0] - self.x_offset

        y1 =  rect_coords[0][1] - self.y_offset
        y2 =  rect_coords[1][1] - self.y_offset

        return [[x1,y1],[x2,y2]]


    def is_point_in_circle(self,points, circle_center,radius):    ## points = [0,0] ## radi = 5   ##circle_cent = [5,5]
        x = points[0]
        y = points[1]

        h = circle_center[0]
        k = circle_center[1]

        if (x-h)**2 + (y-k)**2 <= radius**2:
            return True
        else:
            return False


    def cir_offset(self,cir_cent):       #circle_cent = [5,5]

        x = cir_cent[0] - self.x_offset
        y = cir_cent[1] - self.y_offset

        return [x,y]

    def is_border(self,point,robot_radius):       # point = [1,2]  ## robot_radius = 0.354/2 *res

        status = False
        # print(robot_radius)
        # print(point)

        x = point[0]
        y = point[1]

        if x <= robot_radius - self.x_offset or x >= self.x_max-robot_radius or y <= robot_radius - self.y_offset or y >= self.y_max-robot_radius:
            status = True

        return status

    def is_obstacle(self,point):

        status = False
        in_rect = False
        in_cir = False

        for rect in self.rectangles:
            if self.is_point_in_rect(point,rect):
                in_rect = True

        for cir in self.circles:
            if self.is_point_in_circle(point,cir[0],cir[1]):
                in_cir = True

        if (in_rect or in_cir) == True:
            status = True
        return status


    def add_obstacle(self,x,y,width,breadth):
        ### assuming every obstcle as a rectangular obstacle
        w = width
        b = breadth
        new_rect = self.rect_offset(np.multiply([[(x-b/2) - self.robot_radius,(y+w/2)+ self.robot_radius],[(x+b/2) + self.robot_radius,(y-w/2)- self.robot_radius]],self.res))
        self.rectangles.append(new_rect)

    def update_map(self,M):
        ## M = {1, x, y, sigma, w, b, t}
        if M[0] == 1:
            self.add_obstacle(M[1],M[2],M[4],M[5])

    def obstacle_set_create(self):
        # print(int(grid[0]))
        for i in range(int(self.x_min),int(self.x_max),1):
            for j in range(int(self.y_min),int(self.y_max),1):
                point = [i,j]
                # print(point)

                if self.is_obstacle(point): #or is_point_in_circle(point,circ[0],circ[1]):
                    self.obs_set.add(str(point))
                    self.obstacle_list.append(point)

        return self.obs_set,self.obstacle_list
    # obtained_set = obstacle_set_create(rectangles,circles)

    # def is_obstacle_set(point):
    #     return str(point) in self.obst_set
