import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import HuMMUS_pyqt.pyqt_ui.tab_widget_test as twt

class DlgMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HuMMUS")
        self.resize(1500, 900)
        self.menu = self.menuBar()
        self.b = self.menu.addMenu("file")
        self.c = self.b.addAction("open")
        self.c.triggered.connect(self.evt_test)

        self.mdi = QMdiArea()
        #self.mdi.setViewMode(QMdiArea.ViewMode.TabbedView)
        self.lyMain = QHBoxLayout()


        self.b = self.centralWidget()
        self.setCentralWidget(self.mdi)


    def evt_test(self):
        wdg = twt.Tab().setupUi()
        a = QMdiSubWindow()
        a.setWidget(wdg)

        lyMain = QHBoxLayout()
        wdg.setLayout(lyMain)
        lyMain.addWidget(wdg)

        a.setLayout(lyMain)
        self.mdi.addSubWindow(a)
        self.mdi.setViewMode((QMdiArea.ViewMode.SubWindowView))
        a.show()





if __name__ == "__main__":

    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())

