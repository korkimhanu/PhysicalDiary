"""
 * Date: 2023년 11월 6일
 * Author: 조성진
 * Description: 일기장 GUI 테스트
 * Version: 1.1.0
"""
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QPushButton, QTextEdit, QLineEdit, QListWidget, QWidget
import os
from datetime import datetime

class DiaryManager:
    def __init__(self):
        self.diary_list = []
        self.data_file = os.path.join(os.path.dirname(__file__), '..', 'DB', 'diary_data.txt')

    def load_diary_from_file(self):
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
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

    def save_diary_to_file(self):
        with open(self.data_file, 'w') as file:
            for diary in self.diary_list:
                file.write(f'{diary["diary_id"]}|{diary["diary_title"]}|{diary["diary_weather"]}|{diary["diary_date"]}|{diary["diary_content"]}\n')

    def create_diary(self, _title, _weather, _content):
        if not self.diary_list:
            idx = 0
        else:
            idx = max(diary["diary_id"] for diary in self.diary_list) + 1
        date = datetime.now().strftime('%Y-%m-%d')
        self.diary_list.append(dict(
            diary_id=idx,
            diary_title=_title,
            diary_weather=_weather,
            diary_date=date,
            diary_content=_content
        ))
        self.save_diary_to_file()

class DiaryCreateDialog(QDialog):
    def __init__(self, diary_manager):
        super().__init__()
        self.diary_manager = diary_manager
        self.setWindowTitle("일기 작성하기")
        self.setGeometry(100, 100, 400, 300)
        self.layout = QVBoxLayout()
        self.init_ui()

    def init_ui(self):
        self.create_diary_title_input = QLineEdit("일기 제목을 입력하세요")
        self.create_diary_weather_input = QLineEdit("날씨를 입력하세요")
        self.create_diary_content_input = QTextEdit("일기 내용을 입력하세요")
        self.create_diary_button = QPushButton("일기 작성 완료")
        self.create_diary_button.clicked.connect(self.create_diary)
        self.layout.addWidget(self.create_diary_title_input)
        self.layout.addWidget(self.create_diary_weather_input)
        self.layout.addWidget(self.create_diary_content_input)
        self.layout.addWidget(self.create_diary_button)
        self.setLayout(self.layout)

    def create_diary(self):
        title = self.create_diary_title_input.text()
        weather = self.create_diary_weather_input.text()
        content = self.create_diary_content_input.toPlainText()
        self.diary_manager.create_diary(title, weather, content)
        self.accept()  # Close the dialog after creating the diary

class DiaryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.diary_manager = DiaryManager()
        self.setWindowTitle("일기 프로그램")
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QWidget()
        self.layout = QVBoxLayout()
        self.init_ui()

    def init_ui(self):
        self.menu_label = QLabel("메뉴를 선택하세요:")
        self.layout.addWidget(self.menu_label)

        self.menu_list = QListWidget()
        self.menu_list.addItems(["일기 작성하기", "일기 목록 보기", "프로그램 종료"])
        self.layout.addWidget(self.menu_list)

        self.result_label = QTextEdit()
        self.layout.addWidget(self.result_label)

        self.menu_list.itemClicked.connect(self.handle_menu_selection)

        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def handle_menu_selection(self, item):
        selected_text = item.text()
        if selected_text == "일기 작성하기":
            self.show_create_diary_dialog()
        elif selected_text == "일기 목록 보기":
            self.show_diary_list()
        elif selected_text == "프로그램 종료":
            self.close()

    def show_create_diary_dialog(self):
        create_dialog = DiaryCreateDialog(self.diary_manager)
        create_dialog.exec_()  # Show the dialog and wait for it to be closed
        # After the dialog is closed, you can update the UI as needed

    def show_diary_list(self):
        self.result_label.setText("일기 목록")
        self.result_label.clear()
        for diary in self.diary_manager.diary_list:
            self.result_label.append(f'ID: {diary["diary_id"]} | 제목: {diary["diary_title"]}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DiaryApp()
    window.show()
    window.diary_manager.load_diary_from_file()
    sys.exit(app.exec())
