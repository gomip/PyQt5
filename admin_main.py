# -*- coding: utf-8 -*-

import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QGroupBox, QComboBox, QFileDialog
from PyQt5.QtCore import QFileInfo, QUrl
import pandas as pd
import re

class AdminMain(QWidget):

    def __init__(self):
        super().__init__()
        self.cls = ""                                                                                                # 읽기 / 듣기 / 쓰기 선택값
        self.chp = ""                                                                                                # chapter 선택값
        self.sub = ""                                                                                                # 학습 내용 선택값
        self.dif = ""                                                                                                # 난이도 선택값
        self.selectedFile = ""
        self.df = None
        self.currentData = None 
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
        cbChp.addItem('선택')
        for i in range(1,11):
            cbChp.addItem(str(i))
        cbChp.setFixedWidth(100)
        cbChp.setFixedHeight(30)
        cbChp.activated[str].connect(self.handleChp)
        # 문제 필터 : 강의 끝 ------------------------------------------------------------------------------      

        # 문제 필터 : 학습내용 시작 ------------------------------------------------------------------------
        cbSub = QComboBox()
        cbSub.addItem('선택')
        for i in range(1,11):
            cbSub.addItem(str(i))
        cbSub.setFixedWidth(100)
        cbSub.setFixedHeight(30)
        cbSub.activated[str].connect(self.handleSub)
        # 문제 필터 : 학습내용 끝 --------------------------------------------------------------------------      

        # 문제 필터 : 강의 시작 ----------------------------------------------------------------------------
        cbDif = QComboBox()
        cbDif.addItem('선택')
        for i in range(1,11):
            cbDif.addItem(str(i))
        cbDif.setFixedWidth(100)
        cbDif.setFixedHeight(30)
        cbDif.activated[str].connect(self.handleDif)
        # 문제 필터 : 강의 끝 ------------------------------------------------------------------------------

        # 읽듣쓰 선택 시작 ---------------------------------------------------------------------------------
        cbCls = QComboBox()
        cbCls.addItem('선택')
        cbCls.addItem('읽기')
        cbCls.addItem('듣기')
        cbCls.addItem('쓰기')
        cbCls.setFixedWidth(100)
        cbCls.setFixedHeight(30)
        cbCls.activated[str].connect(self.handleCls)
        # 읽듣쓰 선택 끝 -----------------------------------------------------------------------------------         

        # 문제 필터 : 적용 버튼 시작 ------------------------------------------------------------------------
        btnFilter = QPushButton('&Enter', self)
        btnFilter.setFixedWidth(100)
        btnFilter.setFixedHeight(30)
        btnFilter.setCheckable(True)
        btnFilter.toggle()
        btnFilter.clicked.connect(self.handleUpdateExcel)
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
        grpLayout.addWidget(cbCls)
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

    # 파일 열기 시작 ---------------------------------------------------------------------------------------
    def openFileDialog(self):
        fd = QFileDialog.getOpenFileName(self, '파일 열기', "", "엑셀(*.xls, *.xlsx)")                      # 데이터 파일은 엑셀만 열리도록 설정
        self.selectedFile = fd[0]                                                                                   # fd가 튜프로 return을 해주기 때문에 [0]에 위치한 파일명을 조회
        try :
            self.df = pd.read_excel(self.selectedFile)                                                                   # pandas를 통해 excel 파일 조회
            print(self.df)
        except Exception as e:
            print(e)
    # 파일 열기 끝 -----------------------------------------------------------------------------------------

    # 읽듣쓰 선택 시작 -------------------------------------------------------------------------------------
    def handleCls(self, value) :
        try:
            self.cls = value
            self.df = pd.read_excel(self.selectedFile, sheet_name = self.cls)
        except Exception as e:
            print(e)
    # 읽듣쓰 선택 끝  --------------------------------------------------------------------------------------

    # 챕터 선택 시작 ---------------------------------------------------------------------------------------
    def handleChp(self, value) :
        try:
            self.chp = value
            print('chp', self.chp)
        except Exception as e:
            print(e)
    # 챕터 선택 끝  ----------------------------------------------------------------------------------------

    # 내용 선택 시작 ---------------------------------------------------------------------------------------
    def handleSub(self, value):
        self.sub = value
        print('sub',self.sub)
    # 내용 선택 끝  ----------------------------------------------------------------------------------------

    # 난이도 선택 시작 --------------------------------------------------------------------------------------
    def handleDif(self, value):
        self.dif = value
        print('dif', self.dif)
    # 난이도 선택 끝 ----------------------------------------------------------------------------------------

    # 선택값에 따른 pd값 업데이트 시작 -----------------------------------------------------------------------
    def handleUpdateExcel(self, value):
        try:
            self.currentData = self.df['분류표(강)'] == self.chp
            print(self.currentData)
        except Exception as e :
            print(e)
    # 선택값에 따른 pd값 업데이트 끝 -------------------------------------------------------------------------
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AdminMain()
    sys.exit(app.exec_())