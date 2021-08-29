import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("im.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        '''
        #signal
        
        '''
        
        self.Pallet_Start_btn.clicked.connect(self.Pallet_Start)
        self.Pallet_End_btn.clicked.connect(self.Pallet_End)
        self.Depallet_Start_btn.clicked.connect(self.Depallet_Start)
        self.Depallet_End_btn.clicked.connect(self.Depallet_End)
    
    def Pallet_Start(self):
        print("Pallet Start")

    def Pallet_End(self):
        print("Pallet end")
    
    def Depallet_Start(self):
        print("Depallet Start")

    def Depallet_End(self):
        print("Depallet end")
    

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()