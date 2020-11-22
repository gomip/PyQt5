import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout

class MyApp2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        # 버튼 생성
        okBtn = QPushButton('ok')
        cancelBtn = QPushButton('cancel')

        # ==============================================================================
        # Horizontal Box
        # ==============================================================================
        hbox = QHBoxLayout()                                                            # 수평 박스 생성
        hbox.addStretch(1)                                                              # 빈 공간 생성
        hbox.addWidget(okBtn)                                                           # okbtn 생성
        hbox.addWidget(cancelBtn)                                                       # cancelBtn 생성
        hbox.addStretch(1)                                                              # 빈 공간 생성
        # 현재 stretch factor가 1임으로 창을 늘려도 양쪽 끝의 빈 공간은 같은 비율을 유지한다.

        vbox = QVBoxLayout()                                                            # 수직박스 생성
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)
        # label1 = QLabel('Label1', self)
        # label1.move(20,20)
        # label2 = QLabel('Label2', self)
        # label2.move(20,60)

        # btn1 = QPushButton('Button1', self)
        # btn1.move(80,13)
        # btn2 = QPushButton('Button2', self)
        # btn2.move(80,53)

        self.setWindowTitle('Box')
        self.setGeometry(300,300,400,200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp2()
    sys.exit(app.exec_())