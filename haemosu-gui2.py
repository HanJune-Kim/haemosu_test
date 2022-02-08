#!/usr/bin/env python3
import sys, os
import random
from collections import *
import pandas as pd
import psutil
from PyQt6.QtWidgets import *
from pyqt_ui.HuMMUS_MainWindow import *
import pyqt_ui.HuMMUS_PB_Trimmomatic as trimmomatic_options
import pyqt_ui.HuMMUS_PB_Bowtie2 as bowtie_options
import pyqt_ui.HuMMUS_PB_Kraken2 as kraken_options
import pyqt_ui.HuMMUS_PB_Diamond as diamond_options
import pyqt_ui.HuMMUS_PB_Alpha as alpha_options
import pyqt_ui.HuMMUS_PB_Beta as beta_options
import pyqt_ui.HuMMUS_PB_MWU as mannwhitneyu_option
import pyqt_ui.HuMMUS_PB_lefse as lefse_option
import pyqt_ui.HuMMUS_PB_ANCOMBC as ancombc_option
import pyqt_ui.HuMMUS_PB_Songbird as songbird_option
import pyqt_ui.HuMMUS_PB_RandomForest as randomforest_option
import pyqt_ui.HuMMUS_Recheck_MetaPara as recheck_matepara
import pyqt_ui.HuMMUS_Progress_bar as progressbar
import pyqt_ui.HuMMUS_Create_New_Project as create_project
import HuMMUS_Argument_Generate as Arguments_generator
import qdarktheme
import TreeWidget
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWebEngineWidgets import *
import logging
from PyQt6 import QtCore, QtGui, QtWidgets


class MenuMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MenuMain, self).__init__()
        self.setupUi(self)
        self.ProjectDir = "haha"
        self.ProjectTitle = "haha"
        self.R_path = r"C:\Program Files\R\R-4.1.2\bin\x64\Rscript.exe"
        self.initiate_widget()
        self.setWindowTitle(" - ".join(["HuMMUS v0.1.0", self.ProjectTitle]))

        #############meta variable ################33
        self.HuMMUS_path = os.path.dirname(os.path.realpath(__file__))
        self.ProgramPath = "/".join([self.HuMMUS_path, "HuMMUS_MainMenu.py"])
        self.UiPath = "/".join([self.HuMMUS_path, "UI_Icon", "PNG"])
        self.setWindowIcon(QIcon("/".join([self.UiPath, "HuMMUS_Icon2.png"])))
        ##########Style sheet###########
        #self.Theme = sys.argv[3]
        self.evt_SystemMonitor()

        ##################################################
        ################ Adjust Layout ###################
        ##################################################
        self.lyMain = QVBoxLayout()

        self.centralwidget.setLayout(self.lyMain)
        self.lyTap = QHBoxLayout()
        self.lyMain.addWidget(self.tabWidget)
        self.centralwidget.setStyleSheet(self.MainWindow_style())
        ############### Adjust PB Layout #################
        self.initiate_widget()
        self.PB_UpperMostLayout.insertWidget(0, self.PB_MetaPara_gbx)

        self.PipelineBuilder.setLayout(self.PB_UpperMostLayout)

        self.sp_PBuilder_High_sub.setSizes([10, 100, 300])
        self.sp_PBuilder_High_Top.setSizes([100, 150])
        ############## Adjust VA Layout ##################
        self.lyVAnalysis = QHBoxLayout()
        self.lyGridLayer = QGridLayout()
        #self.VA_MDIArea.setLayout(self.lyGridLayer)
        self.lyVAnalysis.addWidget(self.VA_UpperMost_splitter)
        self.VisualizationAnalysis.setLayout(self.lyVAnalysis)

        self.setLayout(self.lyMain)

        self.VA_HuMMUSViewList_btn_load.clicked.connect(self.evt_VA_list_load_clicked)


        #self.label.setPicture(QPicture)


        ################StatusBar##################

        self.StatusBarInstance = initiate_statusbar()
        self.StatusBar = self.StatusBarInstance.Get_widget()
        self.StatusBarWidget = self.StatusBar.horizontalWidget_2
        self.CPUBar = self.StatusBar.cpuPrg
        self.RAMBar = self.StatusBar.ramPrg
        self.MainStatusBar = self.StatusBar.MainStatusBar
        self.SubStatusBar = self.StatusBar.SubStatusBar
        self.MainPrgBar = self.StatusBar.MainPrgBar
        self.MainPrgBar.setValue(0)
        self.MainWindow_StatusBar.addWidget(self.StatusBarWidget, stretch =1)
        self.MainWindow_StatusBar.setMaximumHeight(90)
        self.MainProcessFinished = True
        self.SubProcess1Finished = True
        self.SubProcess2Finished = True
        self.SubProcess3Finished = True

        ######### Main ###########

        ##################PB Moduels ##########################
        self.module_dict = self.get_module_name()
        self.PB_Modules_prep_tree.itemDoubleClicked.connect(self.evt_PB_Modules_tree_dblclicked)
        self.PB_prep_pipeline_list.itemDoubleClicked.connect(self.evt_PB_pipeline_list_dblclicked)
        self.PB_prep_pipeline_list.itemClicked.connect(self.evt_pipeline_itm_clicked)

        self.PB_Modules_classification_tree.itemDoubleClicked.connect(self.evt_PB_Modules_tree_dblclicked)
        self.PB_class_pipeline_list.itemDoubleClicked.connect(self.evt_PB_pipeline_list_dblclicked)
        self.PB_class_pipeline_list.itemClicked.connect(self.evt_pipeline_itm_clicked)

        self.PB_Modules_sanalysis_tree.itemDoubleClicked.connect(self.evt_PB_Modules_tree_dblclicked)
        self.PB_SA_pipeline_list.itemDoubleClicked.connect(self.evt_PB_pipeline_list_dblclicked)
        self.PB_SA_pipeline_list.itemClicked.connect(self.evt_pipeline_itm_clicked)

        self.PB_Modules_modeling_tree.itemDoubleClicked.connect(self.evt_PB_Modules_tree_dblclicked)
        self.PB_model_pipeline_list.itemDoubleClicked.connect(self.evt_PB_pipeline_list_dblclicked)
        self.PB_model_pipeline_list.itemClicked.connect(self.evt_pipeline_itm_clicked)

        self.PB_ModulePresets_btn_clear.clicked.connect(self.evt_PB_pipeline_clear_clicked)
        self.PB_ModulePresets_cbb.currentIndexChanged.connect(self.evt_PB_preset_cbb_changed)
        self.evt_PB_preset_cbb_changed()
        self.PB_easy_fast_chk.toggled.connect(self.evt_PB_automode_EF_chk_toggled)
        self.PB_easy_fast_chk.setChecked(True)
        self.evt_PB_automode_EF_chk_toggled(True)
        self.PB_easy_sensitive_chk.toggled.connect(self.evt_PB_automode_ES_chk_toggled)
        self.evt_clear_btn_disabled()
        self.PB_manual_expandall.clicked.connect(self.evt_manual_expandall_clicked)
        self.PB_manual_collapseall.clicked.connect(self.evt_manual_collapse_clicked)

        self.PB_SampleDirectory_btn_load.clicked.connect(self.evt_PB_sampledir_btn_load_clicked)
        self.PB_sampleDirectory = ""
        self.PB_SampleDirectory_list.itemDoubleClicked.connect(self.evt_PB_sampledir_itmdblclicked)

        #################VA modules############################
        #self.VA_VAnalysis_preprocessing_list.itemDoubleClicked.connect(self.VA_VAnalysis_itm_dblclicked)
        #self.VA_VAnalysis_classification_list.itemDoubleClicked.connect(self.VA_VAnalysis_itm_dblclicked)
        #self.VA_VAnalysis_SAnalysis_list.itemDoubleClicked.connect(self.VA_VAnalysis_itm_dblclicked)
        #self.VA_VAnalysis_modeling_list.itemDoubleClicked.connect(self.VA_VAnalysis_itm_dblclicked)

        self.VA_Arrange_btn.clicked.connect(self.VA_Arrange_btn_clicked)
        self.VA_CloseAll_btn.clicked.connect(self.VA_CloseAll_btn_clicekd)
