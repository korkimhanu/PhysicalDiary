import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QLineEdit, QSpinBox, QRadioButton, QMessageBox
from PySide6.QtGui import QPixmap
from PIL import Image
from PySide6 import QtCore
import json

class ProfileApp(QMainWindow):
    def __init__(self):
        super(ProfileApp, self).__init__()

        self.setWindowTitle("프로필")
        self.setGeometry(100, 100, 500, 500)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        # Input fields for name and age
        self.name_label = QLabel("이름:")
        self.layout.addWidget(self.name_label)
        self.name_input = QLineEdit(self)
        self.layout.addWidget(self.name_input)

        self.age_label = QLabel("나이:")
        self.layout.addWidget(self.age_label)
        self.age_input = QSpinBox(self)
        self.layout.addWidget(self.age_input)

        # 성별 선택을 위한 라디오 버튼 그룹
        self.gender_label = QLabel("성별:")
        self.layout.addWidget(self.gender_label)
        self.gender_radio_group = []
        self.male_radio = QRadioButton("남자", self)
        self.female_radio = QRadioButton("여자", self)
        self.other_radio = QRadioButton("그 외", self)
        self.gender_radio_group.extend([self.male_radio, self.female_radio, self.other_radio])
        self.layout.addWidget(self.male_radio)
        self.layout.addWidget(self.female_radio)
        self.layout.addWidget(self.other_radio)

        # 프로필 이미지 표시 레이블
        self.profile_label = QLabel(self)
        self.layout.addWidget(self.profile_label)

        self.central_widget.setLayout(self.layout)

        # 업로드 버튼 추가
        self.upload_button = QPushButton("프로필 이미지 업로드", self)
        self.layout.addWidget(self.upload_button)
        self.upload_button.clicked.connect(self.upload_profile_image)

        # 저장 버튼 추가
        self.save_button = QPushButton("프로필 저장", self)
        self.layout.addWidget(self.save_button)
        self.save_button.clicked.connect(self.save_profile_data)

        # Create a Person object to store the data
        self.person = Person()

        # Load profile data when the application starts
        self.load_profile_data()

    def save_profile_data(self):
        # 사용자가 입력한 정보를 Person 객체에 저장
        name = self.name_input.text()
        age = self.age_input.value()

        # 선택된 성별을 가져오기
        selected_gender = ""
        for radio in self.gender_radio_group:
            if radio.isChecked():
                selected_gender = radio.text()
                break

        self.person.set_info(name, selected_gender, age)

        # 프로필 이미지 파일 경로 추적
        pixmap = self.profile_label.pixmap()
        if pixmap is not None:
            image_path = os.path.join("../PhysicalDiary/DB/profile_image", "profile_image.png")  # 파일 이름을 원하는 이름으로 변경
            pixmap.toImage().save(image_path)  # 이미지 저장
        else:
            image_path = ""

        # Person 객체의 정보와 이미지 파일 경로를 JSON 파일에 저장
        profile_data = {
            "person": self.person.to_dict(),
            "image_path": image_path
        }
        with open("../PhysicalDiary/DB/profile_data.json", "w") as file:
            json.dump(profile_data, file)

        # 저장이 완료되었다는 메시지 박스 표시
        QMessageBox.information(self, "저장 완료", "프로필 정보가 성공적으로 저장되었습니다.")

    def load_profile_data(self):
        try:
            with open("../PhysicalDiary/profile_data.json", "r") as file:
                data = json.load(file)
                person_data = data.get("person", {})
                image_path = data.get("image_path", "")
                self.person.from_dict(person_data)

                # 프로필 이미지를 QLabel에 표시
                if image_path and os.path.exists(image_path):
                    pixmap = QPixmap(image_path)
                    self.profile_label.setPixmap(pixmap)
                    self.profile_label.setAlignment(QtCore.Qt.AlignCenter)

                self.update_ui()
        except FileNotFoundError:
            # Handle the case where the file doesn't exist
            pass

    def update_ui(self):
        self.name_input.setText(self.person.name)
        self.age_input.setValue(self.person.age)

        # 성별 라디오 버튼 설정
        for radio in self.gender_radio_group:
            if radio.text() == self.person.gender:
                radio.setChecked(True)

    def upload_profile_image(self):
        options = QFileDialog.Options()
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "프로필 이미지 업로드", "", "Images (*.png *.jpg *.jpeg *.gif *.bmp)", options=options)

        if file_path:
            # 이미지를 DB/profile_image 디렉토리에 복사
            destination_dir = "../PhysicalDiary/DB/profile_image"
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)

            destination_path = os.path.join(destination_dir, "profile_image.png")  # 파일 이름을 원하는 이름으로 변경

            if os.path.exists(destination_path):
                os.remove(destination_path)  # 기존 이미지 삭제

            os.rename(file_path, destination_path)  # 새 이미지로 저장

            # 이미지 크기를 조절
            max_width = 300  # 원하는 최대 폭
            max_height = 300  # 원하는 최대 높이
            image = Image.open(destination_path)
            image.thumbnail((max_width, max_height))

            image.save(destination_path)

            # 이미지를 QLabel에 표시 (가운데 정렬)
            pixmap = QPixmap(destination_path)
            self.profile_label.setPixmap(pixmap)
            self.profile_label.setAlignment(QtCore.Qt.AlignCenter)

class Person:
    def __init__(self):
        self.name = ""
        self.gender = ""
        self.age = 0

    def set_info(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def to_dict(self):
        return {
            "name": self.name,
            "gender": self.gender,
            "age": self.age
        }

    def from_dict(self, data):
        self.name = data.get("name", "")
        self.gender = data.get("gender", "")
        self.age = data.get("age", 0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProfileApp()
    window.show()
    sys.exit(app.exec())