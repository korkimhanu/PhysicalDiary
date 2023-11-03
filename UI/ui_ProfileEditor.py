import sys
from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QHBoxLayout, QMessageBox, QFileDialog
)
from PySide6.QtGui import QPixmap


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")

        self.setWindowTitle("프로필 수정")
        self.setGeometry(100, 100, 300, 200)

        # 프로필 사진
        self.profile_pic_label = QLabel("프로필 사진")
        self.profile_pic = QLabel()
        self.profile_pic.setFixedSize(100, 100)
        self.profile_pic.setPixmap(QPixmap("default_profile.png"))  # 기본 프로필 사진
        self.profile_pic_button = QPushButton("사진 변경")
        self.profile_pic_button.clicked.connect(self.change_profile_pic)

        # 아이디
        self.id_label = QLabel("아이디")
        self.id_edit = QLineEdit()

        # 비밀번호
        self.password_label = QLabel("비밀번호")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)

        # 저장 버튼
        self.save_button = QPushButton("저장")
        self.save_button.clicked.connect(self.save_profile)

        # 레이아웃 구성
        layout = QVBoxLayout()

        pic_layout = QHBoxLayout()
        pic_layout.addWidget(self.profile_pic)
        pic_layout.addWidget(self.profile_pic_button)

        layout.addWidget(self.profile_pic_label)
        layout.addLayout(pic_layout)
        layout.addWidget(self.id_label)
        layout.addWidget(self.id_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def change_profile_pic(self):
        # 파일 다이얼로그를 열어 이미지 파일을 선택합니다.
        filename, _ = QFileDialog.getOpenFileName(self, "프로필 사진 선택", "", "이미지 파일 (*.png *.jpg *.jpeg *.bmp *.gif)")
        if filename:
            self.profile_pic.setPixmap(QPixmap(filename))

    def save_profile(self):
        # 입력된 정보를 가져옵니다.
        user_id = self.id_edit.text()
        password = self.password_edit.text()
        # 여기에 정보를 저장하는 로직을 추가합니다. 예를 들어 데이터베이스에 저장할 수 있습니다.

        # 확인 메시지를 표시합니다.
        QMessageBox.information(self, "저장 완료", "프로필이 저장되었습니다.")

# 이 부분은 main.py에서 QApplication 인스턴스를 생성한 후에 다음과 같이 연결해야 합니다.
# app = QApplication(sys.argv)
# profile_dialog = ProfileDialog()
# profile_dialog.show()
# sys.exit(app.exec())
