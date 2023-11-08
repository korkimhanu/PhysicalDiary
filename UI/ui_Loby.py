# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LobyHWActR.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableView, QWidget,QTableWidget,QTextEdit,
    QTableWidgetItem,QVBoxLayout,QInputDialog,QDialog,QLineEdit)
import os
from datetime import datetime
from subFunctions import food_calorie_calculator as fcc, crawling

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1072, 726)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.background = QLabel(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 1071, 691))
        self.background.setStyleSheet(u"background-color:white;")

        self.Physical = QLabel(self.centralwidget)
        self.Physical.setObjectName(u"Physical")
        self.Physical.setGeometry(QRect(0, 0, 241, 61))
        font = QFont()
        font.setFamilies([u"\ucda9\ubd81\ub300\uc9c1\uc9c0\uccb4"])
        font.setPointSize(36)

        self.Physical.setFont(font)

        self.Diary = QLabel(self.centralwidget)
        self.Diary.setObjectName(u"Diary")
        self.Diary.setGeometry(QRect(90, 40, 241, 61))
        self.Diary.setFont(font)

        self.diary_listTable = QTableWidget(self.centralwidget)
        self.diary_listTable.setObjectName(u"diary_listTable")
        self.diary_listTable.setColumnCount(3)
        self.diary_listTable.setHorizontalHeaderLabels(["제목", "날짜","날씨"])
        weather_column_index = 2  # Index starts at 0, so if "날씨" is the third column, it will be index 2.
        self.diary_listTable.setColumnWidth(weather_column_index, 280)
        self.diary_listTable.cellClicked.connect(self.show_diary)
        self.diary_listTable.setGeometry(QRect(390, 0, 500, 681))

        # button_layout = QVBoxLayout()
        # self.create_button = QPushButton("일기 작성하기")
        # self.create_button.clicked.connect(self.create_diary)
        # button_layout.addWidget(self.create_button)
        #
        # self.modify_button = QPushButton("일기 수정하기")
        # self.modify_button.clicked.connect(self.modify_diary)
        # button_layout.addWidget(self.modify_button)
        #
        # self.delete_button = QPushButton("일기 삭제하기")
        # self.delete_button.clicked.connect(self.delete_diary)
        # button_layout.addWidget(self.delete_button)
        #
        # self.load_diary_button = QPushButton("일기 불러오기")
        # self.load_diary_button.clicked.connect(self.load_diary)
        # button_layout.addWidget(self.load_diary_button)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(910, -1, 160, 681))
        self.btnLayouts = QVBoxLayout(self.verticalLayoutWidget)
        self.btnLayouts.setObjectName(u"btnLayouts")
        self.btnLayouts.setContentsMargins(0, 0, 0, 0)

        self.writeDiaryBtn = QPushButton("일기 작성하기",self.verticalLayoutWidget)
        self.writeDiaryBtn.clicked.connect(self.create_diary)
        self.writeDiaryBtn.setObjectName(u"writeDiaryBtn")

        self.btnLayouts.addWidget(self.writeDiaryBtn)

        self.EditDiaryBtn = QPushButton(u"일기 수정하기",self.verticalLayoutWidget)
        self.EditDiaryBtn.clicked.connect(self.modify_diary)
        self.EditDiaryBtn.setObjectName(u"EditDiaryBtn")

        self.btnLayouts.addWidget(self.EditDiaryBtn)

        self.deleteDiaryBtn = QPushButton(u"일기 삭제하기",self.verticalLayoutWidget)
        self.deleteDiaryBtn.clicked.connect(self.delete_diary)
        self.deleteDiaryBtn.setObjectName(u"deleteDiaryBtn")

        self.btnLayouts.addWidget(self.deleteDiaryBtn)

        self.loadDiaryBtn = QPushButton( u"일기 불러오기", self.verticalLayoutWidget)
        self.loadDiaryBtn.clicked.connect(self.load_diary)
        self.loadDiaryBtn.setObjectName(u"loadDiaryBtn")

        self.btnLayouts.addWidget(self.loadDiaryBtn)

        self.user_name = QLabel(self.centralwidget)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setGeometry(QRect(70, 310, 241, 61))
        font1 = QFont()
        font1.setFamilies([u"\ud55c\ucef4 \ub9d0\ub791\ub9d0\ub791 Bold"])
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setHintingPreference(QFont.PreferDefaultHinting)
        self.user_name.setFont(font1)
        self.user_name.setFocusPolicy(Qt.NoFocus)
        self.user_name.setLayoutDirection(Qt.LeftToRight)
        self.user_name.setAlignment(Qt.AlignCenter)

        self.profileEditBtn = QPushButton(self.centralwidget)
        self.profileEditBtn.setObjectName(u"profileEditBtn")
        self.profileEditBtn.setGeometry(QRect(90, 390, 191, 41))
        self.profileEditBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(0, 450, 391, 221))

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

        data_dir = os.path.join(os.path.dirname(__file__), '..', 'DB')
        self.data_file = os.path.join(data_dir, 'diary_data.txt')

        self.diary_list = []
        self.load_diary_from_file()
        self.current_diary_id = None
        self.diary_text = QTextEdit()

        self.show_diary_list()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.background.setText("")
        self.Physical.setText(QCoreApplication.translate("MainWindow", u"Physical", None))
        self.Diary.setText(QCoreApplication.translate("MainWindow", u"Diary", None))
        self.user_name.setText(QCoreApplication.translate("MainWindow", u"\uc758 \uc6b4\ub3d9\uc77c\uc9c0", None))
        self.profileEditBtn.setText(QCoreApplication.translate("MainWindow", u"\ud504\ub85c\ud544 \uc218\uc815\ud558\uae30", None))
        self.profilePortrait.setText("")
    # retranslateUi

    def load_diary_from_file(self):
        try:
            with open(self.data_file, 'r') as file:
                for line in file:
                    parts = line.strip().split('|')
                    if len(parts) == 5:
                        _id, _title, _weather, _date, _content = parts
                        _id = int(_id)
                        self.diary_list.append(dict(
                            diary_id=_id,
                            diary_title=_title,
                            diary_weather=_weather,
                            diary_date=_date,
                            diary_content=_content
                        ))
        except FileNotFoundError:
            self.diary_list = []

    def show_diary_list(self):
        self.diary_listTable.setRowCount(len(self.diary_list))
        for i, diary in enumerate(self.diary_list):
            item_title = QTableWidgetItem(diary["diary_title"])
            item_title.setFlags(item_title.flags() ^ Qt.ItemIsEditable)
            item_date = QTableWidgetItem(diary["diary_date"])
            item_date.setFlags(item_date.flags() ^ Qt.ItemIsEditable)
            item_weather = QTableWidgetItem(diary["diary_weather"])
            item_weather.setFlags(item_weather.flags() ^ Qt.ItemIsEditable)
            # item_calories = QTableWidgetItem(fcc.calculate_calories(diary["diary_content"]))
            # item_calories.setFlags(item_calories.flags() ^ Qt.ItemIsEditable) #로비에서 칼로리 표시기능(현재 안됨, 구현 요구됨)


            self.diary_listTable.setItem(i, 0, item_title)
            self.diary_listTable.setItem(i, 1, item_date)
            # self.diary_listTable.setItem(i,2,item_calories)
            self.diary_listTable.setItem(i, 2, item_weather)

            self.diary_listTable.setSelectionBehavior(QTableWidget.SelectRows)

    def show_diary(self, row, col):
        self.current_diary_id = self.diary_list[row]["diary_id"]
        self.diary_text.setPlainText(self.diary_list[row]["diary_content"])

    def create_diary(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("일기 작성하기")
        dialog.setGeometry(100, 100, 400, 300)  # 크기 설정

        layout = QVBoxLayout()

        title_label = QLabel("제목:")
        title_input = QLineEdit()
        title_input.setPlaceholderText("제목을 입력해주세요")  # 디폴트 메시지 설정
        layout.addWidget(title_label)
        layout.addWidget(title_input)

        weather_label = QLabel("날씨:"+"\n"+crawling.scrapeWeatherFromNaver())
        layout.addWidget(weather_label)

        content_label = QLabel("내용:")
        content_input = QTextEdit()
        content_input.setPlaceholderText("내용을 입력해주세요")  # 디폴트 메시지 설정
        layout.addWidget(content_label)
        layout.addWidget(content_input)

        ok_button = QPushButton("확인")
        ok_button.clicked.connect(dialog.accept)
        layout.addWidget(ok_button)

        dialog.setLayout(layout)

        if dialog.exec() == QDialog.Accepted:
            title = title_input.text()
            weather = crawling.scrapeWeatherFromNaver()
            content = content_input.toPlainText()

            if title and weather and content:
                if not self.diary_list:
                    idx = 0
                else:
                    idx = max(diary["diary_id"] for diary in self.diary_list) + 1
                date = datetime.now().strftime('%Y-%m-%d')
                self.diary_list.append(dict(
                    diary_id=idx,
                    diary_title=title,
                    diary_weather=weather,
                    diary_date=date,
                    diary_content=content
                ))
                self.save_diary_to_file()
                self.show_diary_list()

    def modify_diary(self):
        if self.current_diary_id is not None:
            content, ok = QInputDialog.getMultiLineText(self, "일기 수정하기", "내용:", self.diary_text.toPlainText())
            if ok:
                for diary in self.diary_list:
                    if diary["diary_id"] == self.current_diary_id:
                        diary["diary_content"] = content
                        self.save_diary_to_file()
                        self.show_diary_list()

    def delete_diary(self):
        if self.current_diary_id is not None:
            for diary in self.diary_list:
                if diary["diary_id"] == self.current_diary_id:
                    self.diary_list.remove(diary)
                    self.save_diary_to_file()
                    self.show_diary_list()

    def load_diary(self):
        if self.current_diary_id is not None:
            diary_data = {}
            for diary in self.diary_list:
                if diary["diary_id"] == self.current_diary_id:
                    diary_data = diary
            if diary_data:
                dialog = QDialog(self)
                dialog.setWindowTitle("View Diary")

                layout = QVBoxLayout()

                title_label = QLabel(f"Title: {diary_data['diary_title']}")
                layout.addWidget(title_label)

                weather_label = QLabel(f"Weather: {diary_data['diary_weather']}")
                layout.addWidget(weather_label)

                date_label = QLabel(f"Date: {diary_data['diary_date']}")
                layout.addWidget(date_label)
                diary_content = diary_data['diary_content']
                total_calories = fcc.calculate_calories(diary_content)

                calories_label = QLabel(f"총 칼로리: {total_calories}kcal")
                layout.addWidget(calories_label)


                text_edit = QTextEdit(dialog)
                text_edit.setPlainText(diary_content)
                layout.addWidget(text_edit)

                dialog.setLayout(layout)
                dialog.exec()

    def save_diary_to_file(self):
        with open(self.data_file, 'w') as file:
            for diary in self.diary_list:
                file.write(
                    f'{diary[u"diary_id"]}|{diary[u"diary_title"]}|{diary[u"diary_weather"]}|{diary[u"diary_date"]}|{diary[u"diary_content"]}\n')



