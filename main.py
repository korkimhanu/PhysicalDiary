import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
#로비 UI를 UI 디렉토리에서 import
from UI import ui_Loby as Loby, ui_Diary as Diary, ui_Login as Login, ui_ProfileEditor as PE

class Loby_Window(QMainWindow, Loby.Ui_MainWindow):  #로비 화면 클래스 생성
    def __init__(self): #class 기본 인자 설정
        super(Loby_Window,self).__init__()
        self.setupUi(self)
        self.profileEditBtn.clicked.connect(self.switch_to_PE) #연결 필요함

    def switch_to_PE(self):
        # 로비 윈도우 인스턴스를 생성하고 보여줍니다.
        self.profileEd = ProfileE_window()  # Loby_Window 인스턴스 생성
        self.profileEd.show()
        self.close()

class ProfileE_window(QMainWindow,PE.Ui_Form):
    def __init__(self):
        super(ProfileE_window, self).__init__()
        self.setupUi(self)

class Diary_Window(QMainWindow,Diary.Ui_MainWindow):

    def __init__(self):
        super(Diary_Window,self).__init__()
        self.setupUi(self)

class Login_Window(QMainWindow, Login.Ui_Form):
    def __init__(self, parent=None):
        super(Login_Window, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_ed.clicked.connect(self.switch_to_loby)  # 버튼 클릭 시 동작을 연결합니다.

    def switch_to_loby(self):
        # 로비 윈도우 인스턴스를 생성하고 보여줍니다.
        self.loby_window = Loby_Window()  # Loby_Window 인스턴스 생성
        self.loby_window.show()
        self.close()


app = QApplication(sys.argv)

Lobywindow = Loby_Window() #Loby_window 클래스 변수 생성
Lobywindow.setFixedSize(1080,720) #창 크기 1080*720으로 설정
Diarywindow = Diary_Window()
Diarywindow.setFixedSize(1080,720)
Loginwindow = Login_Window()
Loginwindow.show() #창 띄우기



app.exec() #앱 실행
