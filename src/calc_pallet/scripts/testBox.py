#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt16MultiArray 

import sys

def main(args):
    rospy.init_node('testBox', anonymous=True)
    pub = rospy.Publisher('/box_position', UInt16MultiArray, queue_size = 10)
    r = rospy.Rate(500)

    listData = [[[8,4],[8,4]],[[8,4],[8,4]],[[8,4],[8,4]]]

    while not rospy.is_shutdown():
        for i in range(len(listData)):
            for j in range(len(listData[i])):

                pubData = UInt16MultiArray(data=listData[i][j])
                pub.publish(pubData)
        r.sleep()

if __name__ == "__main__":
    main(sys.argv)
