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
from UI import ui_Loby


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

        self.diary_listTable.setItem(i, 0, item_title)
        self.diary_listTable.setItem(i, 1, item_date)

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

    weather_label = QLabel("날씨:")
    weather_input = QLineEdit()
    weather_input.setPlaceholderText("날씨를 입력해주세요")  # 디폴트 메시지 설정
    layout.addWidget(weather_label)
    layout.addWidget(weather_input)

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
        weather = weather_input.text()
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


def save_diary_to_file(self):
    with open(self.data_file, 'w') as file:
        for diary in self.diary_list:
            file.write(
                f'{diary["diary_id"]}|{diary["diary_title"]}|{diary["diary_weather"]}|{diary["diary_date"]}|{diary["diary_content"]}\n')

