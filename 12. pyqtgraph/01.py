import sys
from PyQt5.QtWidgets import *
import pyqtgraph as pg


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.plot_widget = pg.PlotWidget()
        self.setCentralWidget(self.plot_widget)

        x = [1, 2, 3, 4]
        y = [1, 4, 9, 16]
        self.plot_widget.plot(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()