import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWebEngineWidgets import *
import random

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HuMMUS")
        self.resize(1500, 900)


        ##### Create Widgets
        self.trwQt = QTreeWidget()
        self.trwQt.setColumnCount(1)
        self.trwQt.setHeaderLabels(["HuMMUS Class"])
        self.trwQt.itemDoubleClicked.connect(self.evt_trwQT_dbClicked)
        self.populateTree()

        self.trwQt.sortItems(0, Qt.SortOrder.AscendingOrder)
        self.trwQt.setColumnWidth(0, 150)
        self.trwQt.expandItem(self.twiQWidget)

        self.cmbParents = QComboBox()
        lstClasses = get_all_items(self.trwQt)
        lstClasses.sort()
        for cls in lstClasses:
            self.cmbParents.addItem(cls.text(0))

        self.ledClassName = QLineEdit("Q")
        self.btnAddClass = QPushButton("Add Class")
        self.btnAddClass.clicked.connect(self.evt_btnAdd_clicked)

        self.web = QWebEngineView()
        self.web.setUrl(QUrl.fromUserInput("https://doc.qt.io/qt-6/qtmodules.html"))
        #### lyWeb Widgets
        self.btnForward = QPushButton(">>")
        self.btnForward.clicked.connect(self.web.forward)
        self.btnBackward = QPushButton("<<")
        self.btnBackward.clicked.connect(self.web.back)
        self.btnHome = QPushButton("HOME")
        self.btnHome.clicked.connect(self.evt_btnHome_clicked)
        self.btnHistory = QPushButton("Show History")
        self.btnHistory.clicked.connect(self.evt_btnHistory_clicked)

        self.tblHistory = QTableWidget(3, 4)
        self.tblHistory.hide()
        self.tblHistory.setColumnWidth(0, 180)
        self.tblHistory.setColumnWidth(1, 180)
        self.tblHistory.setColumnWidth(2, 450)
        self.tblHistory.setColumnWidth(3, 180)
        self.tblHistory.cellClicked.connect(self.evt_tblHistory_clicked)

        ##### Setup Layout

        self.lyMain = QHBoxLayout()
        self.lyTree = QVBoxLayout()
        self.lyBtnWeb = QVBoxLayout()
        self.lybtns = QHBoxLayout()
        self.lyTree.addWidget(self.trwQt)
        self.lyTree.addWidget(self.cmbParents)
        self.lyTree.addWidget(self.ledClassName)
        self.lyTree.addWidget(self.btnAddClass)

        self.lyWev = QVBoxLayout()
        self.lyWev.addWidget(self.web)
        self.lyWev.addWidget(self.tblHistory)

        self.lybtns.addWidget(self.btnHome)
        self.lybtns.addWidget(self.btnBackward)
        self.lybtns.addWidget(self.btnForward)
        self.lybtns.addWidget(self.btnHistory)
        self.lyBtnWeb.addLayout(self.lybtns, 5)
        self.lyBtnWeb.addLayout(self.lyWev, 95)
        self.lyMain.addLayout(self.lyTree, 20)
        self.lyMain.addLayout(self.lyBtnWeb, 80)

        self.setLayout(self.lyMain)


    def populateTree(self):
        ##### Create Top level items

        self.twiQWidget = QTreeWidgetItem(self.trwQt, ["Preprocessing Module"])
        self.twiQGui = QTreeWidgetItem(self.trwQt, ["Classification Module"])
        self.twiQCore = QTreeWidgetItem(self.trwQt, ["Analysis Module"])


        #### Add subItems to Qwidget Module
        lstQWidget = ["Trimming", "Decontamination"]
        for cls in lstQWidget:
            self.twiQWidget.addChild(QTreeWidgetItem([cls]))#, str(random.randrange(25)), str(random.randrange(8))]))

        #### Add SubItems to QGui
        lstQGui = ["Bitmap", "QColor", "QFont", "QIcon", "QImage"]
        for cls in lstQGui:
            self.twiQGui.addChild(QTreeWidgetItem([cls]))#, str(random.randrange(25)), str(random.randrange(8))]))

        #### Add SubItems to QCore
        lstQCore = ["QThread", "QDataTime", "QPixmap", "QUrl", "QFile"]
        for cls in lstQCore:
            self.twiQCore.addChild(QTreeWidgetItem([cls]))#, str(random.randrange(25)), str(random.randrange(8))]))

        #### Add subitems to Qdialog
        twi = self.trwQt.findItems("Trimming", Qt.MatchFlag.MatchRecursive)[0]
        listQDialog = ["Trimmomatic"]
        for cls in listQDialog:
            twi.addChild(QTreeWidgetItem([cls]))#, str(random.randrange(25)), str(random.randrange(8))]))

    ##### Event handler
    def evt_trwQT_dbClicked(self, twi, col):
        #QMessageBox.information(self, "QT Classes", "You chose the {} class".format(twi.text(0)))
        url = "https://doc.qt.io/qt-6/{}.html".format(twi.text(0).lower())
        self.web.setUrl(QUrl.fromUserInput(url))
        self.web.repaint()
        self.refreshHistory()
    def evt_btnAdd_clicked(self):
        ans = QMessageBox.question(self, "Add Class", "Are you sure that you want to add {} to {}".format(self.ledClassName.text(), self.cmbParents.currentText()))
        if ans ==QMessageBox.StandardButton.Yes:
            twi = self.trwQt.findItems(self.cmbParents.currentText(), Qt.MatchFlag.MatchRecursive)[0]
            twi.addChild(QTreeWidgetItem([self.ledClassName.text(), str(random.randrange(25)), str(random.randrange(8))]))

    def evt_btnHome_clicked(self):
        self.web.setUrl(QUrl.fromUserInput("https://netbiolab.org/w/Welcome"))

    def evt_btnHistory_clicked(self):
        if self.tblHistory.isHidden():

            self.tblHistory.show()
            self.btnHistory.setText("Hide History")
            self.refreshHistory()
        else:
            self.tblHistory.hide()
            self.btnHistory.setText("Show History")

    def refreshHistory(self):
        self.tblHistory.clear()
        self.tblHistory.setHorizontalHeaderLabels(["Class", "Module", "URL", "Last Visited"])
        history = self.web.history()
        cnt = history.count()
        self.tblHistory.setRowCount(cnt)
        for idx in range(cnt):
            itm = history.itemAt(idx)
            sClass, sModule = itm.title().split(" | ")
            self.tblHistory.setItem(cnt - idx, 0, QTableWidgetItem(sClass))
            self.tblHistory.setItem(cnt - idx, 1, QTableWidgetItem(sModule))
            self.tblHistory.setItem(cnt - idx, 2, QTableWidgetItem(itm.url().toString()))
            self.tblHistory.setItem(cnt - idx, 3, QTableWidgetItem(itm.lastVisited().toString()))

    def evt_tblHistory_clicked(self, row, col):
        url = self.tblHistory.item(row, 2).text()
        self.web.setUrl(QUrl().fromUserInput(url))
        self.refreshHistory()

def get_subtree_nodes(tree_widget_item):
    nodes = []
    nodes.append(tree_widget_item)
    for i in range(tree_widget_item.childCount()):
        nodes.extend(get_subtree_nodes(tree_widget_item.child(i)))
    return nodes

def get_all_items(tree_widget):

    all_items = []
    for i in range(tree_widget.topLevelItemCount()):
        top_item = tree_widget.topLevelItem(i)
        all_items.extend(get_subtree_nodes(top_item))
    return all_items

if __name__ == "__main__":

    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())
