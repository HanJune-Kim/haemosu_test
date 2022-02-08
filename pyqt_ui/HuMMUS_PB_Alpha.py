# Form implementation generated from reading ui file './HuMMUS_pyqt/pyqt_ui/HuMMUS_PB_Alpha.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_trimmomatic(object):
    def setupUi(self, trimmomatic):
        trimmomatic.setObjectName("trimmomatic")
        trimmomatic.resize(225, 164)
        self.verticalGroupBox_2 = QtWidgets.QGroupBox(trimmomatic)
        self.verticalGroupBox_2.setGeometry(QtCore.QRect(20, 10, 191, 141))
        self.verticalGroupBox_2.setObjectName("verticalGroupBox_2")
        self.trimmomatic_UM_layout = QtWidgets.QVBoxLayout(self.verticalGroupBox_2)
        self.trimmomatic_UM_layout.setObjectName("trimmomatic_UM_layout")
        self.label_8 = QtWidgets.QLabel(self.verticalGroupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setIndent(5)
        self.label_8.setObjectName("label_8")
        self.trimmomatic_UM_layout.addWidget(self.label_8)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_15 = QtWidgets.QLabel(self.verticalGroupBox_2)
        self.label_15.setIndent(5)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_16.addWidget(self.label_15)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem)
        self.PB_alpha_ootus_chk = QtWidgets.QCheckBox(self.verticalGroupBox_2)
        self.PB_alpha_ootus_chk.setText("")
        self.PB_alpha_ootus_chk.setChecked(True)
        self.PB_alpha_ootus_chk.setObjectName("PB_alpha_ootus_chk")
        self.horizontalLayout_16.addWidget(self.PB_alpha_ootus_chk)
        self.trimmomatic_UM_layout.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.verticalGroupBox_2)
        self.label_10.setIndent(5)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.PB_alpha_shannon_chk = QtWidgets.QCheckBox(self.verticalGroupBox_2)
        self.PB_alpha_shannon_chk.setText("")
        self.PB_alpha_shannon_chk.setChecked(True)
        self.PB_alpha_shannon_chk.setObjectName("PB_alpha_shannon_chk")
        self.horizontalLayout_9.addWidget(self.PB_alpha_shannon_chk)
        self.trimmomatic_UM_layout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.verticalGroupBox_2)
        self.label_9.setIndent(5)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.PB_alpha_simpson_chk = QtWidgets.QCheckBox(self.verticalGroupBox_2)
        self.PB_alpha_simpson_chk.setText("")
        self.PB_alpha_simpson_chk.setChecked(True)
        self.PB_alpha_simpson_chk.setObjectName("PB_alpha_simpson_chk")
        self.horizontalLayout_8.addWidget(self.PB_alpha_simpson_chk)
        self.trimmomatic_UM_layout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.verticalGroupBox_2)
        self.label_11.setIndent(5)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.Input_source_cbb = QtWidgets.QComboBox(self.verticalGroupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Input_source_cbb.sizePolicy().hasHeightForWidth())
        self.Input_source_cbb.setSizePolicy(sizePolicy)
        self.Input_source_cbb.setObjectName("Input_source_cbb")
        self.Input_source_cbb.addItem("")
        self.horizontalLayout_10.addWidget(self.Input_source_cbb)
        self.trimmomatic_UM_layout.addLayout(self.horizontalLayout_10)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.trimmomatic_UM_layout.addItem(spacerItem3)

        self.retranslateUi(trimmomatic)
        QtCore.QMetaObject.connectSlotsByName(trimmomatic)

    def retranslateUi(self, trimmomatic):
        _translate = QtCore.QCoreApplication.translate
        trimmomatic.setWindowTitle(_translate("trimmomatic", "Form"))
        self.label_8.setText(_translate("trimmomatic", "Alpha"))
        self.label_15.setText(_translate("trimmomatic", "Oberved OTUs"))
        self.label_10.setText(_translate("trimmomatic", "Shannon"))
        self.label_9.setText(_translate("trimmomatic", "Simpson"))
        self.label_11.setText(_translate("trimmomatic", "Input "))
        self.Input_source_cbb.setItemText(0, _translate("trimmomatic", "None"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    trimmomatic = QtWidgets.QWidget()
    ui = Ui_trimmomatic()
    ui.setupUi(trimmomatic)
    trimmomatic.show()
    sys.exit(app.exec())