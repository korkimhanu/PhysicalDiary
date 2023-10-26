import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from UI.ui_Loby import Ui_MainWindow #로비 UI를 UI 디렉토리에서 import

class Loby_Window(QMainWindow, Ui_MainWindow):  #로비 화면 클래스 생성
    def __init__(self): #class 기본 인자 설정
        super(Loby_Window,self).__init__()
        self.setupUi(self)

app = QApplication(sys.argv)

window = Loby_Window() #Loby_window 클래스 변수 생성
window.setFixedSize(1080,720) #창 크기 1080*720으로 설정
window.show() #창 띄우기

app.exec() #앱 실행