#        self.VA_Ana_Layer_btn.clicked.connect(self.VA_Ana_Layer_btn_clicked)

        ##############Global parameters####################
        self.PB_SequencingType_chkbox_paired.toggled.connect(self.evt_global_parameters_paired_chk)
        self.PB_SequencingType_chkbox_single.toggled.connect(self.evt_global_parameters_single_chk)

        self.PB_SequenceOrigin_chkbox_Human.toggled.connect(self.evt_global_parameters_human_chk)
        self.PB_SequenceOrigin_chkbox_Mouse.toggled.connect(self.evt_global_parameters_mouse_chk)

        self.PB_SequencingPlatform_chkbox_illumina.toggled.connect(self.evt_global_parameters_illumina_chk)
        self.PB_SequenceingPlatform_chkbox_others.toggled.connect(self.evt_global_parameters_others_chk)
        self.PB_threads_spb.setValue(self.return_global_thread())


        ##############Meta Table####################
        self.PB_MetaTable_btn_load.clicked.connect(self.evt_PB_MetaTable_loadbtn_clicked)
        #self.PB_MetaTable_btn_save.clicked.connect(self.evt_PB_MetaTable_savebtn_clicked)
        ############# Tool parameter #####################
        self.PB_toolParameters_editable.toggled.connect(self.evt_PB_toolParameters_editbtn_toggled)

        ##############Metatable parameter ###############
        self.MetaTable = ""
        self.PB_metapara_sampletitle_cbb.currentTextChanged.connect(self.evt_metapara_sampletitle_changed)
        ###############PB pipeline outputs ################
        self.PB_outputs_expandall.clicked.connect(self.evt_pipline_outputs_expand_clicked)
        self.PB_outputs_collapseALL.clicked.connect(self.evt_pipeline_outputs_collapse_clicked)


        ################ToolBar setting ######################
        self.actionNew_Project.setIcon(QIcon("/".join([self.UiPath, "UX-UI-Icon_processed-33.png"])))
        self.actionOpen_Project.setIcon(QIcon("/".join([self.UiPath, "UX-UI-Icon_processed-06.png"])))
        self.actionSave_As.setIcon(QIcon("/".join([self.UiPath, "UX-UI-Icon_processed-20.png"])))
        self.actionContact_Us.setIcon(QIcon("/".join([self.UiPath, "UX-UI-Icon_processed-08.png"])))
        self.actionHuMMUS_Documentation.setIcon(QIcon("/".join([self.UiPath, "UX-UI-Icon_processed-12.png"])))

        ################ Setting DockWidgets ###################


        self.dockWidget_1.setWindowTitle("Queue Stack")
        self.MainJobs = QListWidget()
        self.SubJobs = QListWidget()
        self.MainJobs.setEditTriggers(QListWidget.EditTrigger.NoEditTriggers)
        self.SubJobs.setEditTriggers(QListWidget.EditTrigger.NoEditTriggers)
        self.QueueStackTab = QTabWidget()
        self.QueueStackTab.addTab(self.MainJobs, "Main Process")
        self.QueueStackTab.addTab(self.SubJobs, "Sub Process")
        self.MainJobs.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.SubJobs.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.dockWidget_1.setWidget(self.QueueStackTab)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockWidget_1)

        self.dockWidget_2.setWindowTitle("Status Log")

        self.lydock21 = QHBoxLayout()
        self.MainStatusLog = QPlainTextEdit()
        self.SubStatusLog = QPlainTextEdit()
        self.MainStatusLog.setReadOnly(True)
        self.SubStatusLog.setReadOnly(True)
        self.docktab= QTabWidget()
        self.docktab.addTab(self.MainStatusLog, "Main Process")
        self.docktab.addTab(self.SubStatusLog, "Sub Process")
        self.dockWidget_2.setWidget(self.docktab)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockWidget_2)

        self.dockWidget_3.setWindowTitle("System Log")
        self.MainProcessLogDock = QPlainTextEdit()
        self.SubProcessLogDock = QPlainTextEdit()
        self.MainProcessLogDock.setReadOnly(True)
        self.SubProcessLogDock.setReadOnly(True)
        self.SystemLogTab = QTabWidget()
        self.SystemLogTab.addTab(self.MainProcessLogDock, "Main Process")
        self.SystemLogTab.addTab(self.SubProcessLogDock, "Sub Process")
        self.dockWidget_3.setWidget(self.SystemLogTab)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockWidget_3)

        self.dockWidget_4.setWindowTitle("Note")
        self.dock4pte = QPlainTextEdit()
        self.dockWidget_4.setWidget(self.dock4pte)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockWidget_4)


        #self.actionNew_Project.triggered.connect(self.evt_NewProject_triggered)
        self.actionOpen_Project.triggered.connect(self.evt_OpenProject_triggered)
        self.actionQuit.triggered.connect(self.evt_QuitProgram_triggered)
        #self.actionNew_Project.triggered.connect(self.evt_NewProject_triggered)
        self.actionHuMMUS_Documentation.triggered.connect(self.evt_documentation_triggered)

        self.PB_threads_spb.valueChanged.connect(self.evt_globalparameters_changed)

        #################Proceed###############
        self.PB_Proceed_btn.clicked.connect(self.evt_PB_Proceed_btn_clicked)

        ##############Modify separate tool parameters##################
        self.initiate_tools(["All"])
        self.initiate_tool_dict()
        self.toolThreadToGlobalThreads()
        ################SubProcess Assignment#####################333
        self.ProcessStatusControl = ["Not Running", "Not Running", "Not Running", "Not Running"]


        ##################Diamond Memory Control#####################


        #####################Event Handler##############################

    def evt_diamond2_sensitivity_changed(self):
        if self.diamond.PB_diamond2_sensitivity_cbb.currentText() not in ["Fast", "Sensitive"]:
            self.diamond.PB_diamond2_memory_control_chk.setDisabled(True)
        elif self.diamond.PB_diamond2_sensitivity_cbb.currentText() in ["Fast", "Sensitive"]:
            self.diamond.PB_diamond2_memory_control_chk.setDisabled(False)

    def evt_globalparameters_changed(self, val):
        global_thread = val
        global_thread = self.PB_threads_spb.value()
        self.trimmomatic.PB_trimmomatic_thread_spb.setValue(global_thread)
        self.bowtie2.PB_bowtie2_thread_spb.setValue(global_thread)
        self.kraken2.PB_kraken2_thread_spb.setValue(global_thread)
        self.diamond.PB_diamond_threads_spb.setValue(global_thread)

    def toolThreadToGlobalThreads(self):
        global_thread = self.PB_threads_spb.value()
        self.trimmomatic.PB_trimmomatic_thread_spb.setValue(global_thread)
        self.bowtie2.PB_bowtie2_thread_spb.setValue(global_thread)
        self.kraken2.PB_kraken2_thread_spb.setValue(global_thread)
        self.diamond.PB_diamond_threads_spb.setValue(global_thread)

    def initiate_widget(self):
        self.widget_Ins = initiate_widgets()
        self.widget_Ins.return_rechk_metapara()
        self.PB_SequencingType_chkbox_single = self.widget_Ins.return_rechk_metapara()[0]
        self.PB_SequencingType_chkbox_paired = self.widget_Ins.return_rechk_metapara()[1]
        self.PB_SequenceOrigin_chkbox_Mouse = self.widget_Ins.return_rechk_metapara()[2]
        self.PB_SequenceOrigin_chkbox_Human = self.widget_Ins.return_rechk_metapara()[3]
        self.PB_SequencingPlatform_chkbox_illumina = self.widget_Ins.return_rechk_metapara()[4]
        self.PB_SequenceingPlatform_chkbox_others = self.widget_Ins.return_rechk_metapara()[5]
        self.PB_threads_spb = self.widget_Ins.return_rechk_metapara()[6]
        self.PB_MetaPara_gbx = self.widget_Ins.return_rechk_metapara()[7]
        self.PB_Proceed_btn = self.widget_Ins.return_rechk_metapara()[8]


    def initiate_tools(self, tools):
        self.tool_Ins = tool_instance()
        for tool in tools:
            if tool == "All":
                self.trimmomatic, self.trimmomatic_gbx = self.tool_Ins.return_tools()["Trimmomatic"][0], self.tool_Ins.return_tools()["Trimmomatic"][1]
                self.bowtie2, self.bowtie2_gbx = self.tool_Ins.return_tools()["Bowtie2"][0], self.tool_Ins.return_tools()["Bowtie2"][1]
                self.kraken2, self.kraken2_gbx = self.tool_Ins.return_tools()["Kraken2"][0], self.tool_Ins.return_tools()["Kraken2"][1]
                self.diamond, self.diamond_gbx = self.tool_Ins.return_tools()["Diamond"][0], self.tool_Ins.return_tools()["Diamond"][1]
                self.alpha, self.alpha_gbx = self.tool_Ins.return_tools()["Alpha"][0], self.tool_Ins.return_tools()["Alpha"][1]
                self.beta, self.beta_gbx = self.tool_Ins.return_tools()["Beta"][0], self.tool_Ins.return_tools()["Beta"][1]
                self.mwut, self.mwut_gbx  = self.tool_Ins.return_tools()["Mann-Whitney U Test"][0], self.tool_Ins.return_tools()["Mann-Whitney U Test"][1]
                self.ancombc, self.ancombc_gbx = self.tool_Ins.return_tools()["ANCOMBC"][0], self.tool_Ins.return_tools()["ANCOMBC"][1]
                self.lefse, self.lefse_gbx = self.tool_Ins.return_tools()["LEfSe"][0], self.tool_Ins.return_tools()["LEfSe"][1]
                self.songbird, self.songbird_gbx = self.tool_Ins.return_tools()["SongBird"][0], self.tool_Ins.return_tools()["SongBird"][1]
                self.randomforest, self.randomforest_gbx = self.tool_Ins.return_tools()["Random Forest"][0], self.tool_Ins.return_tools()["Random Forest"][1]
                self.load_analysis_input_source()
                self.diamond.PB_diamond2_sensitivity_cbb.currentTextChanged.connect(self.evt_diamond2_sensitivity_changed)

    def initiate_tool_dict(self):

        self.parameterGbx_dict = {"Trimmomatic": self.trimmomatic_gbx, \
                                    "Bowtie2": self.bowtie2_gbx, \
                                    "Kraken2": self.kraken2_gbx, \
                                    "Diamond": self.diamond_gbx, \
                                    "Alpha": self.alpha_gbx, \
                                    "Beta": self.beta_gbx, \
                                    "Mann-Whitney U Test": self.mwut_gbx, \
                                    "LEfSe": self.lefse_gbx, \
                                    "ANCOMBC": self.ancombc_gbx, \
                                    "SongBird": self.songbird_gbx, \
                                    "Random Forest": self.randomforest_gbx}



        self.toolClass_dict ={
            "Trimmomatic": [self.trimmomatic, "Preprocessing"], \
            "Bowtie2" : [self.bowtie2, "Preprocessing"], \
            "Kraken2" : [self.kraken2, "Classification"], \
            "Diamond" : [self.diamond, "Classification"], \
            "Alpha" : [self.alpha, "Statistical Analysis"], \
            "Beta" : [self.beta, "Statistical Analysis"], \
            "Mann-Whitney U Test" : [self.mwut, "Statistical Analysis"], \
            "LEfSe" : [self.lefse,"Statistical Analysis"], \
            "ANCOMBC" : [self.ancombc, "Statistical Analysis"], \
            "SongBird" : [self.songbird, "Statistical Analysis"], \
            "Random Forest" : [self.randomforest, "Modeling"]

        }

    def VA_Arrange_btn_clicked(self):
        self.VA_MDIArea.tileSubWindows()
    def VA_CloseAll_btn_clicekd(self):
        self.VA_MDIArea.closeAllSubWindows()

    def evt_LogStdOut_append_text(self, msg):
        self.dock3pte.appendPlainText(msg)
    def evt_PB_sampledir_itmdblclicked(self, itm):
        path = self.PB_sampleDirectory+"/"+itm.text()
        print(path)

    def evt_VA_list_load_clicked(self):
        self.RootPath = QDir.rootPath()
        self.ProjectDirTree = QFileSystemModel()
        self.ProjectDirTree.setRootPath(self.RootPath)
        self.ProjectDirTree.setFilter(QDir.Filter.NoDotAndDotDot | QDir.Filter.AllDirs)
        self.ProjectFileList = QFileSystemModel()
        self.ProjectFileList.setFilter(QDir.Filter.NoDotAndDotDot | QDir.Filter.Files)
        self.VA_VAnalysis_ProjectDirtree.setModel(self.ProjectDirTree)
        self.TreeRootIndex = self.ProjectDirTree.index("/".join([self.ProjectDir, self.ProjectTitle]))
        self.FileRootIndex = self.ProjectFileList.index("/".join([self.ProjectDir, self.ProjectTitle]))
        self.VA_VAnalysis_ProjectDirtree.setRootIndex(self.TreeRootIndex)
        self.VA_VAnalysis_ProjectDirtree.setExpandsOnDoubleClick(True)
        self.VA_VAnalysis_ProjectDirtree.setIndentation(10)
        self.VA_VAnalysis_ProjectDirtree.hideColumn(1)
        self.VA_VAnalysis_ProjectDirtree.hideColumn(2)
        self.VA_VAnalysis_ProjectDirtree.hideColumn(3)

        self.VA_VAnalysis_ProjectDirtree.clicked.connect(self.evt_ProjectDirTree_clicked)
        self.VA_VAnalysis_ProjectFilelist.setModel(self.ProjectFileList)
        self.VA_VAnalysis_ProjectFilelist.setRootIndex(self.FileRootIndex)
        self.VA_VAnalysis_ProjectFilelist.doubleClicked.connect(self.evt_ProjectFile_dblclicked)

    def evt_ProjectDirTree_clicked(self, idx):
        SelectedFilePath = self.ProjectDirTree.filePath(idx)
        path = self.ProjectDirTree.fileInfo(idx).absolutePath()

        self.VA_VAnalysis_ProjectFilelist.setRootIndex(self.ProjectFileList.setRootPath(SelectedFilePath))

    def evt_ProjectFile_dblclicked(self, idx):
        SelectedFilePath = self.ProjectFileList.filePath(idx)
        print(SelectedFilePath)
        if SelectedFilePath.endswith(".html"):
            self.NewSubWindow = NewSubWindow_with_QWB(SelectedFilePath)
            self.NewSubWindow.setWindowIcon(QIcon("/".join([self.UiPath, "HuMMUS_LOGO1.png"])))
            self.VA_MDIArea.addSubWindow(self.NewSubWindow)
            self.NewSubWindow.show()



    def evt_PB_sampledir_btn_load_clicked(self):
        sPath = QFileDialog.getExistingDirectory(self, "Load Sample Directory", os.path.expanduser("~"))
        if sPath:
            self.PB_SampleDirectory_list.clear()
            self.PB_sampleDirectory = sPath
            FileList = [fname for fname in os.listdir(sPath) if os.path.isfile("/".join([sPath, fname]))]
            delete_list =[]
            index_list =[]
            for fname in FileList:
                _, fextension = os.path.splitext(fname)
                if not fextension in [".fastq", "faa", ".fna", ".gz", ".bzip2"]:

                    warningmsg = QMessageBox()
                    warningmsg.setIcon(QMessageBox.Icon.Warning)
                    warningmsg.setWindowTitle("File Extension Warning")
                    warningmsg.setText("Not valid file type \n Do you sure to import the file?\n\n'{}'".format(fname))
                    btn1 = QPushButton("Import")
                    btn2 = QPushButton("Import All")
                    btn3 = QPushButton("No")
                    btn4 = QPushButton("Cancel")
                    warningmsg.addButton(btn1, QMessageBox.ButtonRole.YesRole)
                    warningmsg.addButton(btn2, QMessageBox.ButtonRole.YesRole)
                    warningmsg.addButton(btn3, QMessageBox.ButtonRole.NoRole)
                    warningmsg.addButton(btn4, QMessageBox.ButtonRole.NoRole)
                    btn1.clicked.connect(lambda x : None)
                    btn2.clicked.connect(lambda x: index_list.append("YesToAll"))
                    btn3.clicked.connect(lambda x: delete_list.append(fname))
                    btn4.clicked.connect(lambda x: index_list.append("cancel"))

                    if "YesToAll" in index_list:
                        break

                    warningmsg.show()
                    warningmsg.exec()

                if "cancel" in index_list:
                    FileList = []
                    self.PB_SampleDirectory_list.clear()
                    return

            for itm in delete_list:
                FileList.remove(itm)
            self.PB_SampleDirectory_list.addItems(FileList)
        else:
            pass
        self.PB_SampleDirectory_list.sortItems(Qt.SortOrder.AscendingOrder)

    def return_global_thread(self):
        if round(psutil.cpu_count()*(2/3)) %2 != 0:
            return round(psutil.cpu_count()*(2/3)) +1
        else:
            return round(psutil.cpu_count()*(2/3))

    def evt_pipline_outputs_expand_clicked(self):
        self.PB_outputs_tree.expandAll()
    def evt_pipeline_outputs_collapse_clicked(self):
        self.PB_outputs_tree.collapseAll()

    def evt_manual_expandall_clicked(self):
        self.PB_Modules_prep_tree.expandAll()
        self.PB_Modules_classification_tree.expandAll()
        self.PB_Modules_sanalysis_tree.expandAll()
        self.PB_Modules_modeling_tree.expandAll()
    def evt_manual_collapse_clicked(self):
        self.PB_Modules_prep_tree.collapseAll()
        self.PB_Modules_classification_tree.collapseAll()
        self.PB_Modules_sanalysis_tree.collapseAll()
        self.PB_Modules_modeling_tree.collapseAll()



    def evt_PB_append_output_list(self, module_list, action, mode = "Append"):
        output_dict = {"Trimmomatic" : ["Summary Table(ALL)", "Summary Plot(ALL)", "Summary Table(Sample)", "Summary Plot(Sample)"], \
                       "Bowtie2" : ["Summary Table(ALL)", "Summary Plot(ALL)", "Summary Table(Sample)", "Summary Plot(Sample)"], \
                       "Kraken2" : ["Taxonomic Table(Count)", "Taxonomic Table(Relative)"], \
                       "Diamond" : ["Gene family Table(Count)", "Gene family Table(Relatvie)", "Pathway Table(Count)", "Pathway Table(Relatvie)"], \
                       "Alpha" : ["Metric Table", "Alpha Plots"], \
                       "Beta" : ["Metric Table", "Beta PCoA Plots"], \
                       "Mann-Whitney U Test" : ["MWUT Table", "Vocalno Plot"], \
                       "LEfSe" : ["LDA Score Plot", "Cladogram", "Differentail Features"], \
                       "ANCOMBC" : ["Differential Table", "Bias_adj. Table", "DIfferential Plot"], \
                       "SongBird" : ["Differentials Table", "Differential Plot"], \
                       "Random Forest" : ["AUROC Plot"]}

        if action == "Append":
            for module in module_list:
                tmpTree = QTreeWidgetItem(self.PB_outputs_tree, [module])
                for itm in output_dict[module]:
                    tmpTree.addChild(QTreeWidgetItem([itm]))

        elif action == "Delete":
            itm_list = self.PB_outputs_tree.findItems(module_list, Qt.MatchFlag.MatchExactly, 0)

            for itm in itm_list:
                idx = self.PB_outputs_tree.indexFromItem(itm, 0)
                self.PB_outputs_tree.takeTopLevelItem(idx.row())


    def evt_global_parameters_paired_chk(self, chk):
        if chk:
            chkbool = False
            self.SType = "paired"
        else:
            chkbool = True
        self.PB_SequencingType_chkbox_single.setChecked(chkbool)

    def evt_global_parameters_single_chk(self, chk):
        if chk:
            chkbool = False
            self.Stype = "single"
        else:
            chkbool = True
        self.PB_SequencingType_chkbox_paired.setChecked(chkbool)

    def evt_global_parameters_human_chk(self, chk):
        if chk:
            paired_chk = False
        else:
            paired_chk = True
        self.PB_SequenceOrigin_chkbox_Mouse.setChecked(paired_chk)

    def evt_global_parameters_mouse_chk(self, chk):
        if chk:
            paired_chk = False
        else:
            paired_chk = True
        self.PB_SequenceOrigin_chkbox_Human.setChecked(paired_chk)
    def evt_global_parameters_illumina_chk(self, chk):
        if chk:
            paired_chk = False
        else:
            paired_chk = True
        self.PB_SequenceingPlatform_chkbox_others.setChecked(paired_chk)
    def evt_global_parameters_others_chk(self, chk):
        if chk:
            paired_chk = False
        else:
            paired_chk = True
        self.PB_SequencingPlatform_chkbox_illumina.setChecked(paired_chk)

    def evt_PB_MetaTable_loadbtn_clicked(self):

        sFile, sFilter = QFileDialog.getOpenFileName(self, "Load Metadata Table", os.path.expanduser("~"))
        if not sFile:
            return
        MetaTable = pd.read_csv(sFile, sep = "\t")
        if MetaTable.size == 0:
            return
        else:
            self.MetaTablePath = sFile
            self.clear_metapara_cbbs()
            print("Meta Data File '{}' Imported".format(sFile))
            MetaTable.fillna('', inplace = True)
            MetaTable = MetaTable.astype(dtype = "str")
            self.PB_MetaTable_widget.setRowCount(MetaTable.shape[0])
            self.PB_MetaTable_widget.setColumnCount(MetaTable.shape[1])
            self.PB_MetaTable_widget.setHorizontalHeaderLabels(MetaTable.columns.tolist())

            for row in MetaTable.iterrows():
                values = row[1]  ## tuple (index, value)
                for col_idx, value in enumerate(values):
                    if isinstance(value, (float, int)):
                        value = "{0:0, .00f}".format(value)
                    tableItem = QTableWidgetItem(str(value))
                    self.PB_MetaTable_widget.setItem(row[0], col_idx, tableItem)
            self.evt_PB_update_metaparameters(MetaTable.columns.tolist())
            self.MetaTable = MetaTable


    def evt_metapara_sampletitle_changed(self, val):
        if val != "sample_title" and val != "None" and val != "":
            QMessageBox.warning(self, "Warning", "Columns '{}' MUST contain the sample titles in the sample directory you loaded.".format(val))


    def clear_metapara_cbbs(self):
        self.PB_metapara_sampletitle_cbb.clear()
        self.PB_metapara_class1_cbb.clear()
        self.PB_metapara_sclass1_cbb.clear()


    def evt_PB_update_metaparameters(self, col_list):
        tmp_list = ["None"] + col_list
        if "sample_title" in col_list:
            QMessageBox.information(self, "Notice", "Sample title column, 'sample_title', was detected")
            self.PB_metapara_sampletitle_cbb.addItems(tmp_list)
            self.PB_metapara_sampletitle_cbb.setCurrentText("sample_title")
        else:
            QMessageBox.warning(self, "Notice", "Sample title column, 'sample_title', was not detected. You MUST manually specify the columns hodling sample titles in the sample directory you loaded")
            self.PB_metapara_sampletitle_cbb.addItems(tmp_list)
        self.PB_metapara_class1_cbb.addItems(tmp_list)
        self.PB_metapara_sclass1_cbb.addItems(tmp_list)


    def evt_pipeline_itm_clicked(self, itm):
        if not itm == None:
            chk = False if self.PB_toolParameters_editable.checkState() == Qt.CheckState.Unchecked else True
            if self.PB_toolparameter_layout.count() != 0:
                for idx in reversed(range(self.PB_toolparameter_layout.count())):
                    self.PB_toolparameter_layout.itemAt(idx).widget().setParent(None)

                self.PB_toolparameter_layout.addWidget(self.parameterGbx_dict[itm.text()])
            else:
                self.PB_toolparameter_layout.addWidget(self.parameterGbx_dict[itm.text()])
            self.evt_recursive_disabled(self.PB_toolparameter_layout, chk)

    def evt_clear_btn_disabled(self):
        if self.PB_ModulePresets_cbb.currentText() == "Auto":
            self.PB_ModulePresets_btn_clear.setDisabled(True)
        else:
            self.PB_ModulePresets_btn_clear.setDisabled(False)

    def evt_PB_pipeline_clear_clicked(self):
        self.initiate_tools(["All"])
        self.initiate_tool_dict()
        self.PB_pipeline_flow_list.clear()
        self.PB_prep_pipeline_list.clear()
        self.PB_class_pipeline_list.clear()
        self.PB_SA_pipeline_list.clear()
        self.PB_model_pipeline_list.clear()
        self.PB_outputs_tree.clear()
        if self.PB_toolparameter_layout.count() != 0:
            for idx in reversed(range(self.PB_toolparameter_layout.count())):
                self.PB_toolparameter_layout.itemAt(idx).widget().setParent(None)
        self.toolThreadToGlobalThreads()


    def evt_PB_pipeline_flow_logic(self):

        prep_itms = [self.PB_prep_pipeline_list.item(i).text() for i in range(self.PB_prep_pipeline_list.count())]
        class_itms = [self.PB_class_pipeline_list.item(i).text() for i in range(self.PB_class_pipeline_list.count())]
        stats_itms = [self.PB_SA_pipeline_list.item(i).text() for i in range(self.PB_SA_pipeline_list.count())]
        model_itms = [self.PB_model_pipeline_list.item(i).text() for i in range(self.PB_model_pipeline_list.count())]
        arrow = ">"
        #for i in range(self.PB_pipeline_flow_list.count()):
         #   self.PB_pipeline_flow_list.takeItem(i)
        self.PB_pipeline_flow_list.clear()
        self.PB_outputs_tree.clear()
        for module in [prep_itms, class_itms, stats_itms, model_itms]:

            if module == prep_itms and len(module) > 1:
                module = ("Trimmomatic", "Bowtie2")
            elif module == class_itms and len(module) == 2:
                if "Kraken2" in module and "Diamond" in module:
                    module = ("Kraken2", "Diamond")
            for itm in module:

                self.PB_pipeline_flow_list.addItem(itm)
                self.PB_pipeline_flow_list.addItem(arrow)
                self.evt_PB_append_output_list([itm], "Append")



    def evt_PB_automode_EF_chk_toggled(self, chk):
        self.evt_PB_pipeline_clear_clicked()
        itms = ["Trimmomatic", "Bowtie2", "Kraken2", "Diamond", "Alpha", "Beta", "Mann-Whitney U Test", "LEfSe",
                "ANCOMBC", "SongBird", "Random Forest"]
        self.PB_prep_pipeline_list.addItems(itms[:2])
        self.PB_class_pipeline_list.addItems(itms[2:4])
        self.PB_SA_pipeline_list.addItems(itms[4:10])
        self.PB_model_pipeline_list.addItem(itms[-1])
        self.evt_PB_append_output_list(itms, "Append")
        for itm in itms:
            self.PB_pipeline_flow_list.addItem(itm)
            self.PB_pipeline_flow_list.addItem(">")


    def evt_PB_automode_ES_chk_toggled(self, chk):

        self.evt_PB_pipeline_clear_clicked()
        itms = ["Trimmomatic", "Bowtie2","Kraken2", "Diamond", "Alpha", "Beta", "Mann-Whitney U Test", "LEfSe", "ANCOMBC", "SongBird", "Random Forest"]
        self.PB_prep_pipeline_list.addItems(itms[:2])
        self.PB_class_pipeline_list.addItems(itms[2:4])
        self.PB_SA_pipeline_list.addItems(itms[4:10])
        self.PB_model_pipeline_list.addItem(itms[-1])
        self.evt_PB_append_output_list(itms, "Append")
        for itm in itms:
            self.PB_pipeline_flow_list.addItem(itm)
            self.PB_pipeline_flow_list.addItem(">")
        self.bowtie2.PB_bowtie2_sensitive_cbb.setCurrentText("Sensitive")
        self.diamond.PB_diamond2_sensitivity_cbb.setCurrentText("Sensitive")



    def evt_PB_pipeline_list_dblclicked(self, itm):
        if self.PB_ModulePresets_cbb.currentText() != "Auto" and itm != None:
            itm_name = itm.text()
            if itm_name in self.module_dict["Preprocessing"]:
                module_selected = self.PB_prep_pipeline_list
            elif itm_name in self.module_dict["Classification"]:
                module_selected = self.PB_class_pipeline_list
            elif itm_name in self.module_dict["Statistical Analysis"]:
                module_selected = self.PB_SA_pipeline_list
            else:
                module_selected = self.PB_model_pipeline_list

            for i in range(module_selected.count()):
                if module_selected.item(i) != None:
                    if module_selected.item(i).text() == itm_name:
                        module_selected.takeItem(i)

            self.evt_PB_pipeline_flow_logic()

            if self.PB_toolparameter_layout.count() != 0:
                itm_gbx = self.PB_toolparameter_layout.itemAt(0).widget()
                itm_gbx_label = self.PB_toolparameter_layout.itemAt(0).widget().layout().itemAt(0).widget().text()
                if itm_gbx_label == itm_name:
                    for idx in reversed(range(self.PB_toolparameter_layout.count())):
                        self.PB_toolparameter_layout.itemAt(idx).widget().setParent(None)

            self.evt_pipeline_itm_clicked(module_selected.currentItem())

    def evt_PB_Modules_tree_dblclicked(self, itm, col):

        itm_name = itm.text(col)
        if itm_name in self.module_dict["Preprocessing"]:
            module_selected = self.PB_prep_pipeline_list
        elif itm_name in self.module_dict["Classification"]:
            module_selected = self.PB_class_pipeline_list
        elif itm_name in self.module_dict["Statistical Analysis"]:
            module_selected = self.PB_SA_pipeline_list
        else:
            module_selected = self.PB_model_pipeline_list

        itms = self.get_PV_Module_itm_name(itm_name)

        ppl_itm_list = [module_selected.item(i).text() for i in range(module_selected.count())]
        new_itms = []
        overlap_itms = []
        if len(ppl_itm_list) > 0:
            if type(itms) != str:
                for i in itms:
                    if i in ppl_itm_list:
                        overlap_itms.append(i)
                    else:
                        new_itms.append(i)

                new_itms_names = ", ".join([idx1 for idx1 in new_itms]) if type(new_itms) != str else new_itms
                overlap_itms_names = ", ".join([idx2 for idx2 in overlap_itms]) if type(overlap_itms) != str else overlap_itms

                if len(new_itms) != 0 and len(overlap_itms) != 0:
                    QMessageBox.warning(self, "Notice", "'{}' already exist in the pipeline. \n Only '{}' will be appended.  ".format(overlap_itms_names, new_itms_names))
                    module_selected.addItems(new_itms)

                elif len(new_itms) !=0 and len(overlap_itms) == 0:
                    module_selected.addItems(new_itms)

                elif len(new_itms) == 0:
                    QMessageBox.warning(self, "Notice", "'{}' already exist in the piepline.  ".format(overlap_itms_names))
            elif type(itms) == str:
                if itms in ppl_itm_list:
                    QMessageBox.warning(self, "Notice", "'{}' already exist in the piepline.  ".format(itms))
                else:
                    module_selected.addItem(itms)
        else:
            if type(itms) == str:
                module_selected.addItem(itms)
            else:
                module_selected.addItems(itms)

        self.evt_PB_pipeline_flow_logic()

    def get_module_name(self):
        return {"Preprocessing" : ["Preprocessing", "Trimming&QC", "Trimmomatic", "Decontamination", "Bowtie2"], \
                "Classification" : ["Classification", "Taxonomic Profiling", "Kraken2", "Functional Profiling", "Diamond", ], \
                "Statistical Analysis" : ["Statistical Analysis", "Diversity", "Alpha", "Beta", "Differential Abundance", "Mann-Whitney U Test", "LEfSe", "ANCOMBC", "SongBird"], \
                "Modeling" : ["Random Forest"]}

    def get_PV_Module_itm_name(self, name):
        if name == "Preprocessing":
            return "Trimmomatic", "Bowtie2"
        elif name == "Trimming&QC":
            return "Trimmomatic"
        elif name == "Decontamination":
            return "Bowtie2"
        elif name == "Classification":
            return "Kraken2", "Diamond"
        elif name == "Taxonomic Profiling":
            return "Kraken2"
        elif name == "Functional Profiling":
            return "Diamond"
        elif name == "Statistical Analysis":
            return "Alpha", "Beta", "Mann-Whitney U Test", "LEfSe", "ANCOMBC", "SongBird"
        elif name == "Diversity":
            return "Alpha", "Beta"
        elif name == "Differential Abundance":
            return "Mann-Whitney U Test", "LEfSe", "ANCOMBC", "SongBird"
        elif name == "Modeling":
            return "Random Forest"
        else:
            return name

    def evt_PB_preset_cbb_changed(self, index = False):
        self.evt_clear_btn_disabled()
        self.PB_Modules_automode_gbx.setDisabled(index)
        splitter = self.PB_Modules_Manual_layout.itemAt(1).widget()
        for i in range(splitter.count()):
            splitter.widget(i).collapseItem(splitter.widget(i).topLevelItem(0))
        self.evt_PB_pipeline_clear_clicked()
        self.evt_recursive_disabled(self.PB_Modules_Manual_layout, index)
        if index == 0 and self.PB_easy_fast_chk.isChecked() == 1:
            self.evt_PB_automode_EF_chk_toggled(True)
        elif index == 0 and self.PB_easy_fast_chk.isChecked() == 0:
            self.PB_easy_fast_chk.setChecked(True)
            self.PB_easy_sensitive_chk.setChecked(index)




    def evt_recursive_disabled(self, layout, chk, action = "Null"):
        for idx1 in range(layout.count()):
            itm1 = layout.itemAt(idx1)

            if type(itm1) == QWidgetItem:
                itm1.widget().setEnabled(chk)

            elif type(itm1) == QHBoxLayout or type(itm1) == QVBoxLayout:

                for idx2 in range(itm1.count()):

                    itm2 = itm1.itemAt(idx2)

                    if type(itm2) == QWidgetItem:
                        itm2.widget().setEnabled(chk)
                    elif type(itm2) == QHBoxLayout or type(itm2) == QVBoxLayout:
                        self.evt_recursive_disabled(itm2, chk)

    def evt_PB_toolParameters_editbtn_toggled(self, chk):

        self.evt_recursive_disabled(self.PB_toolparameter_layout, chk)

    def evt_VA_Layer_add_clicked(self):
        self.lyGridLayer.addWidget(self.NewVALayer(), 0, 0)



    def evt_NewProject_triggered(self):
        self.NewProject_object = QDialog()
        self.NewProject = create_project.Ui_Dialog()
        self.NewProject.setupUi(self.NewProject_object)
        self.Location = self.NewProject.Location
        self.Loadbtn = self.NewProject.Load
        self.projecttitle = self.NewProject.Project_Title
        self.NewProject.Project_Title
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
                #qprocess = QProcessDistatched(self.ProjectDir, self.ProjectTitle, self.ProgramPath, self.Theme)
                #qprocess.run()




    def evt_OpenProject_triggered(self):
        sFile, sFilter = QFileDialog.getOpenFileName(self, "Open Project", os.path.expanduser("~")) #"HuMMUS Project File (*.hmsp)"
        if sFile:
            print(sFile)
        else:
            pass

    def evt_documentation_triggered(self):
        window = TreeWidget.DlgMain()
        window.show()
        window.exec()

    def evt_QuitProgram_triggered(self):
        sys.exit(0)



    def evt_web_drop_event(self):
        self.web.setUrl(QUrl.fromUserInput(self.url))


    def ToolBar_style(self):
        sStyle = """
            QToolBar {
                background-color: #ECF7FF;
                }
            """
        return sStyle

    def MainWindow_style(self):
        sStyle = """
            QMainWindow {
                background-color: #F6FBFF;
                }
            """
        return sStyle

    def evt_logo_style(self):
        sStyle = r"""
            QLabel {
                background-image: url(C:/Users/Han-June%20Kim/Documents/HJKIM/NBL/pyqt/Untitled-4.png);
                }"""
        return sStyle



    def PB_merging_parameters(self):
        SeqType = self.PB_SequencingType_chkbox_single.text()


    def evt_SystemMonitor(self):
        self.worker = WorkerThread()
        self.worker.start()
        self.worker.update_cpu.connect(self.evt_CpuUpdate)
        self.worker.update_ram.connect(self.evt_RamUpdate)

    def evt_CpuUpdate(self, val):
        self.CPUBar.setFormat("%.02f %%" % val)
        self.CPUBar.setValue(val)
    def evt_RamUpdate(self, val):
        self.RAMBar.setFormat("%.02f %%" % val)
        self.RAMBar.setValue(val)


    def evt_PB_Proceed_btn_clicked(self):
        if self.PB_Proceed_btn.text() == "Terminate":
            for num, status in enumerate(self.ProcessStatusControl):
                if status == "Running":
                    if num == 0:
                        self.MainThread.wait()

                    if num == 1:
                        self.SubWorker1.SubProcess.kill()
                    if num == 2:
                        self.SubWorker2.SubProcess.kill()
                    if num == 3:
                        self.SubWorker3.SubProcess.kill()

            QMessageBox.critical(self, "Critical", "All the running process have been terminated.")
            self.PB_Proceed_btn.setText("Proceed")
        else:
            if self.PB_pipeline_flow_list.count() == 0:
                QMessageBox.critical(self, "Error", "You must select at least one module")
                return
            chk_pipeline_valid = self.validate_pipeline_build()

            if not chk_pipeline_valid:
                return

            self.module_listnw =[]
            for i in [self.PB_pipeline_flow_list.item(i).text() for i in range(self.PB_pipeline_flow_list.count())]:
                if not i == ">":
                    self.module_listnw.append(i)


            self.btnProceednw = QPushButton("Proceed")
            self.btnRecheckPara = QPushButton("Recheck")
            self.btnCancelnw = QPushButton("Cancel")

            self.proceednw_ans = QMessageBox()
            self.proceednw_ans.setIcon(QMessageBox.Icon.Question)
            self.proceednw_ans.setWindowTitle("Important")
            self.proceednw_ans.setText("When the pipeline starts to run, the parameters cannot be changed during run\n Are you sure you want to precced?")
            self.proceednw_ans.addButton(self.btnProceednw, QMessageBox.ButtonRole.YesRole)
            self.proceednw_ans.addButton(self.btnRecheckPara, QMessageBox.ButtonRole.HelpRole)
            self.proceednw_ans.addButton(self.btnCancelnw, QMessageBox.ButtonRole.NoRole)
            self.btnProceednw.clicked.connect(self.evt_proceedWindow_proceedbtn_clicked)
            self.btnCancelnw.clicked.connect(self.evt_proceedWindow_cancelbtn_clicked)
            self.btnRecheckPara.clicked.connect(self.evt_proceedWindow_recheckbtn_clicked)
            self.proceednw_ans.show()
            self.proceednw_ans.exec()


    def evt_proceedWindow_proceedbtn_clicked(self):
        QMessageBox.information(self, "Information", "Pipeline successfully starts!\n You can track the progress of the pipeline through the progress windows.")
        self.generate_parameter()
        self.RunPipelinewithArguments()
        self.MainPrgBar.setValue(0)
        self.PB_Proceed_btn.setText("Terminate")
        self.MainProcessLogDock.clear()
        self.evt_PB_pipeline_clear_clicked()

    def PreparePipelineRunning(self):
        self.MainPrgBar.setValue(0)
        self.PB_Proceed_btn.setDisabled(True)



    def evt_proceedWindow_cancelbtn_clicked(self):
        return

    def evt_proceedWindow_recheckbtn_clicked(self):
        NewDialog = QDialog()
        lyMain = QVBoxLayout()
        ly1stRow = QHBoxLayout()
        ly2ndRow = QHBoxLayout()
        lybtns = QHBoxLayout()
        lybtn1 = QPushButton("Proceed")
        lybtn2 = QPushButton("Cancel")
        self.PB_Proceed_btn.hide()

        lybtns.addWidget(self.PB_MetaPara_gbx)
        lybtns.addStretch(1)
        lybtns.addWidget(lybtn1)
        lybtns.addWidget(lybtn2)
        lybtns.addStretch(1)

        containerGbx = QGroupBox("Pipeline Paramters")
        containerGbx.setLayout(lyMain)

        for module in self.module_listnw:

            if ly1stRow.count() < 5:

                self.parameterGbx_dict[module]
                if not self.parameterGbx_dict[module].isEnabled():
                    self.parameterGbx_dict[module].setDisabled(False)
                ly1stRow.addWidget(self.parameterGbx_dict[module])
            else:
                self.parameterGbx_dict[module] = self.parameterGbx_dict[module]
                if not self.parameterGbx_dict[module].isEnabled():
                    self.parameterGbx_dict[module].setDisabled(False)
                ly2ndRow.addWidget(self.parameterGbx_dict[module])

        if len(self.module_listnw) in [1,2,3]:
            ly1stRow.addStretch(1)
        if len(self.module_listnw) in [6,7,8]:
            ly2ndRow.addStretch(1)

        lybtn2.clicked.connect(lambda x : NewDialog.reject())
        lybtn2.clicked.connect(self.show_proceed_btn)
        lybtn1.clicked.connect(lambda x: NewDialog.reject())
        lybtn1.clicked.connect(self.evt_recheck_proceed_btn_clicked)
        lyMain.addLayout(lybtns)
        lyMain.addLayout(ly1stRow)
        lyMain.addLayout(ly2ndRow)
        NewDialog.setLayout(lyMain)
        NewDialog.setMinimumWidth(1600)
        NewDialog.open()
        NewDialog.exec()
        self.show_proceed_btn()

    def show_proceed_btn(self):
        self.PB_Proceed_btn.show()
        self.PB_UpperMostLayout.insertWidget(0, self.PB_MetaPara_gbx)

    def evt_recheck_proceed_btn_clicked(self):
        self.show_proceed_btn()
        QMessageBox.information(self, "Information",
                                "Pipeline successfully starts!\n You can track the progress of the pipeline through the progress windows.")

        self.generate_parameter()
        self.RunPipelinewithArguments()
        self.PB_Proceed_btn.setText("Terminate")
        self.MainPrgBar.setValue(0)
        self.evt_PB_pipeline_clear_clicked()

    def validate_pipeline_build(self):
        if self.PB_ModulePresets_cbb.currentText() == "Auto":
            validate_automode = True
            if validate_automode:
                validate_automode = self.chk_SampleDir_Empty()
            if validate_automode:
                validate_automode = self.chk_MetaTable_Empty()
            if validate_automode:
                validate_automode = self.chk_tablepara_empty()
            if validate_automode:
                validate_automode = self.chk_sample_match()
            return validate_automode

        elif self.PB_ModulePresets_cbb.currentText() == "Manual":
            validate_manualmode = True
            PipelineFlow_list = [self.PB_pipeline_flow_list.item(row).text() for row in range(self.PB_pipeline_flow_list.count())]
            if validate_manualmode:
                if "Trimmomatic" in PipelineFlow_list or "Bowtie2" in PipelineFlow_list:
                    validate_manualmode = self.chk_SampleDir_Empty()
                    if validate_manualmode:
                        validate_manualmode = self.chk_MetaTable_Empty()
                    if validate_manualmode:
                        validate_manualmode = self.chk_sample_match()

                    if validate_manualmode:
                        if "Kraken2" in PipelineFlow_list or "Diamond" in PipelineFlow_list:
                            if validate_manualmode:
                                validate_manualmode = self.chk_tablepara_empty()

                        elif "Kraken2" not in PipelineFlow_list and "Diamond" not in PipelineFlow_list:
                            for tool in PipelineFlow_list:
                                if not tool == ">":
                                    if self.toolClass_dict[tool][1] in ["Statistical Analysis", "Modeling"]:
                                        if self.toolClass_dict[tool][0].Input_source_cbb.count() == 1 and self.toolClass_dict[tool][0].Input_source_cbb.currentText() == "None":
                                            QMessageBox.critical(self, "Error", "There are no input tables for module '{}'. Please Run the following module first: \n'Kraken2' or Diamond'".format(tool))
                                            validate_manualmode = False
                                        if self.toolClass_dict[tool][0].Input_source_cbb.count() != 1 and self.toolClass_dict[tool][0].Input_source_cbb.currentText() == "None":
                                            QMessageBox.warning(self, "Error", "You MUST specify input tables for the module '{}'. Check 'Input' parameter.".format(tool))
                                            validate_manualmode = False

                elif "Trimmomatic" not in PipelineFlow_list and "Bowtie2" not in PipelineFlow_list:
                    if "Kraken2" in PipelineFlow_list or "Diamond" in PipelineFlow_list:
                        validate_manualmode = self.chk_SampleDir_Empty()
                        if validate_manualmode:
                            validate_manualmode = self.chk_MetaTable_Empty()
                        if validate_manualmode:
                            validate_manualmode = self.chk_tablepara_empty()
                        if validate_manualmode:
                            validate_manualmode = self.chk_sample_match()

                    elif "Kraken2" not in PipelineFlow_list and "Diamond" not in PipelineFlow_list:
                        for tool in PipelineFlow_list:
                            if not tool == ">":
                                if self.toolClass_dict[tool][1] in ["Statistical Analysis", "Modeling"]:
                                    if self.toolClass_dict[tool][0].Input_source_cbb.count() == 1 and self.toolClass_dict[tool][0].Input_source_cbb.currentText() == "None":
                                        QMessageBox.critical(self, "Error", "There are no input tables for module '{}'. Please Run the following module first: \n'Kraken2' or Diamond'".format(tool))
                                        validate_manualmode = False
                                    if self.toolClass_dict[tool][0].Input_source_cbb.count() != 1 and self.toolClass_dict[tool][0].Input_source_cbb.currentText() == "None":
                                        QMessageBox.critical(self, "Error", "You MUST specify input tables for the module '{}'. Check 'Input' parameter.".format(tool))
                                        validate_manualmode = False

            if validate_manualmode:
                validate_manualmode = self.asssign_pipeline_title()
            return validate_manualmode


    def chk_SampleDir_Empty(self):

        if self.PB_SampleDirectory_list.count() == 0:
            QMessageBox.critical(self, "Error", "Sample directory MUST be imported")
            return False
        else:
            return True


    def chk_MetaTable_Empty(self):
        if self.PB_MetaTable_widget.rowCount() == 0:
            QMessageBox.critical(self, "Error", "Metadat table is MUST be imported")
            return False
        else:
            return True

    def chk_tablepara_empty(self):
        if self.PB_metapara_sampletitle_cbb.currentText() == "None" or self.PB_metapara_class1_cbb.currentText() == "None":
            QMessageBox.critical(self, "Error", "Sample title column and at least one class column MUST be specified")
            return False
        else:
            return True


    def chk_sample_match(self):
        self.Metatable_sample_col = self.MetaTable[self.PB_metapara_sampletitle_cbb.currentText()].tolist()

        self.chk_unmatched_bool = True
        self.UnMatchedSample = []
        Sample_dir_list = [self.PB_SampleDirectory_list.item(row).text() for row in range(self.PB_SampleDirectory_list.count())]
        idx1, idx2 = self.find_match_idx()
        self.sample_title_idx1, self.sample_title_idx2 = idx1, idx2
        for dir_sample in Sample_dir_list:
            if dir_sample[idx1:idx2] not in self.Metatable_sample_col:
                self.UnMatchedSample.append(dir_sample)

        if not len(self.UnMatchedSample) == 0:

            unmatched_text = "The metatable does NOT contain the information for the following {} files you loaded.\n Do you want to exclude the samples?".format(str(len(self.UnMatchedSample)))
            dialog_noinput_close = self.msg_for_unmatched_sample(self.UnMatchedSample, unmatched_text, "Unmatched")

            if dialog_noinput_close == False:
                self.chk_unmatched_bool = False
            elif dialog_noinput_close == True and self.chk_unmatched_bool == True:
                self.chk_unmatched_bool = True
        if self.chk_unmatched_bool:
            if self.PB_SequencingType_chkbox_paired.isChecked():
                self.missing_sample = []
                include_sample_list = [self.PB_SampleDirectory_list.item(row).text() for row in range(self.PB_SampleDirectory_list.count())]
                for sample in include_sample_list:
                    count = 0
                    sample_title = sample[idx1:idx2]
                    for c_sample in include_sample_list:
                        if sample_title == c_sample[idx1:idx2]:
                            count +=1

                    if count != 2:
                        self.missing_sample.append(sample)
                if len(self.missing_sample) != 0:

                    missing_text = "The following {} files does NOT have their paired sample files.\nDo you want to exclude the samples?".format(str(len(self.missing_sample)))
                    final_sample_set = set([i[idx1:idx2] for i in [self.PB_SampleDirectory_list.item(row).text() for row in range(self.PB_SampleDirectory_list.count())]])
                    dialog_noinput_close = self.msg_for_unmatched_sample(self.missing_sample, missing_text, "Missing", final_sample_set)

                    if dialog_noinput_close == False:
                        self.chk_unmatched_bool = False
                    elif dialog_noinput_close == True and self.chk_unmatched_bool == True:
                        self.chk_unmatched_bool = True
                ##Final check samples##
                self.valid_sample_list = []

                for dir_sample in [self.PB_SampleDirectory_list.item(row).text() for row in range(self.PB_SampleDirectory_list.count())]:
                    sort_container = []
                    for sub_dir_sample in [self.PB_SampleDirectory_list.item(row).text() for row in range(self.PB_SampleDirectory_list.count())]:
                        if dir_sample != sub_dir_sample and dir_sample[idx1:idx2] == sub_dir_sample[idx1:idx2]:
                            if dir_sample not in self.valid_sample_list and sub_dir_sample not in self.valid_sample_list:
                                sort_container.append(dir_sample)
                                sort_container.append(sub_dir_sample)
                                sort_container.sort()
                                print(sort_container)
                                self.valid_sample_list.append(sort_container[0])
                                self.valid_sample_list.append(sort_container[1])
                if len(self.valid_sample_list) != self.PB_SampleDirectory_list.count():
                    QMessageBox.critical(self, "Error", "The forward and reverse sample number was not matched. \nCheck the name of samples.")
                    self.chk_unmatched_bool = False
                #####2nd Final check#####

                self.valid_forward_list = self.valid_sample_list[::2]
                self.valid_reverse_list = self.valid_sample_list[1::2]


                for forward, reverse in zip(self.valid_forward_list, self.valid_reverse_list):
                    if forward[idx1:idx2] != reverse[idx1:idx2] or forward == reverse:
                        QMessageBox.critical(self, "Error", "The forward {} and reverse {} samples were NOT paired. \nCheck the name of samples.")
                        self.chk_unmatched_bool = False
                ######Sample title validation#####
                self.valid_sample_title = [sample[idx1:idx2] for sample in self.valid_forward_list]
                self.valid_sample_title_tmp = [sample[idx1:idx2] for sample in self.valid_reverse_list]
                if not self.valid_sample_title == self.valid_sample_title_tmp:
                    QMessageBox.critical(self, "Error", "The name of forward and reverse samples were not matched. \nCheck the name of the samples.")

            #############Single Checked###################
            elif self.PB_SequencingType_chkbox_single.isChecked():
                self.Single_dir_samples = [self.PB_SampleDirectory_list.item(row).text() for row in range(self.PB_SampleDirectory_list.count())]
                self.valid_sample_list = []
                self.single_duplicate = set()
                self.partial_duplicate = []
                for idx in range(len(self.Single_dir_samples)):
                    sample = self.Single_dir_samples[idx]
                    if sample not in self.Single_dir_samples[idx+1:]:
                        self.valid_sample_list.append(sample)
                    else:
                        self.single_duplicate.add(sample)
                if self.single_duplicate:
                    QMessageBox.warning(self, "Error", "The following sample files were identified as duplicates. \nIn 'Single sequencing type' Mode, evry file name MUST be discriminative.".format(", ".join(i for i in self.single_duplicate)))
                    self.chk_unmatched_bool = False
                    return self.chk_unmatched_bool
                for num, sample in enumerate(self.Single_dir_samples):

                    for sub_sample in self.Single_dir_samples:
                        if sample != sub_sample and sample[idx1:idx2] == sub_sample[idx1:idx2]:
                            tmp = [sample, sub_sample]
                            tmp.sort()
                            sample_concat = ", ".join(tmp)
                            if sample_concat not in self.partial_duplicate:
                                self.partial_duplicate.append(sample_concat)
                if self.partial_duplicate:
                    final_single_text = "The following sample files are sharing partial-mathced sample title. \nIn 'Single' sequencing mode, everty file name MUST be discriminative.\nCheck the file names and fix manually."
                    indicator = "single_partial_matched"

                    dialog_noinput_close = self.msg_for_unmatched_sample(self.partial_duplicate, final_single_text, indicator, idx1 = idx1, idx2 = idx2)

                    if dialog_noinput_close == False:
                        self.chk_unmatched_bool = False
                    elif dialog_noinput_close == True and self.chk_unmatched_bool == True:
                        self.chk_unmatched_bool = True



        return self.chk_unmatched_bool

    def find_match_idx(self):
        dir_samples = [self.PB_SampleDirectory_list.item(row).text() for row in range(self.PB_SampleDirectory_list.count())]
        Metatable_samples = self.MetaTable[self.PB_metapara_sampletitle_cbb.currentText()].tolist()
        for dir_sample in dir_samples:
            dir_sample = str(dir_sample)
            for table_sample in Metatable_samples:
                table_sample = str(table_sample)
                for idx in range((len(dir_sample) - len(table_sample))):
                    if dir_sample[idx:idx+len(table_sample)] == table_sample:
                        idx1 = idx
                        idx2 = idx+len(table_sample)
                        return idx1, idx2
        return 0, -1


    def asssign_pipeline_title(self):
        self.pipelinetitleldt = QLineEdit()
        explabel = QLabel("Please Enter the title of the pipeline.\nThis title will be used as idicators of the outputs.")
        Proceedbtn = QPushButton("Proceed")
        Proceedbtn.clicked.connect(self.evt_pipelinetitle_proceed_clicked)
        Cancelbtn = QPushButton("Cancel")
        Cancelbtn.clicked.connect(self.evt_pipelinetitle_cancel_clicked)
        self.dialog_noinput_close = False
        self.assigntitle = QDialog()
        self.assigntitle.setWindowTitle("Pipeline Title")
        lyMain = QVBoxLayout()
        lyBtn = QHBoxLayout()
        lyLabel = QHBoxLayout()
        msg_icon  = QLabel("")
        msg_icon.setPixmap(app.style().standardIcon(QStyle.StandardPixmap.SP_MessageBoxInformation).pixmap(32))
        lyBtn.addStretch(1)
        lyBtn.addWidget(Proceedbtn)
        lyBtn.addWidget(Cancelbtn)
        lyLabel.addWidget(msg_icon)
        lyLabel.addWidget(explabel)
        lyMain.addLayout(lyLabel)
        lyMain.addWidget(self.pipelinetitleldt)
        lyMain.addLayout(lyBtn)
        self.assigntitle.setLayout(lyMain)
        self.assigntitle.open()
        self.assigntitle.exec()
        return self.dialog_noinput_close

    def evt_pipelinetitle_proceed_clicked(self):
        if len(self.pipelinetitleldt.text()) < 3:
            QMessageBox.warning(self, "Error", "The pipeline title MUST be more than '3' letters")
        else:
            self.PipeLineTitle = self.pipelinetitleldt.text()
            self.dialog_noinput_close = True
            self.assigntitle.close()

    def evt_pipelinetitle_cancel_clicked(self):
        self.unmatched_missing_msg_dialog.close()
        self.dialog_noinput_close = False
        self.assigntitle.close()



    def msg_for_unmatched_sample(self, list, text, indicator, final = None, idx1 = None, idx2 = None):
        self.final_sample_set = final
        self.dialog_noinput_close = False
        self.unmatched_missing_msg_dialog = QDialog()
        self.unmatched_missing_msg_dialog.setWindowTitle("Error")
        lyMain = QVBoxLayout()
        lybtns = QHBoxLayout()
        lyLabels = QHBoxLayout()
        msg_label = QLabel(text)
        msg_icon = QLabel("")
        msg_icon.setPixmap(app.style().standardIcon(QStyle.StandardPixmap.SP_MessageBoxCritical).pixmap(32))



        msg_cancelbtn = QPushButton("Cancel")
        if indicator == "Unmatched":
            msg_excludebtn = QPushButton("Exclude")
            msg_excludebtn.clicked.connect(self.evt_chk_unmatched_exclude_clicked)
            msg_cancelbtn.clicked.connect(self.evt_chk_unmatched_cancel_clicked)
            msg_ptl = QPlainTextEdit("{}".format("\n".join(sample for sample in list)))
        elif indicator == "Missing":
            msg_excludebtn = QPushButton("Exclude")
            msg_excludebtn.clicked.connect(self.evt_chk_missing_exclude_clicked)
            msg_cancelbtn.clicked.connect(self.evt_chk_unmatched_cancel_clicked)
            msg_ptl = QPlainTextEdit("{}".format("\n".join(sample for sample in list)))
        elif indicator == "single_partial_matched":
            msg_excludebtn = QPushButton("Fix Manually")
            msg_ignorebtn = QPushButton("Ignore and Proceed")
            lybtns.addWidget(msg_ignorebtn)
            msg_ignorebtn.clicked.connect(self.evt_chk_ignorebtn_clicked)
            msg_excludebtn.clicked.connect(self.evt_chk_single_partial_clicked)
            msg_cancelbtn.clicked.connect(self.evt_chk_unmatched_cancel_clicked)
            single_duplicate_list = []
            for i in list:
                samples = i.split(", ")
                samples.sort()
                name1 = samples[0][:idx1]+ " '" + samples[0][idx1:idx2] + "' "+samples[0][idx2:]
                name2 = samples[1][:idx1] + " '" + samples[1][idx1:idx2] + "' " + samples[1][idx2:]
                t_name = name1 + "  <-->  " + name2
                single_duplicate_list.append(t_name)
            msg_ptl = QPlainTextEdit("{}".format("\n".join(sample for sample in single_duplicate_list)))

        msg_ptl.setReadOnly(True)
        lyLabels.addWidget(msg_icon)
        lyLabels.addWidget(msg_label)
        lyLabels.addStretch(1)
        lyMain.addLayout(lyLabels)
        lybtns.addStretch(1)
        lybtns.addWidget(msg_excludebtn)
        lybtns.addWidget(msg_cancelbtn)
        lyMain.addWidget(msg_ptl)
        lyMain.addLayout(lybtns)
        self.unmatched_missing_msg_dialog.setLayout(lyMain)
        self.unmatched_missing_msg_dialog.open()
        self.unmatched_missing_msg_dialog.exec()
        return self.dialog_noinput_close

    def load_analysis_input_source(self):
        path = os.path.dirname(os.path.realpath(__file__))+"/HuMMUS_input_source_test/"
        table_list = os.listdir(path)
        if table_list:
            self.alpha.Input_source_cbb.addItems(table_list)
            self.beta.Input_source_cbb.addItems(table_list)
            self.mwut.Input_source_cbb.addItems(table_list)


    def evt_chk_unmatched_exclude_clicked(self):
        for itm in self.UnMatchedSample:

            MatchedItm = self.PB_SampleDirectory_list.findItems(itm, Qt.MatchFlag.MatchExactly)
            for mitm in MatchedItm:
                self.PB_SampleDirectory_list.takeItem(self.PB_SampleDirectory_list.indexFromItem(mitm).row())
        self.PB_SampleDirectory_list.sortItems(Qt.SortOrder.AscendingOrder)
        self.unmatched_missing_msg_dialog.close()
        QMessageBox.information(self, "Notice", "{} samples were removed from sample directory".format(str(len(self.UnMatchedSample))))
        self.dialog_noinput_close = True

    def evt_chk_ignorebtn_clicked(self):
        self.unmatched_missing_msg_dialog.close()
        self.dialog_noinput_close = True

    def evt_chk_unmatched_cancel_clicked(self):
        self.chk_unmatched_bool = False
        self.unmatched_missing_msg_dialog.close()

    def evt_chk_missing_exclude_clicked(self):
        for itm in self.missing_sample:

            missingItm = self.PB_SampleDirectory_list.findItems(itm, Qt.MatchFlag.MatchExactly)
            for mitm in missingItm:
                self.PB_SampleDirectory_list.takeItem(self.PB_SampleDirectory_list.indexFromItem(mitm).row())
        self.PB_SampleDirectory_list.sortItems(Qt.SortOrder.AscendingOrder)
        self.unmatched_missing_msg_dialog.close()
        QMessageBox.information(self, "Notice", "{} samples were removed from sample directory.\n Total {} samples will be used for the pipeline.".format(str(len(self.missing_sample)), str(len(self.final_sample_set))))

        self.dialog_noinput_close = True

    def evt_chk_single_partial_clicked(self):
        self.chk_unmatched_bool = False
        self.dialog_noinput_close = True
        self.unmatched_missing_msg_dialog.close()


    def generate_parameter(self):


        self.MetaPara_dict = {
            "M_Single" : self.PB_SequencingType_chkbox_single.isChecked(), \
            "M_Paired" : self.PB_SequencingType_chkbox_paired.isChecked(), \
            "M_Mouse" : self.PB_SequenceOrigin_chkbox_Mouse.isChecked(), \
            "M_Human" : self.PB_SequenceOrigin_chkbox_Human.isChecked(), \
            "M_Illumina" : self.PB_SequencingPlatform_chkbox_illumina.isChecked(), \
            "M_Others" : self.PB_SequenceingPlatform_chkbox_others.isChecked(), \
            "M_Threads" : self.PB_threads_spb.value()
                              }

        self.TrimPara_dict = {
            "Trim_Threads" : self.trimmomatic.PB_trimmomatic_thread_spb.value(),\
            "Trim_Phred" : self.trimmomatic.PB_trimmomatic_phred_cmb.currentText(), \
            "Trim_Summary" : self.trimmomatic.PB_trimmomatic_summary_chk.isChecked(), \
            "Trim_Leading" : self.trimmomatic.PB_trimmomatic_leading_ldt.text(), \
            "Trim_Trailing" : self.trimmomatic.PB_trimmomatic_traling_ldt.text(), \
            "Trim_Minlen": self.trimmomatic.PB_trimmomatic_minlen_ldt.text(), \
            "Trim_Sliding": self.trimmomatic.PB_trimmomatic_slidingwindow_ldt.text(),\
        }

        self.BowPara_dict = {
            "Bow_Threads" : self.bowtie2.PB_bowtie2_thread_spb.value(), \
            "Bow_Phred" : self.bowtie2.PB_bowtie2_phred_cmb.currentText(), \
            "Bow_Sensi" : self.bowtie2.PB_bowtie2_sensitive_cbb.currentText(), \
            "Bow_ROSAM" : self.bowtie2.PB_bowtie2_reordersam_chk.isChecked(), \
            "Bow_Exclusion" : self.bowtie2.PB_bowtie2_exclusion_cbb.value()

        }

        self.KraPara_dict = {
            "Kra_Threads" : self.kraken2.PB_kraken2_thread_spb.value(), \
            "Kra_Uncla" : self.kraken2.PB_kraken2_unclass_chk.isChecked(), \
            "Kra_Cla" : self.kraken2.PB_kraken2_class_chk.isChecked(), \
            "Kra_Confi" : self.kraken2.PB_kraken2_confidence_dblspb.value()
        }

        self.DiaPara_dict = {
            "Dia_Threads" : self.diamond.PB_diamond_threads_spb.value(), \
            "Dia_Sensi" : self.diamond.PB_diamond2_sensitivity_cbb.currentText(), \
            "Dia_MinId" : self.diamond.PB_diamond2_minidentity_spb.value(), \
            "Dia_QCover" : self.diamond.PB_diamond2_querycover_Spb.value(), \
            "Dia_Eval" : self.diamond.PB_diamond2_eval_ldt.text(), \
            "Dia_Verbose" : self.diamond.PB_diamond2_verbose_chk.isChecked(), \
            "Dia_Aligned" : self.diamond.PB_diamond2_aligned_chk.isChecked(), \
            "Dia_Unaligned" : self.diamond.PB_diamond2_unaligned_chk.isChecked(), \
            "Dia_MemControl" : self.diamond.PB_diamond2_memory_control_chk.isChecked()
        }

        self.AlpPara_dict = {
            "Ala_OOtus" : self.alpha.PB_alpha_ootus_chk.isChecked(), \
            "Ala_Shnn" : self.alpha.PB_alpha_shannon_chk.isChecked(), \
            "Ala_Simp" : self.alpha.PB_alpha_simpson_chk.isChecked(), \
            "Ala_Input" : self.alpha.Input_source_cbb.currentText()
        }

        self.BetaPara_dict = {
            "Beta_BC" : self.beta.PB_beta_braycurtis_chk.isChecked(), \
            "Beta_ACH" : self.beta.PB_beta_aitchison_chk.isChecked(), \
            "Beta_WUF" : self.beta.PB_beta_uwunifrac_chk.isChecked(), \
            "Beta_UWUF" : self.beta.PB_beta_uwunifrac_chk.isChecked(), \
            "Beta_Input" : self.beta.Input_source_cbb.currentText()
        }

        self.MWUTPara_dict = {
            "MWUT_ZP" : self.mwut.PB_MWU_zero_cbb.currentText(), \
            "MWUT_pval" : self.mwut.MWU_alpha.value(), \
            "MWUT_LFC" : self.mwut.MWU_LFC.value(), \
            "MWUT_FDR" : self.mwut.MWU_FDR.value(), \
            "MWUT_LFCFDR" : self.mwut.MWU_LFC_FDR.value(), \
            "MWUT_Input" : self.mwut.Input_source_cbb.currentText()
        }

        self.LefPara_dict ={
            "Lef_KW" : self.lefse.PB_lefse_kwalpha_dblspb.value(), \
            "Lef_PWC" : self.lefse.PB_lefse_pwilcoxon_dblsbp.value(), \
            "Lef_LDA" : self.lefse.PB_lefse_ldascore_spb.value(), \
            "Lef_Multi" : self.lefse.PB_lefse_multiclass.currentText(), \
            "Lef_Input" : self.lefse.Input_source_cbb.currentText()
        }

        self.ACBPara_dict = {
            "ACB_Pval" : self.ancombc.ANCOMBC_aval_dblspb.value(), \
            "ACB_FDR" : self.ancombc.ANCOMBC_padj_cbb.currentText(), \
            "ACB_ZC" : self.ancombc.ANCOMBC_zerocut_dblspb.value(), \
            "ACB_LibCut" : self.ancombc.ANCOMBC_librarycut_ldt.text(), \
            "ACB_StrZero" : self.ancombc.ANCOMBC_sturczero_chk.isChecked(), \
            "ACB_GLBTest" : self.ancombc.ANCOMBC_globaltest_chk.isChecked(), \
            "ACB_MEM" : self.ancombc.ANCOMBC_maxemiter_ldt.text(), \
            "ACB_Input" : self.ancombc.Input_source_cbb.currentText()
        }

        self.SBDPara_dict = {
            "SBD_DiffP" : self.songbird.doubleSpinBox.value(), \
            "SBD_LRate" : self.songbird.doubleSpinBox_2.value(), \
            "SBD_Epoch" : self.songbird.lineEdit_3.text(), \
            "SBD_Batch" : self.songbird.lineEdit.text(), \
            "SBD_GrdClip" : self.songbird.lineEdit_2.text(), \
            "SBD_ChkPoint" : self.songbird.lineEdit_4.text(), \
            "SBD_Verbose" : self.songbird.checkBox.isChecked(), \
            "SBD_Input" : self.songbird.Input_source_cbb.currentText()
        }

        self.RFPara_dict = {
            "RF_Est" : self.randomforest.RF_Estimators_.value(), \
            "RF_MDepth" : self.randomforest.RF_maxDepth_spb.value(), \
            "RF_MaxLeaf" : self.randomforest.RF_max_leaf_nodes_spb.value(), \
            "RF_MinSLeaf" : self.randomforest.RF_Min_Samples_Leaf_dblspb.value(), \
            "RF_MaxFture" : self.randomforest.RF_Max_Features_ldt.text(), \
            "RF_BStrap" : self.randomforest.RF_Bootstrap_chk.isChecked(), \
            "RF_RState" : self.randomforest.RF_RandomState_spb.value(), \
            "RF_Input" : self.randomforest.Input_source_cbb.currentText()
        }

        self.TableCol_dict = {
            "SampleTitle" : self.PB_metapara_sampletitle_cbb.currentText(), \
            "Class1" : self.PB_metapara_class1_cbb.currentText(), \
            "SClass1" : self.PB_metapara_sclass1_cbb.currentText(), \
            "MetaTablePath" : self.MetaTablePath
        }

        self.Project_dict = {
            "SampleDir" : self.PB_sampleDirectory, \
            "SampleTitles" : [self.PB_SampleDirectory_list.item(i).text() for i in range(self.PB_SampleDirectory_list.count())],\
            "SampleIdx1" : self.sample_title_idx1, \
            "SampleIdx2" : self.sample_title_idx2, \
            "HuMMUSDir" : os.path.abspath(os.path.dirname(__file__)), \
            "ProjectDir" : self.ProjectDir, \
            "ProjectTitle" : self.ProjectTitle, \
            "PipelineFlow" : [self.PB_pipeline_flow_list.item(row).text() for row in range(self.PB_pipeline_flow_list.count())],\
            "PipelineTitle" : self.PipeLineTitle, \
            "AvailableMemory" : psutil.virtual_memory()[1]*1e-9
        }

        self.paradict_idx = {
            "MetaParamter": self.MetaPara_dict, \
            "TableParameter" : self.TableCol_dict, \
            "Project_dict" : self.Project_dict, \
            "Trimmomatic": self.TrimPara_dict, \
            "Bowtie2": self.BowPara_dict, \
            "Kraken2": self.KraPara_dict, \
            "Diamond": self.DiaPara_dict, \
            "Alpha": self.AlpPara_dict, \
            "Beta": self.BetaPara_dict, \
            "Mann-Whitney U Test": self.MWUTPara_dict, \
            "LEfSe": self.LefPara_dict, \
            "ANCOMBC": self.ACBPara_dict, \
            "SongBird": self.SBDPara_dict, \
            "Random Forest" : self.RFPara_dict, \
            }
        for k in self.paradict_idx.keys():
            print(self.paradict_idx[k])

    def Update_QueueStack(self, MainProcessList, SubProcessDict):
        self.MainJobs.clear()
        self.SubJobs.clear()
        self.MainProcessLogDock.clear()
        self.MainStatusLog.clear()
        self.SubProcessLogDock.clear()
        self.MainStatusLog.clear()
        for mainitm in MainProcessList:
            job = "{} (waiting)".format(mainitm)
            self.MainJobs.addItem(job)
        for key in SubProcessDict.keys():
            for val in SubProcessDict[key]:
                job = "{} (waiting)".format(val)
                self.SubJobs.addItem(job)


    def RunPipelinewithArguments(self):
        MainProcessList, SubProcessDict = self.Reorganize_MainSubProcess()
        self.Update_QueueStack(MainProcessList, SubProcessDict)
        self.MainWorker = MainProcess(self.MetaPara_dict, self.Project_dict, self.TableCol_dict, self.paradict_idx, MainProcessList, SubProcessDict)
        self.MainThread = QThread(self)
        self.MainWorker.moveToThread(self.MainThread)
        self.MainWorker.stderrMain.connect(self.evt_MainProcess_stderr)
        self.MainWorker.stdoutMain.connect(self.evt_MainProcess_stdout)
        self.MainWorker.statusMain.connect(self.evt_MainProcess_status)
        self.MainWorker.subProcess.connect(self.evt_Execute_SubProcess)
        self.MainWorker.mpstatus.connect(self.evt_MainProcess_control)
        self.MainWorker.prgbaseval.connect(self.evt_MainProgressBar)
        self.MainWorker.bowtieStd.connect(self.evt_MainProcess_bowtie_std)
        self.MainThread.started.connect(self.MainWorker.run)
        self.MainThread.start()

    def evt_Execute_SubProcess(self, list):
        SubProcessArgumentList = list
        if self.ProcessStatusControl[1] == "Not Running":
            self.SubWorker1 = SubProcess1(SubProcessArgumentList)
            self.SubThread1 = QThread(self)
            print(self.SubThread1.currentThreadId())
            self.SubWorker1.moveToThread(self.SubThread1)
            self.SubWorker1.stderrSub.connect(self.evt_SubProcess_stderr)
            self.SubWorker1.stdoutSub.connect(self.evt_SubProcess_stdout)
            self.SubWorker1.statusSub.connect(self.evt_SubProcess1_status)
            self.SubWorker1.sp1status.connect(self.evt_SubProcess1_control)
            self.SubThread1.started.connect(self.SubWorker1.run)
            self.SubThread1.start()



        elif self.ProcessStatusControl[2] == "Not Running":
            self.SubWorker2 = SubProcess2(SubProcessArgumentList)
            self.SubThread2 = QThread(self)
            self.SubWorker2.moveToThread(self.SubThread2)
            self.SubWorker2.stderrSub.connect(self.evt_SubProcess_stderr)
            self.SubWorker2.stdoutSub.connect(self.evt_SubProcess_stdout)
            self.SubWorker2.statusSub.connect(self.evt_SubProcess2_status)
            self.SubWorker2.sp2status.connect(self.evt_SubProcess2_control)
            self.SubThread2.started.connect(self.SubWorker2.run)
            self.SubThread2.start()



        elif self.ProcessStatusControl[3] == "Not Running":
            self.SubWorker3 = SubProcess3(SubProcessArgumentList)
            self.SubThread3 = QThread(self)
            self.SubWorker3.moveToThread(self.SubThread3)
            self.SubWorker3.stderrSub.connect(self.evt_SubProcess_stderr)
            self.SubWorker3.stdoutSub.connect(self.evt_SubProcess_stdout)
            self.SubWorker3.statusSub.connect(self.evt_SubProcess3_status)
            self.SubWorker3.sp3status.connect(self.evt_SubProcess3_control)
            self.SubThread3.started.connect(self.SubWorker3.run)
            self.SubThread3.start()


    def evt_MainProcess_control(self, str):
        self.ProcessStatusControl[0] = str
    def evt_SubProcess1_control(self, str):
        self.ProcessStatusControl[1] = str
    def evt_SubProcess2_control(self, str):
        self.ProcessStatusControl[2] = str
    def evt_SubProcess3_control(self, str):
        self.ProcessStatusControl[3] = str

    def evt_MainProcess_bowtie_std(self, std):
        str = std
        bowtiepath = "/".join([self.ProjectDir, self.ProjectTitle, "Preprocessing", "Bowtie2", self.PipeLineTitle])
        bowtielog = "/".join([bowtiepath, "Bowtie2_Log"])
        self.MainProcessLogDock.appendPlainText(std)
        print(bowtiepath)

        if os.path.isfile(bowtielog):
            with open(bowtielog, "a") as a:
                a.write("".join([str, "\n"]))
            a.close()
        else:
            with open(bowtielog, "w") as n:
                n.write("".join([str, "\n"]))
            n.close()

    def evt_MainProgressBar(self, val):
        self.MainPrgBar.setValue(val)

    def evt_MainProcess_stderr(self, stderr):
        self.MainProcessLogDock.appendPlainText(stderr)
    def evt_MainProcess_stdout(self, stdout):
        self.MainProcessLogDock.appendPlainText(stdout)

    def evt_MainProcess_status(self, list):
        indicator = list[0]

        if indicator == "start":
            status = list[1]
            jobnum = list[2]
            self.MainStatusLog.appendPlainText("# {} stats to run.".format(status))
            self.MainJobs.item(jobnum).setText("{} (running)".format(status))
        elif indicator == "finished":
            status = list[1]
            jobnum = list[2]
            self.MainStatusLog.appendPlainText("# {} complete.".format(status))
            self.MainStatusBar.setText("# {} complete.".format(status))
            self.MainJobs.item(jobnum).setText("{} (complete)".format(status))

        elif indicator == "Allfinished":
            self.MainStatusLog.appendPlainText("# All MainProcess Job Complete!")
            self.MainStatusBar.setText("# All MainProcess Job Complete!")
            if "Running" not in self.ProcessStatusControl:
                self.MainPrgBar.setValue(100)
                self.PB_Proceed_btn.setText("Proceed")

        elif indicator == "sample":
            status = list[1]
            self.MainStatusLog.appendPlainText("{} is in process".format(status))
        elif indicator == "ProgressLog":
            module = list[1]
            sample = list[2]
            self.MainStatusBar.setText("# {} is running on {}".format(module, sample))

        ##########################Someday clean#########################3
    def evt_SubProcess_stderr(self, stderr):
        self.SubProcessLogDock.appendPlainText(stderr)
    def evt_SubProcess_stdout(self, stdout):
        self.SubProcessLogDock.appendPlainText(stdout)

    def evt_SubProcess1_status(self, list):
        indicator = list[0]
        if indicator == "start":
            status = list[1]
            self.SubStatusLog.appendPlainText("# {} stats to run.".format(status))
            self.SubStatusBar.setText("# {} stats to run.".format(status))
            self.SubJobs.findItems(status, Qt.MatchFlag.MatchContains)[0].setText("{} (running)".format(status))

        elif indicator == "finished":
            if list[1] != None:
                status = list[1]
                self.SubStatusLog.appendPlainText("# {} complete.".format(status))
                self.SubStatusBar.setText("# {} complete.".format(status))
                self.SubJobs.findItems(status, Qt.MatchFlag.MatchContains)[0].setText("{} (complete)".format(status))
            else:
                if "Running" not in self.ProcessStatusControl[1:]:
                    self.SubStatusLog.appendPlainText("# All SubProcess Job Complete!")
                    self.SubStatusBar.setText("# All SubProcess Job Complete!")
                if "Running" not in self.ProcessStatusControl:
                    self.MainPrgBar.setValue(100)
                    self.PB_Proceed_btn.setText("Proceed")


        elif indicator == "ProgressLog":
            module = list[1]
            self.SubStatusBar.setText("# {} is running".format(module))

    def evt_SubProcess2_status(self, list):
        indicator = list[0]
        if indicator == "start":
            status = list[1]
            self.SubStatusLog.appendPlainText("# {} stats to run.".format(status))
            self.SubStatusBar.setText("# {} stats to run.".format(status))
            self.SubJobs.findItems(status, Qt.MatchFlag.MatchContains)[0].setText("{} (running)".format(status))

        elif indicator == "finished":
            if list[1] != None:
                status = list[1]
                self.SubStatusLog.appendPlainText("# {} complete.".format(status))
                self.SubJobs.findItems(status, Qt.MatchFlag.MatchContains)[0].setText("{} (complete)".format(status))
            else:
                if "Running" not in self.ProcessStatusControl[1:]:
                    self.SubStatusLog.appendPlainText("# All SubProcess Job Complete!")
                    self.SubStatusBar.setText("# All SubProcess Job Complete!")
                if "Running" not in self.ProcessStatusControl:
                    self.MainPrgBar.setValue(100)
                    self.PB_Proceed_btn.setText("Proceed")

        elif indicator == "ProgressLog":
            module = list[1]
            self.SubStatusBar.setText("# {} is running".format(module))

    def evt_SubProcess3_status(self, list):
        indicator = list[0]
        if indicator == "start":
            status = list[1]
            self.SubStatusLog.appendPlainText("# {} stats to run.".format(status))
            self.SubStatusBar.setText("# {} stats to run.".format(status))
            self.SubJobs.findItems(status, Qt.MatchFlag.MatchContains)[0].setText("{} (running)".format(status))

        elif indicator == "finished":
            if list[1] != None:
                status = list[1]
                self.SubStatusLog.appendPlainText("# {} complete.".format(status))
                self.SubJobs.findItems(status, Qt.MatchFlag.MatchContains)[0].setText("{} (complete)".format(status))
            else:
                if "Running" not in self.ProcessStatusControl[1:]:
                    self.SubStatusLog.appendPlainText("# All SubProcess Job Complete!")
                    self.SubStatusBar.setText("# All SubProcess Job Complete!")
                if "Running" not in self.ProcessStatusControl:
                    self.MainPrgBar.setValue(100)
                    self.PB_Proceed_btn.setText("Proceed")

        elif indicator == "ProgressLog":
            module = list[1]
            self.SubStatusBar.setText("# {} is running".format(module))


    def Reorganize_MainSubProcess(self):
        pipeline_list = self.Project_dict["PipelineFlow"]

        analysis_list = []
        for module in pipeline_list:
            if module in ["Alpha", "Beta", "Mann-Whitney U Test", "LEfSe", "ANCOMBC", "SongBird"]:
                analysis_list.append(module)
        MainProcessList = []
        SubProcessdict = {}
        for module in pipeline_list:
            if module == "Trimmomatic":
                MainProcessList.append("Trimmomatic")
                SubProcessdict[module] = ["Trimmomatic Summary"]
            if module == "Bowtie2":
                MainProcessList.append("Bowtie2")
                SubProcessdict[module] = ["Bowtie2 Summary"]
            if module == "Kraken2":
                MainProcessList.append("Kraken2")
                Kraken2Sub = []
                for submodule in analysis_list:
                    Kraken2Sub.append("_".join(["Taxonomic", submodule]))
                Kraken2Sub = ["Kraken2 Taxonomic Table"] + Kraken2Sub
                SubProcessdict[module] = Kraken2Sub
            if module == "Diamond":
                MainProcessList.append("Diamond")
                Diamond2Sub = []
                for submodule in analysis_list:
                    Diamond2Sub.append("_".join(["Gene family", submodule]))
                    Diamond2Sub.append("_".join(["Pathway", submodule]))
                Diamond2Sub = ["Diamond Genefamily Table", "Diamond Pathway Table"] + Diamond2Sub
                SubProcessdict[module] = Diamond2Sub
            if module == "Random Forest":
                MainProcessList.append("Random Forest")
                SubProcessdict[module] = ["Random Forest Sub"]

        return MainProcessList, SubProcessdict


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        label = QLabela
        self.setCentralWidget(label)
        file = open("HuMMUS_logo.gif", "rb")
        ba = file.read()
        self.buffer = QBuffer()
        self.buffer.setData(ba)
        movie = QMovie(self.buffer, QByteArray())
        label.setMovie(movie)
        label.setMargin(20)
        movie.start()

