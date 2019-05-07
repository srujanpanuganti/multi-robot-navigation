#!/usr/bin/env python
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

# def callback(msg):
#
# #we access the ranges data from the from LaserScan and check if there is any obstable withing the distance of 0.5 meters
# global move

res = 10
# ROBOT_INITIAL_POSE="-x 5 -y 2" roslaunch planning sru.launch

list_of = []

with open('/home/srujan/catkin_ws/src/planning/scripts/converted_velocities.txt') as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split('\t')]
        # in alternative, if you need to use the file content as numbers
        # inner_list = [int(elt.strip()) for elt in line.split(',')]
        list_of.append(inner_list)


list_arr = np.asarray(list_of).astype(float)


with open('node_path.txt') as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split('\t')]
        # in alternative, if you need to use the file content as numbers
        # inner_list = [int(elt.strip()) for elt in line.split(',')]
        node_list.append(inner_list)

node_list.pop(0)
node_arr = np.asarray(node_list).astype(float)

#we create a node called listener
rospy.init_node('listener',anonymous = True)

#we create a publisher to publish on to /cmd_vel_mux/input/teleop which is equivalent to geometry_msgs/Twist for turtlebot
# pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size = 10)

pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)

move = Twist()
rate = rospy.Rate(1)
current_pos = Pose()

def mover():
	count = 0
	for vel in list_arr:

		move.linear.x = vel[0]
		move.linear.y = vel[1]
		move.linear.z =  0
		move.angular.x = 0
		move.angular.y = 0
		move.angular.z = vel[5]



		print('publishing')

		start_time = rospy.Time.now()
		duration = rospy.Duration(1)
		end_time = start_time + duration
		# rospy.Duration(0.5)



		while rospy.Time.now() < end_time:

			print(current_pos.x,current_pos.y)

			# print("count", count)
			count +=1
			# print("I'm doing this:", move)
			pub.publish(move)
			#t1 = rospy.Time().now().to_sec()
			#print("T1", t1)
			rate.sleep()


mover()
rospy.spin()

