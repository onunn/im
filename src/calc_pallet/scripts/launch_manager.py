#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import roslaunch
import rospkg
from std_msgs.msg import String

class LaunchManager:

    def __init__(self):

        self.palletizingLaunch = None
        self.palletizingStarted = False

        self.depalletizingLaunch = None
        self.depalletizingStarted = False
        

    def startpallet(self):

        uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
        mapping_pkg_path = rospkg.RosPack().get_path('collect_db') 
        print(mapping_pkg_path)
        
        self.palletizingLaunch = roslaunch.parent.ROSLaunchParent(uuid, [mapping_pkg_path + '/launch/collect_test.launch']) 
        self.palletizingLaunch.start()
        self.palletizingStarted = True
        

    def stoppallet(self):

        if self.palletizingLaunch != None:
            self.palletizingLaunch.shutdown()
            self.palletizingLaunch = None
        self.palletizingStarted = False


    def startdepallet(self):

        uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
        mapping_pkg_path = rospkg.RosPack().get_path('collect_db') 
        print(mapping_pkg_path)
        
        self.depalletizingLaunch = roslaunch.parent.ROSLaunchParent(uuid, [mapping_pkg_path + '/launch/collect_db.launch']) 
        self.depalletizingLaunch.start()
        self.depalletizingStarted = True
        

    def stopdepallet(self):

        if self.depalletizingLaunch != None:
            self.depalletizingLaunch.shutdown()
            self.depalletizingLaunch = None
        self.depalletizingStarted = False


    def LaunchMangerCB(self, msg):
        if msg.data == 'pallet start':
            print('pallet start')
            if self.palletizingStarted == False:
                self.startpallet()

        elif msg.data == 'pallet end':
            print('pallet end')
            self.stoppallet()

        elif msg.data == 'depallet start':
            print('depallet start')
            if self.depalletizingStarted == False:
                self.startdepallet()

        elif msg.data == 'depallet end':
            print('depallet end')
            self.stopdepallet()


# Start the node
if __name__ == '__main__':
    rospy.init_node("launch_manager")#, disable_signals=True)
    launchManager = LaunchManager()

    # rospy.spin()

    while not rospy.is_shutdown():
        # wait data
        try:
            msg = rospy.wait_for_message('/launch_manager', String, 1.0)
            launchManager.LaunchMangerCB(msg)
        except:
            pass
