import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QHBoxLayout, QMessageBox
from PySide6.QtGui import QPixmap


class ProfileEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('프로필 수정')

        # 레이아웃 설정
        layout = QVBoxLayout()

        # 프로필 이미지
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap('default_profile.png'))  # 기본 프로필 이미지
        self.image_button = QPushButton('이미지 변경', self)
        self.image_button.clicked.connect(self.changeImage)

        # 아이디 입력
        self.id_label = QLabel('아이디', self)
        self.id_edit = QLineEdit(self)

        # 비밀번호 입력
        self.password_label = QLabel('비밀번호', self)
        self.password_edit = QLineEdit(self)
        self.password_edit.setEchoMode(QLineEdit.Password)

        # 저장 버튼
        self.save_button = QPushButton('저장', self)
        self.save_button.clicked.connect(self.saveProfile)

        # 레이아웃에 위젯 추가
        layout.addWidget(self.image_label)
        layout.addWidget(self.image_button)
        layout.addWidget(self.id_label)
        layout.addWidget(self.id_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def changeImage(self):
        file_name, _ = QFileDialog.getOpenFileName(self, '프로필 이미지 선택')
        if file_name:
            self.image_label.setPixmap(QPixmap(file_name))

    def saveProfile(self):
        # 실제 애플리케이션에서는 여기에 프로필 정보를 저장하는 코드를 작성해야 합니다.
        QMessageBox.information(self, '저장', '프로필이 성공적으로 저장되었습니다!')