class NewSubWindow_with_QWB(QMdiSubWindow):
    def __init__(self, url = None):
        super().__init__()
        self.web = QWebEngineView()
        self.url = url
        self.web.load(QUrl.fromLocalFile(url))
        self.web.page().profile().downloadRequested.connect(self.on_downloadRequested)
        self.web.setAcceptDrops(True)
        self.setWidget(self.web)
        self.setWindowTitle(url.split("/")[-1])
        self.adjustSize()

    def on_downloadRequested(self, download):
        path, _ = QFileDialog.getSaveFileName(self, "Save File", "Png  (*.png)")
        if path:
            download.setDownloadDirectory(str(path.rsplit("/", 1)[0]))
            download.setDownloadFileName(str(path.rsplit("/", 1)[1])+".png")
            download.accept()

    def return_web(self):
        return self


class WorkerThread(QThread):
    update_cpu = pyqtSignal(float)
    update_ram = pyqtSignal(float)
    def run(self):
        while True:
            cpu_usage = psutil.cpu_percent(interval = 1)
            memory_info = psutil.virtual_memory()
            memory_usage = memory_info[2]
            self.update_cpu.emit(cpu_usage)
            self.update_ram.emit(memory_usage)

class MainProcess(QObject):
    stderrMain = pyqtSignal(str)
    stdoutMain = pyqtSignal(str)
    statusMain = pyqtSignal(list)
    subProcess = pyqtSignal(list)
    prgbaseval = pyqtSignal(float)
    mpstatus = pyqtSignal(str)
    bowtieStd = pyqtSignal(str)
    def __init__(self, metaparadict, projectdict, tablecoldict, paradictidx, mainprocesslist, subprocessdict):
        super().__init__()

        self.PreviousProcess = ""

        self.MainProcessList = mainprocesslist
        self.SubProcessDict = subprocessdict
        self.MetaPara_dict = metaparadict
        self.Project_dict = projectdict
        self.TableCol_dict = tablecoldict
        self.paradict_idx  = paradictidx
        self.numofsubjob = 0
        for key in self.SubProcessDict:
            self.numofsubjob += len(self.SubProcessDict[key])

        if self.MetaPara_dict["M_Paired"]:
            forward_list, reverse_list = self.Project_dict["SampleTitles"][::2], self.Project_dict["SampleTitles"][1::2]
            self.sample_list = [[forward, reverse] for forward, reverse in zip(forward_list, reverse_list)]
        else:
            self.sample_list = self.Project_dict["SampleTitles"]

        self.totalnumofjob = (len(self.MainProcessList)*len(self.sample_list)) + self.numofsubjob
        self.PrgBaseVal = 100/self.totalnumofjob
        self.CumPrgVal = 0
    def run(self):
        self.mpstatus.emit("Running")
        for jobnum, mainprocessjob in enumerate(self.MainProcessList):
            MainAgenerator = Arguments_generator.ArgumentGenerator(self.MetaPara_dict, self.TableCol_dict, self.Project_dict, self.paradict_idx, self.sample_list, mainprocessjob)
            self.MainProcessArgumentList = MainAgenerator.GenerateArguments()
            for num, argument in enumerate(self.MainProcessArgumentList):

                self.MainProcessor = QProcess()
                self.CurrentProcess = argument[1]
                self.SampleName = argument[2]
                if self.CurrentProcess == "Bowtie2":
                    self.MainProcessor.readyReadStandardError.connect(self.evt_MainProcess_bowtie_stderr)
                    self.MainProcessor.readyReadStandardOutput.connect(self.evt_MainProcess_bowtie_stdout)
                else:
                    self.MainProcessor.readyReadStandardError.connect(self.evt_MainProcess_stderr)
                    self.MainProcessor.readyReadStandardOutput.connect(self.evt_MainProcess_stdout)
                print(argument)
                self.MainProcessor.start("python3", argument)

                if self.PreviousProcess != self.CurrentProcess:
                    self.statusMain.emit(["start", self.CurrentProcess, jobnum])
                self.statusMain.emit(["sample", self.SampleName])
                self.statusMain.emit(["ProgressLog", self.CurrentProcess, self.SampleName])

                self.MainProcessor.waitForFinished(-1)
                self.CumPrgVal += self.PrgBaseVal
                self.prgbaseval.emit(self.CumPrgVal)

                if argument == self.MainProcessArgumentList[-1]:
                        self.statusMain.emit(["finished", self.CurrentProcess, jobnum])
                        print(self.SubProcessDict[self.CurrentProcess])
                        SubAgenerator = Arguments_generator.ArgumentGenerator(self.MetaPara_dict, self.TableCol_dict,
                                                                              self.Project_dict, self.paradict_idx,
                                                                              self.sample_list,
                                                                              self.SubProcessDict[self.CurrentProcess])
                        SubProcessArgumentList = SubAgenerator.GenerateArguments()
                        print(SubProcessArgumentList)
                        self.subProcess.emit(SubProcessArgumentList)

                elif argument != self.MainProcessArgumentList[-1]:
                    if self.CurrentProcess != self.MainProcessArgumentList[num + 1][1]:
                        self.statusMain.emit(["finished", self.CurrentProcess, jobnum])
                        SubAgenerator = Arguments_generator.ArgumentGenerator(self.MetaPara_dict, self.TableCol_dict,
                                                                              self.Project_dict, self.paradict_idx,
                                                                              self.sample_list,
                                                                              self.SubProcessDict[self.CurrentProcess])
                        SubProcessArgumentList = SubAgenerator.GenerateArguments()
                        print(SubProcessArgumentList)
                        self.subProcess.emit(SubProcessArgumentList)
                        self.PreviousProcess = self.CurrentProcess

                    elif self.CurrentProcess == self.MainProcessArgumentList[num + 1][1]:
                        self.PreviousProcess = self.CurrentProcess
        self.mpstatus.emit("Not Running")
        self.statusMain.emit(["Allfinished"])

    def evt_MainProcess_bowtie_stderr(self):
        data = self.MainProcessor.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.bowtieStd.emit(stderr)

    def evt_MainProcess_bowtie_stdout(self):
        data = self.MainProcessor.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.bowtieStd.emit(stdout)

    def evt_MainProcess_stderr(self):
        data = self.MainProcessor.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.stderrMain.emit(stderr)

    def evt_MainProcess_stdout(self):
        data = self.MainProcessor.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.stdoutMain.emit(stdout)

