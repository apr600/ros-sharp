#!/usr/bin/env python

import rospy
import numpy
from geometry_msgs.msg import PointStamped

    
def moveToPos():
	# initialize node
	rospy.init_node('moveToPos', anonymous = True)

	#### Setup MouseToJoy Publisher 
   	moveToPosPublisher = rospy.Publisher("/pos", PointStamped, queue_size = 5)
	rate = rospy.Rate(10) # 10hz
	msg = PointStamped()

        pos_x = 0.0
	pos_y = 0.0
        
	while not rospy.is_shutdown():
		#### Initialize PointStamped msg every loop
                msg.header.frame_id = '/pos'
                msg.header.stamp = rospy.Time.now()
                
		msg.point.x = 0.0
		msg.point.y = 0.0
                msg.point.z = 6.0

                ### Get New pos position and update message ###
                pos_x, pos_y = move_drone(pos_x, pos_y)
                msg.point.x = pos_x
                msg.point.y = pos_y	

		#### Publish msg
		#rospy.loginfo([pos_x, pos_y])
		rospy.loginfo(msg)
		moveToPosPublisher.publish(msg)
		rate.sleep()

def move_drone(x,y):
    if 0 <= x < 0.9 and 0 <= y < 0.9:
        xnew = x+0.1
        ynew = y+0.1
    
    else:
        xnew = 0.0
        ynew = 0.0
    return xnew, ynew


if __name__ == '__main__':
	moveToPos()
