"""
 * Date: 2023년 11월 6일
 * Author: 조성진
 * Description: 일기장 GUI 테스트
 * Version: 1.1.0
"""
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QLineEdit, QListWidget
import os
from datetime import datetime

class DiaryManager:
    def __init__(self):
        self.diary_list = []
        self.data_file = os.path.join(os.path.dirname(__file__), 'diary_data.txt')

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

    def append_to_diary(self, _id, _content):
        for diary in self.diary_list:
            if diary["diary_id"] == _id:
                diary["diary_content"] += "\n" + _content
                self.save_diary_to_file()
                return True
        return False

    def read_diary(self, _id):
        for diary in self.diary_list:
            if diary["diary_id"] == _id:
                return diary
        return None

    def update_diary(self, _id, _content):
        for diary in self.diary_list:
            if diary["diary_id"] == _id:
                diary["diary_content"] = _content
                self.save_diary_to_file()
                return True
        return False

    def delete_diary(self, _id):
        for diary in self.diary_list:
            if diary["diary_id"] == _id:
                self.diary_list.remove(diary)
                self.save_diary_to_file()
                return True
        return False

class DiaryApp(QWidget):
    def __init__(self):
        super().__init()
        self.diary_manager = DiaryManager()
        self.setWindowTitle("일기 프로그램")
        self.setGeometry(100, 100, 800, 600)
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

        self.setLayout(self.layout)

    def handle_menu_selection(self, item):
        selected_text = item.text()
        if selected_text == "일기 작성하기":
            self.show_create_diary_form()
        elif selected_text == "일기 목록 보기":
            self.show_diary_list()
        elif selected_text == "프로그램 종료":
            self.close()

    def show_create_diary_form(self):
        self.result_label.setText("일기 작성하기")
        self.create_diary_title_input = QLineEdit("일기 제목을 입력하세요")
        self.create_diary_weather_input = QLineEdit("날씨를 입력하세요")
        self.create_diary_content_input = QTextEdit("일기 내용을 입력하세요")
        self.create_diary_button = QPushButton("일기 작성 완료")
        self.create_diary_button.clicked.connect(self.create_diary)
        self.layout.addWidget(self.create_diary_title_input)
        self.layout.addWidget(self.create_diary_weather_input)
        self.layout.addWidget(self.create_diary_content_input)
        self.layout.addWidget(self.create_diary_button)

    def create_diary(self):
        title = self.create_diary_title_input.text()
        weather = self.create_diary_weather_input.text()
        content = self.create_diary_content_input.toPlainText()
        self.diary_manager.create_diary(title, weather, content)
        self.result_label.setText("일기가 작성되었습니다.")

        # 일기 작성이 완료되면 입력 창을 제거
        self.layout.removeWidget(self.create_diary_title_input)
        self.layout.removeWidget(self.create_diary_weather_input)
        self.layout.removeWidget(self.create_diary_content_input)
        self.layout.removeWidget(self.create_diary_button)
        self.create_diary_title_input.deleteLater()
        self.create_diary_weather_input.deleteLater()
        self.create_diary_content_input.deleteLater()
        self.create_diary_button.deleteLater()

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
