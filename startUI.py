import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("im.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)


        self.chk_1.stateChanged.connect(self.chkFunction)
        self.chk_2.stateChanged.connect(self.chkFunction)


        self.pallet_start.clicked.connect(self.STR1)
        self.pallet_end.clicked.connect(self.STR2)
        self.depallet_start.clicked.connect(self.STR3)
        self.depalletizing_end.clicked.connect(self.STR4)


        self.palletizing_pub_ = rospy.Publisher("/launch_manager", String, queue_size=10)
        self.depalletizing_pub_ = rospy.Publisher("/launch_manager", String, queue_size=10)


    
    def chkFunction(self) :
        #CheckBox는 여러개가 선택될 수 있기 때문에 elif를 사용하지 않습니다.
        if self.chk_1.isChecked() : 
            print("chk_1 isChecked")



        elif self.chk_2.isChecked() : 
            print("chk_2 isChecked")

    def STR1(self) :
        self.palletizing_pub_.publish('pallet start')

        
    def STR2(self) :
        self.palletizing_pub_.publish('pallet end')

        
    def STR3(self) :
        self.depalletizing_pub_.publish('depallet start')


    def STR4(self) :
        self.depalletizing_pub_.publish('depallet end')



if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()