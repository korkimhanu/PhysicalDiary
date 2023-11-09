import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
# 로비 UI를 UI 디렉토리에서 import
from UI import ui_Loby as Loby, ui_Diary as Diary, ui_Login as Login
from UI.ui_ProfileEditor import ProfileApp

class Loby_Window(QMainWindow, Loby.Ui_MainWindow):
    def __init__(self):
        super(Loby_Window, self).__init__()
        self.setupUi(self)
        self.profileEditBtn.clicked.connect(self.switch_to_PE)

    def switch_to_PE(self):
        self.profileEd = ProfileApp()
        self.profileEd.show()
       # self.close()

class Diary_Window(QMainWindow, Diary.Ui_MainWindow):
    def __init__(self):
        super(Diary_Window, self).__init__()
        self.setupUi(self)

class Login_Window(QMainWindow, Login.Ui_Form):
    def __init__(self, parent=None):
        super(Login_Window, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_ed.clicked.connect(self.switch_to_loby)

    def switch_to_loby(self):
        self.loby_window = Loby_Window()
        self.loby_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    Lobywindow = Loby_Window()
    Lobywindow.setFixedSize(1080, 720)
    Diarywindow = Diary_Window()
    Diarywindow.setFixedSize(1080, 720)
    Loginwindow = Login_Window()
    Lobywindow.show()

    app.exec()