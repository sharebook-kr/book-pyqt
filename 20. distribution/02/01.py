import sys 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
import os

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__() 

        label = QLabel()
        label.setPixmap(QPixmap("python-logo.png"))

        button = QPushButton("Clock")

        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.addWidget(label)
        vbox.addWidget(button)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()