class SubProcess1(QObject):
    stderrSub = pyqtSignal(str)
    stdoutSub = pyqtSignal(str)
    statusSub = pyqtSignal(list)
    SubPrgBar = pyqtSignal(float)
    sp1status = pyqtSignal(str)
    def __init__(self, SubArgumentList):
        super().__init__()
        self.program = "python3"
        self.SubArgumentList = SubArgumentList

        self.PreviousProcess = ""

    def run(self):
        self.sp1status.emit("Running")
        for num, argument in enumerate(self.SubArgumentList):
            self.SubProcess = QProcess()
            self.CurrentProcess = argument[1]
            self.SubProcess.readyReadStandardError.connect(self.evt_SubProcess1_stderr)
            self.SubProcess.readyReadStandardOutput.connect(self.evt_SubProcess1_stdout)
            print(argument)
            self.SubProcess.start(self.program, argument)

            if self.PreviousProcess != self.CurrentProcess:
                self.statusSub.emit(["start", self.CurrentProcess])
            self.statusSub.emit(["ProgressLog", self.CurrentProcess])

            self.SubProcess.waitForFinished(-1)

            if argument == self.SubArgumentList[-1]:
                self.statusSub.emit(["finished", self.CurrentProcess])

            elif argument != self.SubArgumentList[-1]:
                if self.CurrentProcess != self.SubArgumentList[num + 1]:
                    self.statusSub.emit(["finished", self.CurrentProcess])
                    self.PreviousProcess = self.CurrentProcess
                elif self.CurrentProcess == self.SubArgumentList[num + 1]:
                    self.PreviousProcess = self.CurrentProcess
        self.sp1status.emit("Not Running")
        self.statusSub.emit(["finished", None])

    def evt_SubProcess1_stderr(self):
        data = self.SubProcess.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.stderrSub.emit(stderr)

    def evt_SubProcess1_stdout(self):
        data = self.SubProcess.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.stdoutSub.emit(stdout)

