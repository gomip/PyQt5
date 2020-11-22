import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QDesktopWidget, QLabel, QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt                                                                                 # 폰트
from PyQt5 import QtGui
# =====================================================================================================
# QLabel = 레이블 표시
# QtCore = 폰트
# QLineEdit, QPushButton = 아이디 비밀번호 입력 및 로그인 버튼
# QMessageBox = 메시지 박스 노출 
# =====================================================================================================

class Login(QWidget):
    global login_id
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('채점 시스템')
        self.resize(500,350)
        self.center()
        self.show()

        # =====================================================================================================
        # 레이블 
        # =====================================================================================================
        labelTitle = QLabel('Log In', self)
        labelTitle.setAlignment(Qt.AlignCenter)

        fontTitle = labelTitle.font()
        fontTitle.setPointSize(20)

        labelTitle.setFont(fontTitle)

        labelId = QLabel('Username', self)
        labelId.setStyleSheet("margin-top: 10px;")
        labelPwd = QLabel('Password',self)
        labelPwd.setStyleSheet("margin-top: 5px;")

        # =====================================================================================================
        # 아이디 및 패스워드 입력
        # =====================================================================================================
        self.editId = QLineEdit()                                                                               # 아이디 입력 위젯 생성
        # editId.setPlaceholderText('ID를 입력해주세요.')                                                         # 입력된 값이 없을 경우 default 텍스트 설정
        self.editId.setEchoMode(QLineEdit.Normal)                                                                   # 입력한 값을 QLineEdit 위젯에 공개 
        self.editId.setFixedSize(240,40)                                                                            # 텍스트박스 크기 조절
        self.editId.setStyleSheet("border-width: 2px;"
                             "border-radius: 5px;"
                             "font-size: 15px;"
                            )                                                                                  # 스타일 정의

        self.editPwd = QLineEdit()                                                                              # 비밀번호 입력 위젯 생성
        # editPwd.setPlaceholderText('비밀번호를 입력해주세요.')
        self.editPwd.setEchoMode(QLineEdit.Password)                                                                # 비밀번호는 입력시 * 노출 
        self.editPwd.setFixedSize(240,40)                                                                           # 텍스트박스 크기 조절
        self.editPwd.setStyleSheet("border-width: 2px;"
                             "border-radius: 5px;"
                             "font-size: 15px;"
                            )                                                                                  # 스타일 정의

        # =====================================================================================================
        # 로그인 버튼
        # =====================================================================================================
        btnLogin = QPushButton('로그인',self)
        # btnLogin.setText('로그인')
        btnLogin.setCheckable(True)
        btnLogin.setFixedSize(240,40)
        btnLogin.setStyleSheet("border-width: 2px;"
                               "border-radius: 5px;"
                               "font-size: 15px;"
                               "margin-top: 5px;"
                               "color: white;"
                               "background-color: #229EF2;"
                              )
        btnLogin.clicked.connect(self.onLogin)

        # =====================================================================================================
        # 로그인 레이아웃
        # =====================================================================================================
        # 입력 레이아웃
        vboxInput = QVBoxLayout()
        vboxInput.addWidget(labelId)
        vboxInput.addWidget(self.editId)
        vboxInput.addWidget(labelPwd)
        vboxInput.addWidget(self.editPwd)
        vboxInput.addWidget(btnLogin)

        # 가운데 정렬을 위해 레이아웃 추가
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vboxInput)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(2)
        vbox.addWidget(labelTitle)
        vbox.addLayout(hbox)
        vbox.addStretch(2)
        self.setLayout(vbox)

    # =====================================================================================================
    # 화면 중앙 출력
    # =====================================================================================================
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    # =====================================================================================================
    # 텍스트 변경 onChanged 핸들러
    # =====================================================================================================
    def onLogin(self):
        msg = QMessageBox()
        if (self.editId.text() == 'admin' and self.editPwd.text() == '1234'):
            msg.setText('로그인')
            msg.exec_()
        elif (self.editId.text() != 'admin' or self.editPwd.text() != '1234'):
            msg.setText('로그인 id 혹은 pwd가 잘못되었습니다.')
            msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())