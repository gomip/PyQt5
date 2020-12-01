import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QGroupBox, QComboBox, QFileDialog

class AdminQus:
    print('hi')

    def renderQus(self):
        print('bye')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AdminQus()
    sys.exit(app.exec_())