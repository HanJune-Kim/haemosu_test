import sys, os
import time
from PyQt6.QtWidgets import *
from pyqt_ui.HuMMUS_MainOpen import *
from pyqt_ui.HuMMUS_MainWindow import *
import qdarktheme
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import pyqt_ui.HuMMUS_Create_New_Project as create_project
from PyQt6.QtWebEngineWidgets import *

from PyQt6 import QtCore, QtGui, QtWidgets
class MenuMain(QDialog, Ui_Dialog):
    def __init__(self):
        super(MenuMain, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("HuMMUS v1.0.0")

        self.MainPath = os.path.dirname(os.path.realpath(__file__))
        self.ProgramPath = "/".join([self.MainPath, "HuMMUS_MainMenu.py"])
        self.UiPath = "/".join([self.MainPath, "UI_Icon", "PNG"])
        self.setWindowIcon(QIcon("/".join([self.UiPath, "HuMMUS_Icon1.png"])))
        #self.setWindowFlags(Qt.WindowType.Dialog.FramelessWindowHint)
        self.ToolMenu = QMenu()
        self.Theme = "dark"
        self.actionNewProject = QAction("New Project")
        self.actionOpenProject = QAction("Open Project")
        self.actionDocumentation = QAction("Documentation")
        self.actionTheme = QAction("Light Theme")
        self.actionTheme.setCheckable(True)
        self.actionTheme.setChecked(False)
        self.actionQuitHuMMUS = QAction("Quit HuMMUS")
        self.ToolMenu.addAction(self.actionNewProject)
        self.ToolMenu.addAction(self.actionOpenProject)
        self.ToolMenu.addAction(self.actionDocumentation)
        self.ToolMenu.addAction(self.actionQuitHuMMUS)
        self.minimizebtn.clicked.connect(self.evt_minimizebtn_clicked)


        self.GoWithHuMMUSBtn.setMenu(self.ToolMenu)
        self.GoWithHuMMUSBtn.setIcon(QIcon("/".join([self.UiPath, "GOWITHHUMMUSBTN1.png"])))
        self.GoWithHuMMUSBtn.setIconSize(QSize(110, 100))
        self.LogoLabel.setPixmap(QPixmap("/".join([self.UiPath, "HuMMUS_LOGO1.png"])))

        self.actionNewProject.triggered.connect(self.evt_actionNewProject_triggered)
        #self.actionOpenProject.triggered.connect(self.evt_actionOpenProject_triggered)
        self.actionQuitHuMMUS.triggered.connect(self.evt_actionQuitHuMMUS_triggered)




    def evt_minimizebtn_clicked(self):
        self.showMinimized()

    def evt_actionQuitHuMMUS_triggered(self):
        self.close()

    def evt_actionNewProject_triggered(self):
        self.NewProject_object = QDialog()
        self.NewProject = create_project.Ui_Dialog()
        self.NewProject.setupUi(self.NewProject_object)
        self.Location = self.NewProject.Location
        self.Loadbtn = self.NewProject.Load
        self.projecttitle = self.NewProject.Project_Title
        self.Createbtn = self.NewProject.Create_Project
        self.Loadbtn.clicked.connect(self.evt_NewProject_load_clicked)
        self.Createbtn.clicked.connect(self.evt_NewProject_create_clicked)

        self.NewProject_object.open()
        self.NewProject_object.exec()

    def evt_NewProject_load_clicked(self):
        self.ProjectDir = QFileDialog.getExistingDirectory(self, "Location to New Project", os.path.expanduser("~"))
        self.Location.setText(self.ProjectDir)

    def evt_NewProject_create_clicked(self):
        if self.projecttitle.text() == "" or self.Location.text() == "":
            QMessageBox.critical(self, "Error", "Both 'Project Title' and 'Loaction' MUST be specified.")
        elif self.projecttitle.text() != "" or self.Location.text() != "":
            current_path = "/".join([self.Location.text(), self.projecttitle.text()])
            if os.path.isdir(current_path):
                QMessageBox.critical(self, "Error", "The directory already exist.\n{}".format(current_path))
            else:
                os.makedirs(self.ProjectDir+"/"+self.projecttitle.text(), exist_ok = True)
                self.NewProject_object.reject()
                QMessageBox.information(self, "Notice", "The HuMMUS Project {} was created in {}.".format(self.projecttitle.text(), self.ProjectDir))
                self.setWindowTitle(" - ".join([self.windowTitle(), self.projecttitle.text()]))
                self.ProjectTitle = self.projecttitle.text()
                if not self.DarkMode.isChecked():
                    self.Theme = "light"
                self.qprocess = QProcessDistatched(self.ProjectDir, self.ProjectTitle, self.ProgramPath, self.Theme)
                self.qprocess.run()
                self.showMinimized()




class QProcessDistatched(QProcess):

    def __init__(self, projectdir, projecttitle, programpath, theme):
        super().__init__()
        self.ProjectDir = projectdir
        self.ProjectTitle = projecttitle
        self.ProgramPath = programpath
        self.pythonpath = "/home/hjkim-g15-portable/HuMMUS_venv/bin/python3.9"
        self.theme = theme
        self.arguments = [self.ProgramPath, self.ProjectDir, self.ProjectTitle, self.theme]
    def run(self):
        self.setProgram(self.pythonpath)
        self.setArguments(self.arguments)
        self.startDetached()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarktheme.load_stylesheet("light"))
    #app.setStyle("WindowsVista")
    menuMain = MenuMain()
    menuMain.show()
    sys.exit(app.exec())
