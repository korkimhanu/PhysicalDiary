# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'LobyFhSKFO.ui'
#
# Created by: Qt User Interface Compiler version 6.6.0
#
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QRect, Qt
from PySide6.QtGui import QFont, QCursor
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
                               QPushButton, QStatusBar, QTableView, QWidget,
                               QCalendarWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1072, 726)

        # 메인 윈도우의 중앙에 배치될 위젯
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # 배경 레이블
        self.background = QLabel(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 1071, 691))
        self.background.setStyleSheet(u"background-color:white;")

        # "Physical" 레이블
        self.Physical = QLabel(self.centralwidget)
        self.Physical.setObjectName(u"Physical")
        self.Physical.setGeometry(QRect(0, 0, 241, 61))
        font = QFont()
        font.setFamilies([u"\ucda9\ubd81\ub300\uc9c1\uc9c0\uccb4"])  # 폰트 설정
        font.setPointSize(36)
        self.Physical.setFont(font)

        # "Diary" 레이블
        self.Diary = QLabel(self.centralwidget)
        self.Diary.setObjectName(u"Diary")
        self.Diary.setGeometry(QRect(90, 40, 241, 61))
        self.Diary.setFont(font)

        # 일지 리스트를 표시할 테이블 뷰
        self.diary_listTable = QTableView(self.centralwidget)
        self.diary_listTable.setObjectName(u"diary_listTable")
        self.diary_listTable.setGeometry(QRect(390, 0, 681, 681))

        # 사용자 이름을 표시할 레이블
        self.user_name = QLabel(self.centralwidget)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setGeometry(QRect(70, 310, 241, 61))
        font1 = QFont()
        font1.setFamilies([u"\ud55c\ucef4 \ub9d0\ub791\ub9d0\ub791 Bold"])  # 폰트 설정
        font1.setPointSize(18)
        font1.setBold(True)
        self.user_name.setFont(font1)
        self.user_name.setAlignment(Qt.AlignCenter)

        # 프로필 편집 버튼
        self.profileEditBtn = QPushButton(self.centralwidget)
        self.profileEditBtn.setObjectName(u"profileEditBtn")
        self.profileEditBtn.setGeometry(QRect(90, 390, 191, 41))
        self.profileEditBtn.setCursor(QCursor(Qt.PointingHandCursor))

        # 캘린더 위젯
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(0, 450, 391, 221))

        # 프로필 사진을 표시할 레이블
        self.profilePortrait = QLabel(self.centralwidget)
        self.profilePortrait.setObjectName(u"profilePortrait")
        self.profilePortrait.setGeometry(QRect(140, 190, 101, 101))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1072, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        # 각 위젯에 대한 텍스트 설정
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        # self.background에는 텍스트 설정이 필요하지 않음
        self.Physical.setText(QCoreApplication.translate("MainWindow", u"Physical", None))
        self.Diary.setText(QCoreApplication.translate("MainWindow", u"Diary", None))
        self.user_name.setText(QCoreApplication.translate("MainWindow", u"\uc758 \uc6b4\ub3d9\uc77c\uc9c0", None))
        self.profileEditBtn.setText(
            QCoreApplication.translate("MainWindow", u"\ud504\ub85c\ud544 \uc218\uc815\ud558\uae30", None))
        # self.profilePortrait에는 텍스트 설정이 필요하지 않음
    # retranslateUi