class SubProcess2(QObject):
    stderrSub = pyqtSignal(str)
    stdoutSub = pyqtSignal(str)
    statusSub = pyqtSignal(list)
    SubPrgBar = pyqtSignal(float)
    sp2status = pyqtSignal(str)

    def __init__(self, SubArgumentList):
        super().__init__()
        self.program = "python3"
        self.SubArgumentList = SubArgumentList

        self.PreviousProcess = ""

    def run(self):
        self.sp2status.emit("Running")
        for num, argument in enumerate(self.SubArgumentList):
            self.SubProcess = QProcess()
            self.CurrentProcess = argument[1]
            self.SubProcess.readyReadStandardError.connect(self.evt_SubProcess2_stderr)
            self.SubProcess.readyReadStandardOutput.connect(self.evt_SubProcess2_stdout)
            print(argument)
            self.SubProcess.start(self.program, argument)

            if self.PreviousProcess != self.CurrentProcess:
                self.statusSub.emit(["start", self.CurrentProcess])
            self.statusSub.emit(["ProgressLog", self.CurrentProcess])

            self.SubProcess.waitForFinished(-1)

            if argument == self.SubArgumentList[-1]:
                self.statusSub.emit(["finished", self.CurrentProcess])

            elif argument != self.SubArgumentList[-1]:
                if self.CurrentProcess != self.SubArgumentList[num + 1]:
                    self.statusSub.emit(["finished", self.CurrentProcess])

                    self.PreviousProcess = self.CurrentProcess

                elif self.CurrentProcess == self.SubArgumentList[num + 1]:
                    self.PreviousProcess = self.CurrentProcess
        self.sp2status.emit("Not Running")
        self.statusSub.emit(["finished", None])


    def evt_SubProcess2_stderr(self):
        data = self.SubProcess.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.stderrSub.emit(stderr)
    def evt_SubProcess2_stdout(self):
        data = self.SubProcess.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.stdoutSub.emit(stdout)

