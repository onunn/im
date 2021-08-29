#!/usr/bin/env python
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import rospy

form_class = uic.loadUiType("im.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)


        self.chk_1.clicked.connect(self.chkFunction)
        self.chk_2.clicked.connect(self.chkFunction)

        self.Pallet_Start_btn.clicked.connect(self.Pallet_Start)
        self.Pallet_End_btn.clicked.connect(self.Pallet_End)
        self.Depallet_Start_btn.clicked.connect(self.Depallet_Start)
        self.Depallet_End_btn.clicked.connect(self.Depallet_End)



        self.palletizing_pub_ = rospy.Publisher("/launch_manager", String, queue_size=10)
        self.depalletizing_pub_ = rospy.Publisher("/launch_manager", String, queue_size=10)

    def chkFunction(self) :
        if self.chk_1.isChecked() : 
            print("chk_1 isChecked")



        elif self.chk_2.isChecked() : 
            print("chk_2 isChecked")

    def Pallet_Start(self) :
        #self.palletizing_pub_.publish('pallet start')
        print('pallet start')
        
    def Pallet_End(self) :
        #self.palletizing_pub_.publish('pallet end')
        print('pallet End')

        
    def Depallet_Start(self) :
        #self.depalletizing_pub_.publish('depallet start')
        print('Depallet start')


    def Depallet_End(self) :
        #self.depalletizing_pub_.publish('depallet end')
        print('Depallet End')

 

if __name__ == "__main__" :
    app = QApplication(sys.argv) 

    myWindow = WindowClass() 

    myWindow.show()

    app.exec_()