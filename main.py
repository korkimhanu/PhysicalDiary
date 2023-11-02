import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
#로비 UI를 UI 디렉토리에서 import
from UI import ui_Loby as Loby, ui_Diary as Diary, ui_Login as Login

class Loby_Window(QMainWindow, Loby.Ui_MainWindow):  #로비 화면 클래스 생성
    def __init__(self): #class 기본 인자 설정
        super(Loby_Window,self).__init__()
        self.setupUi(self)
class Diary_Window(QMainWindow,Diary.Ui_MainWindow):

    def __init__(self):
        super(Diary_Window,self).__init__()
        self.setupUi(self)

class Login_Window(QMainWindow,Login.Ui_Form):
    def __init__(self):
        super(Login_Window,self).__init__()
        self.setupUi(self)
app = QApplication(sys.argv)

Lobywindow = Loby_Window() #Loby_window 클래스 변수 생성
Lobywindow.setFixedSize(1080,720) #창 크기 1080*720으로 설정
Diarywindow = Diary_Window()
Diarywindow.setFixedSize(1080,720)
Loginwindow = Login_Window()
Loginwindow.show() #창 띄우기

app.exec() #앱 실행
