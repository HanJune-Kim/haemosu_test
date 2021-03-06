# Form implementation generated from reading ui file './HuMMUS_pyqt/pyqt_ui/HuMMUS_PB_Trimmomatic.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_trimmomatic(object):
    def setupUi(self, trimmomatic):
        trimmomatic.setObjectName("trimmomatic")
        trimmomatic.resize(227, 281)
        self.trimmomatic_GBX = QtWidgets.QGroupBox(trimmomatic)
        self.trimmomatic_GBX.setGeometry(QtCore.QRect(20, 10, 188, 271))
        self.trimmomatic_GBX.setObjectName("trimmomatic_GBX")
        self.trimmomatic_UM_layout = QtWidgets.QVBoxLayout(self.trimmomatic_GBX)
        self.trimmomatic_UM_layout.setObjectName("trimmomatic_UM_layout")
        self.bbbb_5 = QtWidgets.QLabel(self.trimmomatic_GBX)
        font = QtGui.QFont()
        font.setBold(True)
        self.bbbb_5.setFont(font)
        self.bbbb_5.setIndent(5)
        self.bbbb_5.setObjectName("bbbb_5")
        self.trimmomatic_UM_layout.addWidget(self.bbbb_5)
        self.aaa = QtWidgets.QHBoxLayout()
        self.aaa.setObjectName("aaa")
        self.aaaaa = QtWidgets.QLabel(self.trimmomatic_GBX)
        self.aaaaa.setIndent(5)
        self.aaaaa.setObjectName("aaaaa")
        self.aaa.addWidget(self.aaaaa)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.aaa.addItem(spacerItem)
        self.PB_trimmomatic_thread_spb = QtWidgets.QSpinBox(self.trimmomatic_GBX)
        self.PB_trimmomatic_thread_spb.setProperty("value", 4)
        self.PB_trimmomatic_thread_spb.setObjectName("PB_trimmomatic_thread_spb")
        self.aaa.addWidget(self.PB_trimmomatic_thread_spb)
        self.trimmomatic_UM_layout.addLayout(self.aaa)
        self.aaaaaa = QtWidgets.QHBoxLayout()
        self.aaaaaa.setObjectName("aaaaaa")
        self.bbb = QtWidgets.QLabel(self.trimmomatic_GBX)
        self.bbb.setIndent(5)
        self.bbb.setObjectName("bbb")
        self.aaaaaa.addWidget(self.bbb)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.aaaaaa.addItem(spacerItem1)
        self.PB_trimmomatic_phred_cmb = QtWidgets.QComboBox(self.trimmomatic_GBX)
        self.PB_trimmomatic_phred_cmb.setObjectName("PB_trimmomatic_phred_cmb")
        self.PB_trimmomatic_phred_cmb.addItem("")
        self.PB_trimmomatic_phred_cmb.addItem("")
        self.aaaaaa.addWidget(self.PB_trimmomatic_phred_cmb)
        self.trimmomatic_UM_layout.addLayout(self.aaaaaa)
        self.bbbbbb_3 = QtWidgets.QHBoxLayout()
        self.bbbbbb_3.setObjectName("bbbbbb_3")
        self.bbbbbb_5 = QtWidgets.QLabel(self.trimmomatic_GBX)
        self.bbbbbb_5.setIndent(5)
        self.bbbbbb_5.setObjectName("bbbbbb_5")
        self.bbbbbb_3.addWidget(self.bbbbbb_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.bbbbbb_3.addItem(spacerItem2)
        self.PB_trimmomatic_summary_chk = QtWidgets.QCheckBox(self.trimmomatic_GBX)
        self.PB_trimmomatic_summary_chk.setChecked(True)
        self.PB_trimmomatic_summary_chk.setObjectName("PB_trimmomatic_summary_chk")
        self.bbbbbb_3.addWidget(self.PB_trimmomatic_summary_chk)
        self.trimmomatic_UM_layout.addLayout(self.bbbbbb_3)
        self.bbbbbb_6 = QtWidgets.QHBoxLayout()
        self.bbbbbb_6.setObjectName("bbbbbb_6")
        self.bbbbbb_8 = QtWidgets.QLabel(self.trimmomatic_GBX)
        self.bbbbbb_8.setIndent(5)
        self.bbbbbb_8.setObjectName("bbbbbb_8")
        self.bbbbbb_6.addWidget(self.bbbbbb_8)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.bbbbbb_6.addItem(spacerItem3)
        self.PB_trimmomatic_leading_ldt = QtWidgets.QLineEdit(self.trimmomatic_GBX)
        self.PB_trimmomatic_leading_ldt.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PB_trimmomatic_leading_ldt.setObjectName("PB_trimmomatic_leading_ldt")
        self.bbbbbb_6.addWidget(self.PB_trimmomatic_leading_ldt)
        self.trimmomatic_UM_layout.addLayout(self.bbbbbb_6)
        self.bbbbbb_9 = QtWidgets.QHBoxLayout()
        self.bbbbbb_9.setObjectName("bbbbbb_9")
        self.bbbbbb_11 = QtWidgets.QLabel(self.trimmomatic_GBX)
        self.bbbbbb_11.setIndent(5)
        self.bbbbbb_11.setObjectName("bbbbbb_11")
        self.bbbbbb_9.addWidget(self.bbbbbb_11)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.bbbbbb_9.addItem(spacerItem4)
        self.PB_trimmomatic_traling_ldt = QtWidgets.QLineEdit(self.trimmomatic_GBX)
        self.PB_trimmomatic_traling_ldt.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PB_trimmomatic_traling_ldt.setObjectName("PB_trimmomatic_traling_ldt")
        self.bbbbbb_9.addWidget(self.PB_trimmomatic_traling_ldt)
        self.trimmomatic_UM_layout.addLayout(self.bbbbbb_9)
        self.bbbbbb_12 = QtWidgets.QHBoxLayout()
        self.bbbbbb_12.setObjectName("bbbbbb_12")
        self.bbbbbbbb = QtWidgets.QLabel(self.trimmomatic_GBX)
        self.bbbbbbbb.setIndent(5)
        self.bbbbbbbb.setObjectName("bbbbbbbb")
        self.bbbbbb_12.addWidget(self.bbbbbbbb)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.bbbbbb_12.addItem(spacerItem5)
        self.PB_trimmomatic_minlen_ldt = QtWidgets.QLineEdit(self.trimmomatic_GBX)
        self.PB_trimmomatic_minlen_ldt.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PB_trimmomatic_minlen_ldt.setDragEnabled(True)
        self.PB_trimmomatic_minlen_ldt.setObjectName("PB_trimmomatic_minlen_ldt")
        self.bbbbbb_12.addWidget(self.PB_trimmomatic_minlen_ldt)
        self.trimmomatic_UM_layout.addLayout(self.bbbbbb_12)
        self.bbbb_2 = QtWidgets.QHBoxLayout()
        self.bbbb_2.setObjectName("bbbb_2")
        self.bbbb_4 = QtWidgets.QLabel(self.trimmomatic_GBX)
        self.bbbb_4.setIndent(5)
        self.bbbb_4.setObjectName("bbbb_4")
        self.bbbb_2.addWidget(self.bbbb_4)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.bbbb_2.addItem(spacerItem6)
        self.PB_trimmomatic_slidingwindow_ldt = QtWidgets.QLineEdit(self.trimmomatic_GBX)
        self.PB_trimmomatic_slidingwindow_ldt.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PB_trimmomatic_slidingwindow_ldt.setObjectName("PB_trimmomatic_slidingwindow_ldt")
        self.bbbb_2.addWidget(self.PB_trimmomatic_slidingwindow_ldt)
        self.trimmomatic_UM_layout.addLayout(self.bbbb_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.trimmomatic_UM_layout.addItem(spacerItem7)

        self.retranslateUi(trimmomatic)
        QtCore.QMetaObject.connectSlotsByName(trimmomatic)

    def retranslateUi(self, trimmomatic):
        _translate = QtCore.QCoreApplication.translate
        trimmomatic.setWindowTitle(_translate("trimmomatic", "Form"))
        self.bbbb_5.setText(_translate("trimmomatic", "Trimmomatic"))
        self.aaaaa.setText(_translate("trimmomatic", "Threads"))
        self.bbb.setText(_translate("trimmomatic", "Phred Score"))
        self.PB_trimmomatic_phred_cmb.setItemText(0, _translate("trimmomatic", "Phred33"))
        self.PB_trimmomatic_phred_cmb.setItemText(1, _translate("trimmomatic", "Phred64"))
        self.bbbbbb_5.setText(_translate("trimmomatic", "Summary"))
        self.PB_trimmomatic_summary_chk.setText(_translate("trimmomatic", "Enable"))
        self.bbbbbb_8.setText(_translate("trimmomatic", "LEADING"))
        self.PB_trimmomatic_leading_ldt.setText(_translate("trimmomatic", "5"))
        self.bbbbbb_11.setText(_translate("trimmomatic", "TRAILING"))
        self.PB_trimmomatic_traling_ldt.setText(_translate("trimmomatic", "5"))
        self.bbbbbbbb.setText(_translate("trimmomatic", "MINLEN"))
        self.PB_trimmomatic_minlen_ldt.setText(_translate("trimmomatic", "36"))
        self.bbbb_4.setText(_translate("trimmomatic", "SLIDINGWINDOW"))
        self.PB_trimmomatic_slidingwindow_ldt.setText(_translate("trimmomatic", "4:15"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    trimmomatic = QtWidgets.QWidget()
    ui = Ui_trimmomatic()
    ui.setupUi(trimmomatic)
    trimmomatic.show()
    sys.exit(app.exec())
