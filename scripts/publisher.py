#!/usr/bin/env python3
# above command need to be mentioned in every python scripts when using with ROS

#importing rospy to use ROS with python client
import rospy
from turtlesim.msg import Pose
#importing the LaserScan data from the LaserSensor attached to the turtlebot.
#We will subscribe to this laserscan data to build our obstacle avoidance algorithm
from sensor_msgs.msg import LaserScan
# We import the Twist topic from the geometry_msgs to publish our messages to the turtlebot
from geometry_msgs.msg import Twist
# import main_4
import numpy as np
import glob
import os
import main


# def callback(msg):
#
# #we access the ranges data from the from LaserScan and check if there is any obstable withing the distance of 0.5 meters
# global move

res = 10
# ROBOT_INITIAL_POSE="-x 5 -y 2" roslaunch planning sru.launch

list_of = []


# path = '/home/catkin_ws/src/planning/scripts'

# print(path)

l_o_l = []

# for infile in glob.glob('*.txt'):
#     #print('inside for')
#
#     list_of = []

# all_files = os.listdir(".")
#
#
# print(all_files)
#
# txt_files = filter(lambda x: x[-4:] == '.txt', all_files)

# print(txt_files)
# txt_files.sort()
#
# print('i am here')


for infile in sorted(glob.glob('*.txt')):
#
#     list_of = []
# for infile in txt_files:
#     # if
#     print(infile)

    with open(infile) as f:
        for line in f:
            inner_list = [elt.strip() for elt in line.split('\t')]
            # in alternative, if you need to use the file content as numbers
            # inner_list = [int(elt.strip()) for elt in line.split(',')]
            list_of.append(inner_list)


    l_o_l.append(np.asarray(list_of).astype(float))

# print(l_o_l)

rospy.init_node('rob',anonymous = True)

# pub1 = rospy.Publisher('/robot1/mobile_base/commands/velocity', Twist, queue_size=10)

pub_vel_1 = rospy.Publisher('/robot1/mobile_base/commands/velocity', Twist, queue_size=1)
pub_vel_2 = rospy.Publisher('/robot2/mobile_base/commands/velocity', Twist, queue_size=1)
pub_vel_3 = rospy.Publisher('/robot3/mobile_base/commands/velocity', Twist, queue_size=1)
pub_vel_4 = rospy.Publisher('/robot4/mobile_base/commands/velocity', Twist, queue_size=1)
pub_vel_5 = rospy.Publisher('/robot5/mobile_base/commands/velocity', Twist, queue_size=1)
pub_vel = (pub_vel_1, pub_vel_2, pub_vel_3, pub_vel_4, pub_vel_5)

move1 = Twist()
move2 = Twist()
move3 = Twist()
move4 = Twist()
move5 = Twist()

vel1 = l_o_l[0]
vel2 = l_o_l[1]
vel3 = l_o_l[2]
vel4 = l_o_l[3]
vel5 = l_o_l[4]


# print(vel1[0][0])

move1.linear.x = vel1[0][0]
move1.linear.y = vel1[0][1]
move1.linear.z =  0
move1.angular.x = 0
move1.angular.y = 0
move1.angular.z = vel1[0][5]


move2.linear.x = vel2[0][0]
move2.linear.y = vel2[0][1]
move2.linear.z =  0
move2.angular.x = 0
move2.angular.y = 0
move2.angular.z = vel2[0][5]

move3.linear.x = vel3[0][0]
move3.linear.y = vel3[0][1]
move3.linear.z =  0
move3.angular.x = 0
move3.angular.y = 0
move3.angular.z = vel3[0][5]

move4.linear.x = vel4[0][0]
move4.linear.y = vel4[0][1]
move4.linear.z =  0
move4.angular.x = 0
move4.angular.y = 0
move4.angular.z = vel4[0][5]

move5.linear.x = vel5[0][0]
move5.linear.y = vel5[0][1]
move5.linear.z =  0
move5.angular.x = 0
move5.angular.y = 0
move5.angular.z = vel5[0][5]

pub_vel_1.publish(move1)
pub_vel_2.publish(move2)
pub_vel_3.publish(move3)
pub_vel_4.publish(move4)
pub_vel_5.publish(move5)

# rate = rospy.Rate(1)

# start_time = rospy.Time.now()
# duration = rospy.Duration(1)
# end_time = start_time + duration
# rospy.Duration(0.5)


# while rospy.Time.now() < end_time:
#
# 	print(current_pos.x,current_pos.y)
#
# 	# print("count", count)
# 	count +=1
# 	# print("I'm doing this:", move)
# 	pub.publish(move)
# 	#t1 = rospy.Time().now().to_sec()
# 	#print("T1", t1)
# 	rate.sleep()

# rospy.spin()


# for lis in l_o_l:
#
# 	list_arr = np.asarray(lis)
#
# 	for vel in list_arr:
#
# 		move.linear.x = vel[0]
# 		move.linear.y = vel[1]
# 		move.linear.z =  0
# 		move.angular.x = 0
# 		move.angular.y = 0
# 		move.angular.z = vel[5]



# for i in range(num_of_robots):
# 	print(i)
#
# with open('/home/srujan/catkin_ws/src/planning/scripts/converted_velocities.txt') as f:
#     for line in f:
#         inner_list = [elt.strip() for elt in line.split('\t')]
#         # in alternative, if you need to use the file content as numbers
#         # inner_list = [int(elt.strip()) for elt in line.split(',')]
#         list_of.append(inner_list)
#
#
# list_arr = np.asarray(list_of).astype(float)


# with open('node_path.txt') as f:
#     for line in f:
#         inner_list = [elt.strip() for elt in line.split('\t')]
#         # in alternative, if you need to use the file content as numbers
#         # inner_list = [int(elt.strip()) for elt in line.split(',')]
#         node_list.append(inner_list)
#
# node_list.pop(0)
# node_arr = np.asarray(node_list).astype(float)

#we create a node called listener
# rospy.init_node('robot1',anonymous = True)
# rospy.init_node('robot2',anonymous = True)
# rospy.init_node('robot3',anonymous = True)



#we create a publisher to publish on to /cmd_vel_mux/input/teleop which is equivalent to geometry_msgs/Twist for turtlebot

# pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size = 10)

# pub1 = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
# pub2 = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
# pub3 = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)

# move = Twist()
# rate = rospy.Rate(1)
# current_pos = Pose()
#
# def mover():
# 	count = 0
# 	for vel in list_arr:
#
# 		move.linear.x = vel[0]
# 		move.linear.y = vel[1]
# 		move.linear.z =  0
# 		move.angular.x = 0
# 		move.angular.y = 0
# 		move.angular.z = vel[5]
#
#
#
# 		print('publishing')
#
# 		start_time = rospy.Time.now()
# 		duration = rospy.Duration(1)
# 		end_time = start_time + duration
# 		# rospy.Duration(0.5)
#
#
#
# 		while rospy.Time.now() < end_time:
#
# 			print(current_pos.x,current_pos.y)
#
# 			# print("count", count)
# 			count +=1
# 			# print("I'm doing this:", move)
# 			pub.publish(move)
# 			#t1 = rospy.Time().now().to_sec()
# 			#print("T1", t1)
# 			rate.sleep()
#
#
# mover()
# rospy.spin()

