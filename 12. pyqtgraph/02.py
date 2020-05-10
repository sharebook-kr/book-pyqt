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

        # Style
        self.plot_widget.setBackground('w')
        self.plot_widget.setTitle("기본 그래프")
        self.plot_widget.setLabel("left", "y-axis")
        self.plot_widget.setLabel("bottom", "x-axis")
        self.plot_widget.showGrid(x=True, y=True)

        self.plot_widget.plot(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()