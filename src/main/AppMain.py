# -*- coding: utf-8 -*-

# ======================================================================================================================
# 2020.12.05 | gomip | created
#   - 모든 레이아웃은 AppMain 파일에서 관리한다
# ======================================================================================================================

import sys
from PyQt5.QtWidgets import *
import pandas as pd


class AppMain(QWidget):
    def __init__(self):
        super().__init__()

        # ==============================================================================================================
        # 초기값
        # ==============================================================================================================
        self.cls = ''
        self.chp = ''
        self.sub = ''
        self.dif = ''
        self.selectedFile = ""

        self.init_ui()

    def init_ui(self):
        # self.setStyleSheet("background-color: #343a40;")
        self.setWindowTitle('main_v1')
        self.resize(1280, 960)
        self.center()
        self.show()

        # ==============================================================================================================
        # 페이지 구성
        # 실제로 출력될 화면
        # 우측은 문제 필터 및 리스트 출력
        # ==============================================================================================================
        # 필터 프레임 시작 ------------------------------------------------------------------------------------------------
        menu_frame = QFrame()
        menu_frame.setObjectName('menu_frame')
        menu_style = ""
        with open("../meta/design.qss", "r") as mf:
            menu_style = mf.read()
        menu_frame.setStyleSheet(menu_style)                                                                            # css 적용
        # 필터 프레임 끝 -------------------------------------------------------------------------------------------------

        # 필터 영역 시작 -------------------------------------------------------------------------------------------------
        file_layout = QVBoxLayout(menu_frame)
        # 파일 선택 -----------------------------------------------------------------------------------------------------
        file_opt_layout = QHBoxLayout()

        file_opt_label = QLabel("1. 파일 선택", self)
        file_opt_label.setFixedWidth(100)

        file_opt_button = QPushButton('&Open', menu_frame)
        file_opt_button.setFixedWidth(100)
        file_opt_button.setFixedHeight(30)
        file_opt_button.clicked.connect(self.openFileDialog)

        file_opt_layout.addStretch(1)
        file_opt_layout.addWidget(file_opt_label)
        file_opt_layout.addStretch(1)
        file_opt_layout.addWidget(file_opt_button)
        file_opt_layout.addStretch(2)
        # 분류 선택 -----------------------------------------------------------------------------------------------------
        cls_opt_layout = QHBoxLayout()

        cls_opt_label = QLabel("2. 항목 선택", self)
        cls_opt_label.setFixedWidth(100)

        cls_opt_button = QComboBox()
        cls_opt_button.addItem('선택')
        cls_opt_button.addItem('읽기')
        cls_opt_button.addItem('듣기')
        cls_opt_button.addItem('쓰기')
        cls_opt_button.setFixedWidth(100)
        cls_opt_button.setFixedHeight(30)
        cls_opt_button.activated[str].connect(self.handleCls)

        cls_opt_layout.addStretch(1)
        cls_opt_layout.addWidget(cls_opt_label)
        cls_opt_layout.addStretch(1)
        cls_opt_layout.addWidget(cls_opt_button)
        cls_opt_layout.addStretch(2)
        # 필터 선택 -----------------------------------------------------------------------------------------------------
        filter_opt_layout = QVBoxLayout()

        # 강의 선택
        filter_chp_layout = QHBoxLayout()
        filter_chp_label = QLabel("3-1. 강의 선택", self)
        filter_chp_label.setFixedWidth(100)
        filter_chp_button = QComboBox()
        filter_chp_button.addItem('선택')
        filter_chp_button.setFixedWidth(100)
        filter_chp_button.setFixedHeight(30)
        # 동작 함수
        filter_chp_button.activated[str].connect(self.handleChp)

        filter_chp_layout.addStretch(1)
        filter_chp_layout.addWidget(filter_chp_label)
        filter_chp_layout.addStretch(1)
        filter_chp_layout.addWidget(filter_chp_button)
        filter_chp_layout.addStretch(2)

        # 학습내용 선택
        filter_sub_layout = QHBoxLayout()
        filter_sub_label = QLabel("3-2. 학습내용 선택", self)
        filter_sub_label.setFixedWidth(100)
        filter_sub_button = QComboBox()
        filter_sub_button.addItem('선택')
        filter_sub_button.setFixedWidth(100)
        filter_sub_button.setFixedHeight(30)
        # 동작함수
        filter_sub_button.activated[str].connect(self.handleSub)

        filter_sub_layout.addStretch(1)
        filter_sub_layout.addWidget(filter_sub_label)
        filter_sub_layout.addStretch(1)
        filter_sub_layout.addWidget(filter_sub_button)
        filter_sub_layout.addStretch(2)

        # 난이도 선택
        filter_dif_layout = QHBoxLayout()
        filter_dif_label = QLabel("3-3. 난이도 선택", self)
        filter_dif_label.setFixedWidth(100)
        filter_dif_button = QComboBox()
        filter_dif_button.addItem('선택')
        filter_dif_button.setFixedWidth(100)
        filter_dif_button.setFixedHeight(30)
        # 동작함수
        filter_dif_button.activated[str].connect(self.handleDif)

        filter_dif_layout.addStretch(1)
        filter_dif_layout.addWidget(filter_dif_label)
        filter_dif_layout.addStretch(1)
        filter_dif_layout.addWidget(filter_dif_button)
        filter_dif_layout.addStretch(2)

        for i in range(1,11) :
            filter_chp_button.addItem(str(i))
            filter_sub_button.addItem(str(i))
            filter_dif_button.addItem(str(i))

        filter_opt_layout.addStretch(1)
        filter_opt_layout.addLayout(filter_chp_layout)
        filter_opt_layout.addStretch(1)
        filter_opt_layout.addLayout(filter_sub_layout)
        filter_opt_layout.addStretch(1)
        filter_opt_layout.addLayout(filter_dif_layout)
        filter_opt_layout.addStretch(1)

        # 레이아웃 구성 --------------------------------------------------------------------------------------------------
        file_layout.addLayout(file_opt_layout)
        file_layout.addLayout(cls_opt_layout)
        file_layout.addLayout(filter_opt_layout)
        file_layout.addStretch(1)
        # 필터 영역 끝 ---------------------------------------------------------------------------------------------------

        # 레이아웃 시작 --------------------------------------------------------------------------------------------------
        main_layout = QHBoxLayout()
        main_layout.setObjectName('main_layout')

        qus_layout = QVBoxLayout()
        menu_layout = QVBoxLayout()

        menu_layout.addWidget(menu_frame)                                                                               # menu_layout에 스타일을 적용한 menu_frame을 넘겨준다.

        # main_layout에 각각의 레이아웃 추가
        main_layout.addLayout(qus_layout, 4)
        main_layout.addLayout(menu_layout, 2)

        self.setLayout(main_layout)
        # 레이아웃 끝 ----------------------------------------------------------------------------------------------------

    # ==================================================================================================================
    # Function
    # ==================================================================================================================

    # 화면 중앙 배치 시작 -------------------------------------------------------------------------------------------------
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    # 화면 중앙 배치 끝 --------------------------------------------------------------------------------------------------

    # 파일 열기 시작 -----------------------------------------------------------------------------------------------------
    def openFileDialog(self):
        fd = QFileDialog.getOpenFileName(self, '파일 열기', "", "엑셀(*.xls, *.xlsx)")                                      # 데이터 파일은 엑셀만 열리도록 설정
        self.selectedFile = fd[0]                                                                                       # fd가 튜프로 return을 해주기 때문에 [0]에 위치한 파일명을 조회
        try :
            self.df = pd.read_excel(self.selectedFile)                                                                  # pandas를 통해 excel 파일 조회
            print(self.selectedFile)
        except Exception as e:
            print(e)
    # 파일 열기 끝 -------------------------------------------------------------------------------------------------------

    # 읽듣쓰 선택 시작 -----------------------------------------------------------------------------------------------------
    def handleCls(self, value) :
        print(self.selectedFile)
        try:
            self.cls = value
            self.df = pd.read_excel(self.selectedFile, sheet_name = self.cls)
        except Exception as e:
            print(e)
    # 읽듣쓰 선택 끝  ------------------------------------------------------------------------------------------------------

    # 챕터 선택 시작 -----------------------------------------------------------------------------------------------------
    def handleChp(self, value) :
        try:
            self.chp = value
        except Exception as e:
            print(e)
    # 챕터 선택 끝  ------------------------------------------------------------------------------------------------------

    # 내용 선택 시작 -----------------------------------------------------------------------------------------------------
    def handleSub(self, value):
        try:
            self.sub = value
        except Exception as e:
            print(e)
    # 내용 선택 끝  ------------------------------------------------------------------------------------------------------

    # 난이도 선택 시작 ---------------------------------------------------------------------------------------------------
    def handleDif(self, value):
        try:
            self.dif = value
        except Exception as e:
            print(e)
    # 난이도 선택 끝 -----------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AppMain()
    sys.exit(app.exec_())