class SubProcess3(QObject):
    stderrSub = pyqtSignal(str)
    stdoutSub = pyqtSignal(str)
    statusSub = pyqtSignal(list)
    SubPrgBar = pyqtSignal(float)
    sp3status = pyqtSignal(str)
    def __init__(self, SubArgumentList):
        super().__init__()
        self.program = "python3"
        self.SubArgumentList = SubArgumentList
        self.PreviousProcess = ""

    def run(self):
        self.sp3status.emit("Running")
        for num, argument in enumerate(self.SubArgumentList):
            self.SubProcess = QProcess()
            self.CurrentProcess = argument[1]
            self.SubProcess.readyReadStandardError.connect(self.evt_SubProcess3_stderr)
            self.SubProcess.readyReadStandardOutput.connect(self.evt_SubProcess3_stdout)
            print(argument)
            self.SubProcess.start(self.program, argument)

            if self.PreviousProcess != self.CurrentProcess:
                self.statusSub.emit(["start", self.CurrentProcess])
            self.statusSub.emit(["ProgressLog", self.CurrentProcess])

            self.SubProcess.waitForFinished(-1)

            if argument == self.SubArgumentList[-1]:
                self.statusSub.emit(["finished", self.CurrentProcess])
            elif argument != self.SubArgumentList[-1]:
                if self.CurrentProcess != self.SubArgumentList[num + 1]:
                    self.statusSub.emit(["finished", self.CurrentProcess])

                    self.PreviousProcess = self.CurrentProcess

                elif self.CurrentProcess == self.SubArgumentList[num + 1]:
                    self.PreviousProcess = self.CurrentProcess

        self.sp3status.emit("Not Running")
        self.statusSub.emit(["finished", None])


    def evt_SubProcess3_stderr(self):
        data = self.SubProcess.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.stderrSub.emit(stderr)
    def evt_SubProcess3_stdout(self):
        data = self.SubProcess.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.stdoutSub.emit(stdout)


