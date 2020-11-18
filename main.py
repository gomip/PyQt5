import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QToolTip, QMainWindow
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        # ==============================================================================
        # Tooltip
        # ==============================================================================
        self.statusBar().showMessage('Ready')                                           # statusBar() 메서드를 최초로 호출함으로서 상태바가 만들어진다.
        
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
        # Window
        # ==============================================================================
        self.setWindowTitle("Scanner")                                                  # 타이틀바 설정      
        self.setWindowIcon(QIcon("bear.png"))                                           # 아이콘 설정     
        self.setGeometry(300,300,500,500)                                               # 매개변수 : (a,b,c,d)에 대해 a,b는 move의 변수 c,d는 resize의 역할을 수행해준다.                                   
        # self.move(300,300)                                                              # 스크린의 x=300 y=300에 윈도우 배치
        # self.resize(400,200)                                                            # 화면 크기 조절
        self.show()                                                                     # 스크린에 화면 보여주기

if __name__ == '__main__':                                                              # 현재 파일의 name(현재 모듈을 가리키는 내장 변수)이 같을 경우 아래 코드를 수행
    app = QApplication(sys.argv)                                                        # 모든 PyQt5 애플리케이션은 어플리케이션 객체를 생성해야한다.
    ex = MyApp()
    sys.exit(app.exec_())