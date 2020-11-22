import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QToolTip, QMainWindow, qApp, QAction
from PyQt5.QtWidgets import QDesktopWidget                                              # 화면 크기 박스      
from PyQt5.QtCore import QDate,Qt,QTime                                                 # 날짜
from PyQt5.QtWidgets import QLabel, QVBoxLayout                                         # 레이아웃
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUi()

    def initUi(self):
        # ==============================================================================
        # Menu Bar 상단 메뉴
        # ==============================================================================
        exitAction = QAction(QIcon('bear.png'), 'Exit', self)                           # 아이콘, Exit action을 생성
        exitAction.setShortcut('Ctrl+Q')                                                # 단축키
        exitAction.setStatusTip('Exit Application')                                     # 상태바에 나타낼 팁 설정
        exitAction.triggered.connect(qApp.quit)                                         # 동작 선택시, 생성된 시그널이 QApplication위젯의 quit()메서드에 연결되고 앱 종료

        menuBar = self.menuBar()                                                        # 메뉴바 생성
        menuBar.setNativeMenuBar(False)
        filemenu = menuBar.addMenu('&File')                                             # & => 단축키 설정, &뒤에 F가 있음으로 alt+F가 File메뉴의 단축키
        filemenu.addAction(exitAction)                                                  # 액션 추가.

        # ==============================================================================
        # Tool Bar
        # ==============================================================================
        self.toolbar = self.addToolBar('Exit')                                          # ToolBar 생성
        self.toolbar.addAction(exitAction)
        
        # ==============================================================================
        # Style
        # ==============================================================================
        lbl_red = QLabel('Red')
        lbl_green = QLabel('Green')
        lbl_blue = QLabel('Blue')

        lbl_red.setStyleSheet("color: red;" "border-style: solid;" "border-width: 2px;" "border-color : #FA8072;" "border-radius: 3px;")
        lbl_green.setStyleSheet("color: green;" "background-color: #7fffd4;")
        lbl_blue.setStyleSheet("color: blue;" "background-color: #87cefa;" "border-style: dashed;" "border-width: 3px;" "border-color: #1e90ff")

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)
        
        self.setLayout(vbox)
        
        # ==============================================================================
        # Status Bar
        # ==============================================================================
        # self.statusBar().showMessage('Ready')                                           # statusBar() 메서드를 최초로 호출함으로서 상태바가 만들어진다.
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
        
        # ==============================================================================
        # Tooltip
        # ==============================================================================
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>Widget</b> widget')

        # ==============================================================================
        # Button
        # ==============================================================================
        btn = QPushButton('Quit',self)                                                  # push 버튼 생성, 첫번째 파라미터는 버튼에 표시될 텍스트. 두번째 파라미터는 버튼이 위치할 부모 위젯
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(200,200)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)                           # 버튼을 클릭하면 clicked 시그널 생성. -> quit 메서드에 연결. 
        
        # ==============================================================================
        # Date
        # ==============================================================================
        now = QDate.currentDate()
        print(now.toString())
        print(now.toString('d.M.yy'))
        print(now.toString('dd.MM.yyyy'))
        print(now.toString('ddd.MMM.yyyy'))
        print(now.toString(Qt.ISODate))
        print(now.toString(Qt.DefaultLocaleLongDate))

        time = QTime.currentTime()
        print(time.toString())


        # ==============================================================================
        # Window
        # ==============================================================================
        self.setWindowTitle("Scanner")                                                  # 타이틀바 설정      
        self.setWindowIcon(QIcon("bear.png"))                                           # 아이콘 설정     
        # self.setGeometry(300,300,500,500)                                               # 매개변수 : (a,b,c,d)에 대해 a,b는 move의 변수 c,d는 resize의 역할을 수행해준다.                                   
        # self.move(300,300)                                                              # 스크린의 x=300 y=300에 윈도우 배치
        # self.resize(400,200)                                                            # 화면 크기 조절
        self.resize(500,500)
        self.center()                                                                   # 스크린 가운데 화면 표시
        self.show()                                                                     # 스크린에 화면 보여주기

    def center(self):
        qr = self.frameGeometry()                                                       # 창의 위치와 크기 정보를 가져온다
        cp = QDesktopWidget().availableGeometry().center()                              # 사용하는 모니터의 가운데 위치를 파악
        qr.moveCenter(cp)                                                               # 창의 직사각형 위치를 화면의 중심의 위치로 
        self.move(qr.topLeft())

if __name__ == '__main__':                                                              # 현재 파일의 name(현재 모듈을 가리키는 내장 변수)이 같을 경우 아래 코드를 수행
    app = QApplication(sys.argv)                                                        # 모든 PyQt5 애플리케이션은 어플리케이션 객체를 생성해야한다.
    ex = MyApp()
    sys.exit(app.exec_())