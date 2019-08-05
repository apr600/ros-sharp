#!/usr/bin/env python

import rospy
import numpy as np
from geometry_msgs.msg import PointStamped, PoseArray, Pose, Point, Quaternion

class MoveSwarm:
    
    def __init__(self):
        # initialize node
	rospy.init_node('moveSwarm', anonymous = True)

        # Initialize/set vars
        self.num_drones = 3
        self.init_pos = np.random.random((self.num_drones, 2))*.25
        self.swarm_pos = self.init_pos
        # Initialize Publishers

        self.swarm_pub = rospy.Publisher('/swarm_pos', PoseArray, queue_size=1)
        self.rate = rospy.Rate(10)
        self.msg = PoseArray()

    def move_drone(self, x, y, init_pos):
        if 0 <= x < 0.9 and 0 <= y < 0.9:
            xnew = x+0.1
            ynew = y+0.1

        else:
            xnew = init_pos[0]
            ynew = init_pos[1]
        return [xnew, ynew]
            
    def update_swarm_pos(self):
        # Update swarm positions
        for i in range(self.num_drones): 
            self.swarm_pos[i] = self.move_drone(self.swarm_pos[i,0], self.swarm_pos[i,0],...
                                           self.init_pos[i])
        #### Update PoseArray msg
        for i in range(self.num_drones):
            pose = Pose()
            pose.position.x = self.swarm_pos[i,0]
            pose.position.y = self.swarm_pos[i,1]
            pose.position.z = 6.0

            pose.orientation.x = 0
            pose.orientation.y = 0
            pose.orientation.z = 0
            pose.orientation.w = 1
            self.msg.poses.append(pose)

        self.msg.header.frame_id = '/swarm_pos'
        self.msg.header.stamp = rospy.Time.now()
        # Publish Message
        rospy.loginfo(self.msg)
        self.swarm_pub.publish(self.msg)
        self.rate.sleep()
    
if __name__ == '__main__':
    swarm = MoveSwarm()
    while not rospy.is_shutdown():
        swarm.update_swarm_pos()    