class tool_instance(QWidget):
    def __init__(self):
        super().__init__()
        self.trimmomatic = trimmomatic_options.Ui_trimmomatic()
        self.trimmomatic.setupUi(self)
        self.bowtie2 = bowtie_options.Ui_trimmomatic()
        self.bowtie2.setupUi(self)
        self.kraken2 = kraken_options.Ui_trimmomatic()
        self.kraken2.setupUi(self)
        self.diamond = diamond_options.Ui_trimmomatic()
        self.diamond.setupUi(self)
        self.alpha = alpha_options.Ui_trimmomatic()
        self.alpha.setupUi(self)
        self.beta = beta_options.Ui_trimmomatic()
        self.beta.setupUi(self)
        self.MWUT = mannwhitneyu_option.Ui_trimmomatic()
        self.MWUT.setupUi(self)
        self.lefse = lefse_option.Ui_trimmomatic()
        self.lefse.setupUi(self)
        self.ancombc = ancombc_option.Ui_trimmomatic()
        self.ancombc.setupUi(self)
        self.songbird = songbird_option.Ui_trimmomatic()
        self.songbird.setupUi(self)
        self.randomforest = randomforest_option.Ui_trimmomatic()
        self.randomforest.setupUi(self)

    def return_tools(self):
            return {
                "Trimmomatic": [self.trimmomatic, self.trimmomatic.trimmomatic_GBX], \
                "Bowtie2" : [self.bowtie2, self.bowtie2.verticalGroupBox_2], \
                "Kraken2" : [self.kraken2, self.kraken2.verticalGroupBox_2], \
                "Diamond" : [self.diamond, self.diamond.verticalGroupBox_2], \
                "Alpha" : [self.alpha, self.alpha.verticalGroupBox_2], \
                "Beta" : [self.beta, self.beta.verticalGroupBox_2], \
                "Mann-Whitney U Test" : [self.MWUT, self.MWUT.verticalGroupBox_2], \
                "LEfSe" : [self.lefse, self.lefse.verticalGroupBox_2], \
                "ANCOMBC" : [self.ancombc, self.ancombc.PB_ANCOMBC_option_GBX], \
                "SongBird" : [self.songbird, self.songbird.PB_SongBird_option_gbx], \
                "Random Forest" : [self.randomforest, self.randomforest.PB_RandomForset_gbx]
            }
