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
        

    def start_qrpallet(self):

        uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
        mapping_pkg_path = rospkg.RosPack().get_path('calc_pallet') 
        print(mapping_pkg_path)
        
        self.palletizingLaunch = roslaunch.parent.ROSLaunchParent(uuid, [mapping_pkg_path + '/launch/QR_pallet.launch']) 
        self.palletizingLaunch.start()
        self.palletizingStarted = True
        
    def start_alphapallet(self):

        uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
        mapping_pkg_path = rospkg.RosPack().get_path('calc_pallet') 
        print(mapping_pkg_path)
        
        self.palletizingLaunch = roslaunch.parent.ROSLaunchParent(uuid, [mapping_pkg_path + '/launch/Alphabet_pallet.launch']) 
        self.palletizingLaunch.start()
        self.palletizingStarted = True

    def stop_qrpallet(self):

        if self.palletizingLaunch != None:
            self.palletizingLaunch.shutdown()
            self.palletizingLaunch = None
        self.palletizingStarted = False

    def stop_alphapallet(self):

        if self.palletizingLaunch != None:
            self.palletizingLaunch.shutdown()
            self.palletizingLaunch = None
        self.palletizingStarted = False

    def LaunchMangerCB(self, msg):
        if msg.data == 'qrpallet start':
            print('qrpallet start')
            if self.palletizingStarted == False:
                self.start_qrpallet()

        elif msg.data == 'alphapallet start':
            print('alphapallet start')
            if self.palletizingStarted == False:
                self.start_alphapallet()

        elif msg.data == 'qrapallet start':
            print('pallet end')
            self.stop_qrpallet()

        elif msg.data == 'qrapallet end':
            print('pallet end')
            self.stop_alphapallet()



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
