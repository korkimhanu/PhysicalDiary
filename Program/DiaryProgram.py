"""
 * Date: 2023년 11월 8일
 * Author: 박병규, 이대규, 조성진
 * Description: 일기장
 * Version: 3.0
"""
import os
import sys
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QWidget, QTextEdit, QInputDialog, QDialog, QLabel, QLineEdit
from PySide6.QtCore import Qt
from food_calorie_calculator import calculate_calories

class DiaryApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # 경로 설정
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'DB')
        self.data_file = os.path.join(data_dir, 'diary_data.txt')

        self.diary_list = []
        self.load_diary_from_file()

        self.setWindowTitle("일기장 프로그램")
        self.setGeometry(100, 100, 800, 500)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # 위젯을 감싸는 수평 레이아웃
        horizontal_layout = QHBoxLayout()

        # 왼쪽에 일기 목록을 추가
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["제목", "날짜"])
        self.table_widget.cellClicked.connect(self.show_diary)
        horizontal_layout.addWidget(self.table_widget)

        # 오른쪽에 버튼들을 포함한 수직 레이아웃
        button_layout = QVBoxLayout()
        self.create_button = QPushButton("일기 작성하기")
        self.create_button.clicked.connect(self.create_diary)
        button_layout.addWidget(self.create_button)

        self.modify_button = QPushButton("일기 수정하기")
        self.modify_button.clicked.connect(self.modify_diary)
        button_layout.addWidget(self.modify_button)

        self.delete_button = QPushButton("일기 삭제하기")
        self.delete_button.clicked.connect(self.delete_diary)
        button_layout.addWidget(self.delete_button)

        self.load_diary_button = QPushButton("일기 불러오기")
        self.load_diary_button.clicked.connect(self.load_diary)
        button_layout.addWidget(self.load_diary_button)

        self.calculate_calories_button = QPushButton("칼로리 계산하기")
        self.calculate_calories_button.clicked.connect(self.calculate_calories)
        button_layout.addWidget(self.calculate_calories_button)

        horizontal_layout.addLayout(button_layout)
        self.central_widget.setLayout(horizontal_layout)

        self.current_diary_id = None
        self.diary_text = QTextEdit()

        self.show_diary_list()

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

                text_edit = QTextEdit(dialog)
                text_edit.setPlainText(diary_data['diary_content'])
                layout.addWidget(text_edit)

                dialog.setLayout(layout)
                dialog.exec()

    def show_diary(self, row, col):
        self.current_diary_id = self.diary_list[row]["diary_id"]
        self.diary_text.setPlainText(self.diary_list[row]["diary_content"])

    def show_diary_list(self):
        self.table_widget.setRowCount(len(self.diary_list))
        for i, diary in enumerate(self.diary_list):
            item_title = QTableWidgetItem(diary["diary_title"])
            item_title.setFlags(item_title.flags() ^ Qt.ItemIsEditable)
            item_date = QTableWidgetItem(diary["diary_date"])
            item_date.setFlags(item_date.flags() ^ Qt.ItemIsEditable)

            self.table_widget.setItem(i, 0, item_title)
            self.table_widget.setItem(i, 1, item_date)

            self.table_widget.setSelectionBehavior(QTableWidget.SelectRows)

    def calculate_calories(self):
        if self.current_diary_id is not None:
            diary_data = {}
            for diary in self.diary_list:
                if diary["diary_id"] == self.current_diary_id:
                    diary_data = diary

            if diary_data:
                diary_content = diary_data['diary_content']
                total_calories = calculate_calories(diary_content)
                dialog = QDialog(self)
                dialog.setWindowTitle("칼로리 계산 결과")

                layout = QVBoxLayout()

                calories_label = QLabel(f"총 칼로리: {total_calories}kcal")
                layout.addWidget(calories_label)

                text_edit = QTextEdit(dialog)
                text_edit.setPlainText(diary_content)
                layout.addWidget(text_edit)

                dialog.setLayout(layout)
                dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DiaryApp()
    window.show()
    sys.exit(app.exec_())