class initiate_statusbar(QWidget):
    def __init__(self):
        super().__init__()
        self.StatusBar = progressbar.Ui_StatusBar()
        self.StatusBar.setupUi(self)
    def Get_widget(self):
        return self.StatusBar

class QProcessDistatched(QObject):
    def __init__(self, projectdir, projecttitle, programpath, theme):
        super().__init__()
        self.ProjectDir = projectdir
        self.ProjectTitle = projecttitle
        self.ProgramPath = programpath
        self.pythonpath = "/home/hjkim-g15-portable/HuMMUS_venv/bin/python3.9"
        self.theme = theme
        self.arguments = [self.ProgramPath, self.ProjectDir, self.ProjectTitle, self.theme]
    def run(self):
        self.Processor = QProcess()
        self.Processor.setProgram(self.pythonpath)
        self.Processor.setArguments(self.arguments)
        self.Processor.startDetached()

class initiate_widgets(QWidget):
    def __init__(self):
        super().__init__()
        self.rechk_metapara = recheck_matepara.Ui_Form()
        self.rechk_metapara.setupUi(self)

    def return_rechk_metapara(self):
        self.metapara_list = [self.rechk_metapara.PB_SequencingType_chkbox_single, \
                         self.rechk_metapara.PB_SequencingType_chkbox_paired, \
                         self.rechk_metapara.PB_SequenceOrigin_chkbox_Mouse, \
                         self.rechk_metapara.PB_SequenceOrigin_chkbox_Human, \
                         self.rechk_metapara.PB_SequencingPlatform_chkbox_illumina,\
                         self.rechk_metapara.PB_SequenceingPlatform_chkbox_others, \
                         self.rechk_metapara.PB_threads_spb, \
                         self.rechk_metapara.PB_MetaPara_gbx, self.rechk_metapara.PB_Proceed_btn]

        return self.metapara_list

if __name__ == "__main__":
    print(sys.argv)

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarktheme.load_stylesheet("dark"))
    #app.setStyle("WindowsVista")
    menuMain = MenuMain()
    menuMain.show()
    sys.exit(app.exec())



