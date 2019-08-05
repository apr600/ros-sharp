#!/usr/bin/env python

import rospy
import numpy as np
import matplotlib.pyplot as plt
from point_stamped_sample.msg import VR_dist
class VR_dist:
    ''' 
    Subscribes to the VR dist topic and constantly plots the distribution for the 
    ergodic controller
    '''
    
    def __init__(self):
        rospy.init_node('vr_distr', anonymous=True)
        self.distr_sub = rospy.Subscriber('/vr_dist', VR_dist, self.update_dist)

        self.nx = 10
        self.ny = 10
        self.dist = np.zeros((self.nx, self.ny))
        self.im = plt.imshow(data)        

    def update_dist(self, arr):
        self.dist = arr
        self.im.set_data(self.dist)
        plt.draw()


if __name__ == '__main__':
    x = VR_dist()
    rospy.spin()
        
