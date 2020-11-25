import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QGroupBox, QComboBox, QFileDialog

class AdminMain(QWidget):
    chp = ''
    sub = ''
    dif = ''

    def __init__(self):
        super().__init__()
        self.initUi()
    
    def initUi(self):
        self.setWindowTitle('Admin_v1')
        self.resize(1280, 960)
        self.center()
        self.show()

        # =================================================================================================
        # 페이지 구성
        # =================================================================================================
        
        # 프레임 시작 --------------------------------------------------------------------------------------
        self.qusFrame = QFrame()
        self.qusFrame.setObjectName("qus_frame")
        qusFrameStyle = ""
        with open("./design/design.qss", "r") as fqus:
            qusFrameStyle = fqus.read()
        self.qusFrame.setStyleSheet(qusFrameStyle)

        self.btnFrame = QFrame()
        self.btnFrame.setObjectName("btn_frame")
        btnFrameStyle = ""
        with open("./design/design.qss", "r") as fbtn:
            btnFrameStyle = fbtn.read()
        self.btnFrame.setStyleSheet(btnFrameStyle)
        # 프레임 끝 ---------------------------------------------------------------------------------------

        # 버튼 생성 시작 ----------------------------------------------------------------------------------
        btnOpen = QPushButton('&Open', self.btnFrame)
        btnOpen.setFixedWidth(100)
        btnOpen.setFixedHeight(30)
        btnOpen.setCheckable(True)
        btnOpen.toggle()
        btnOpen.clicked.connect(self.openFileDialog)

        btnSave = QPushButton('&Save', self.btnFrame)
        btnSave.setFixedWidth(100)
        btnSave.setFixedHeight(30)
        btnSave.setCheckable(True)
        btnSave.toggle()

        btnRes = QPushButton('&Res', self.btnFrame)
        btnRes.setFixedWidth(100)
        btnRes.setFixedHeight(30)
        btnRes.setCheckable(True)
        btnRes.toggle()
        # 버튼 생성 끝 ------------------------------------------------------------------------------------

        # 문제 필터 : 강의 시작 ---------------------------------------------------------------------------
        cbChp = QComboBox()
        for i in range(1,11):
            cbChp.addItem(str(i))
        cbChp.setFixedWidth(100)
        cbChp.setFixedHeight(30)
        # 문제 필터 : 강의 끝 ------------------------------------------------------------------------------      

        # 문제 필터 : 학습내용 시작 ------------------------------------------------------------------------
        cbSub = QComboBox()
        for i in range(1,11):
            cbSub.addItem(str(i))
        cbSub.setFixedWidth(100)
        cbSub.setFixedHeight(30)
        # 문제 필터 : 학습내용 끝 --------------------------------------------------------------------------      

        # 문제 필터 : 강의 시작 ----------------------------------------------------------------------------
        cbDif = QComboBox()
        for i in range(1,11):
            cbDif.addItem(str(i))
        cbDif.setFixedWidth(100)
        cbDif.setFixedHeight(30)
        # 문제 필터 : 강의 끝 ------------------------------------------------------------------------------      

        # 문제 필터 : 적용 버튼 시작 ------------------------------------------------------------------------
        btnFilter = QPushButton('&Enter', self)
        btnFilter.setFixedWidth(100)
        btnFilter.setFixedHeight(30)
        btnFilter.setCheckable(True)
        btnFilter.toggle()
        # 문제 필터 : 적용 버튼 끝 --------------------------------------------------------------------------

        # 문제 필터 그룹 시작 ------------------------------------------------------------------------------
        filterGroup = QGroupBox()

        grpLayout = QHBoxLayout()
        grpLayout.setObjectName("fil_grp_layout")
        filStyle = ""
        with open("./design/design.qss", "r") as fbtn:
            filStyle = fbtn.read()
        filterGroup.setStyleSheet(filStyle)

        grpLayout.addStretch(1)
        grpLayout.addWidget(cbChp)
        grpLayout.addStretch(1)
        grpLayout.addWidget(cbSub)
        grpLayout.addStretch(1)
        grpLayout.addWidget(cbDif)
        grpLayout.addStretch(1)
        grpLayout.addWidget(btnFilter)
        grpLayout.addStretch(1)
        
        grpBoxLayout = QVBoxLayout()
        grpBoxLayout.addStretch(1)
        grpBoxLayout.addLayout(grpLayout)
        grpBoxLayout.addStretch(5)

        filterGroup.setLayout(grpBoxLayout)

        # 문제 필터 그룹 끝  -------------------------------------------------------------------------------

        # 로그인 레이아웃 시작 -----------------------------------------------------------------------------
        # 좌측은 문제 우측은 필터링 및 버튼들을 모아두는 형식
        totLayout = QHBoxLayout()                                                                          # 전체 레이아웃
        qusLayout = QVBoxLayout()                                                                          # 문제 레이아웃           
        btnLayout = QVBoxLayout()                                                                          # 버튼 레이아웃

        btnTopLayout = QHBoxLayout()
        btnTopLayout.addStretch(1)
        btnTopLayout.addWidget(btnOpen)
        btnTopLayout.addStretch(1)
        btnTopLayout.addWidget(btnSave)
        btnTopLayout.addStretch(1)
        btnTopLayout.addWidget(btnRes)
        btnTopLayout.addStretch(1)

        btnBoxLayout = QVBoxLayout(self.btnFrame)
        btnBoxLayout.addStretch(1)
        btnBoxLayout.addLayout(btnTopLayout)
        btnBoxLayout.addStretch(1)
        btnBoxLayout.addWidget(filterGroup)
        btnBoxLayout.addStretch(8)
        # 로그인 레이아웃 끝 -------------------------------------------------------------------------------

        # 문제 페이지 구성 ---------------------------------------------------------------------------------
        qusLayout.addWidget(self.qusFrame)

        # 버튼 페이지 구성 ---------------------------------------------------------------------------------
        btnLayout.addWidget(self.btnFrame)

        # 전체 페이지 구성 ---------------------------------------------------------------------------------

        totLayout.addLayout(qusLayout, 2)
        totLayout.addLayout(btnLayout, 1)

        self.setLayout(totLayout)
    
    # =====================================================================================================
    # Function
    # =====================================================================================================
    # 중앙 배치 --------------------------------------------------------------------------------------------
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # =====================================================================================================
    # 파일 열기
    # =====================================================================================================
    def openFileDialog(self):
        fd = QFileDialog.getOpenFileName(self, '파일 열기', "", self.tr("파일 타입(*.xls, *.xlsx)"))         # 데이터 파일은 엑셀만 열리도록 설정
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AdminMain()
    sys.exit(app.exec_())