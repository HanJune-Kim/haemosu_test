# Form implementation generated from reading ui file './HuMMUS_pyqt/pyqt_ui/HuMMUS_PB_Songbird.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_trimmomatic(object):
    def setupUi(self, trimmomatic):
        trimmomatic.setObjectName("trimmomatic")
        trimmomatic.resize(237, 285)
        self.PB_SongBird_option_gbx = QtWidgets.QGroupBox(trimmomatic)
        self.PB_SongBird_option_gbx.setGeometry(QtCore.QRect(20, 10, 201, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB_SongBird_option_gbx.sizePolicy().hasHeightForWidth())
        self.PB_SongBird_option_gbx.setSizePolicy(sizePolicy)
        self.PB_SongBird_option_gbx.setObjectName("PB_SongBird_option_gbx")
        self.trimmomatic_UM_layout = QtWidgets.QVBoxLayout(self.PB_SongBird_option_gbx)
        self.trimmomatic_UM_layout.setObjectName("trimmomatic_UM_layout")
        self.label_8 = QtWidgets.QLabel(self.PB_SongBird_option_gbx)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setIndent(5)
        self.label_8.setObjectName("label_8")
        self.trimmomatic_UM_layout.addWidget(self.label_8)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_18 = QtWidgets.QLabel(self.PB_SongBird_option_gbx)
        self.label_18.setIndent(5)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_19.addWidget(self.label_18)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.PB_SongBird_option_gbx)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setProperty("value", 1.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_19.addWidget(self.doubleSpinBox)
        self.trimmomatic_UM_layout.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_19 = QtWidgets.QLabel(self.PB_SongBird_option_gbx)
        self.label_19.setIndent(5)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_20.addWidget(self.label_19)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.PB_SongBird_option_gbx)
        self.doubleSpinBox_2.setDecimals(4)
        self.doubleSpinBox_2.setMaximum(1.0)
        self.doubleSpinBox_2.setSingleStep(0.001)
        self.doubleSpinBox_2.setProperty("value", 0.001)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.horizontalLayout_20.addWidget(self.doubleSpinBox_2)
        self.trimmomatic_UM_layout.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_16 = QtWidgets.QLabel(self.PB_SongBird_option_gbx)
        self.label_16.setIndent(5)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_17.addWidget(self.label_16)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.PB_SongBird_option_gbx)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_17.addWidget(self.lineEdit_3)
        self.trimmomatic_UM_layout.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_17 = QtWidgets.QLabel(self.PB_SongBird_option_gbx)
        self.label_17.setIndent(5)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_18.addWidget(self.label_17)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem3)
        self.lineEdit = QtWidgets.QLineEdit(self.PB_SongBird_option_gbx)
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_18.addWidget(self.lineEdit)
        self.trimmomatic_UM_layout.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_20 = QtWidgets.QLabel(self.PB_SongBird_option_gbx)
        self.label_20.setIndent(5)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_21.addWidget(self.label_20)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.PB_SongBird_option_gbx)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_21.addWidget(self.lineEdit_2)
        self.trimmomatic_UM_layout.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_22 = QtWidgets.QLabel(self.PB_SongBird_option_gbx)
        self.label_22.setIndent(5)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_23.addWidget(self.label_22)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.PB_SongBird_option_gbx)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_23.addWidget(self.lineEdit_4)
        self.trimmomatic_UM_layout.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_15 = QtWidgets.QLabel(self.PB_SongBird_option_gbx)
        self.label_15.setIndent(5)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_16.addWidget(self.label_15)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem6)
        self.checkBox = QtWidgets.QCheckBox(self.PB_SongBird_option_gbx)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_16.addWidget(self.checkBox)
        self.trimmomatic_UM_layout.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.PB_SongBird_option_gbx)
        self.label_11.setIndent(5)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.Input_source_cbb = QtWidgets.QComboBox(self.PB_SongBird_option_gbx)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Input_source_cbb.sizePolicy().hasHeightForWidth())
        self.Input_source_cbb.setSizePolicy(sizePolicy)
        self.Input_source_cbb.setObjectName("Input_source_cbb")
        self.Input_source_cbb.addItem("")
        self.horizontalLayout_10.addWidget(self.Input_source_cbb)
        self.trimmomatic_UM_layout.addLayout(self.horizontalLayout_10)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.trimmomatic_UM_layout.addItem(spacerItem7)

        self.retranslateUi(trimmomatic)
        QtCore.QMetaObject.connectSlotsByName(trimmomatic)

    def retranslateUi(self, trimmomatic):
        _translate = QtCore.QCoreApplication.translate
        trimmomatic.setWindowTitle(_translate("trimmomatic", "Form"))
        self.label_8.setText(_translate("trimmomatic", "SongBird"))
        self.label_18.setText(_translate("trimmomatic", "DIfferential priop"))
        self.label_19.setText(_translate("trimmomatic", "Learning rate"))
        self.label_16.setText(_translate("trimmomatic", "Epochs"))
        self.lineEdit_3.setText(_translate("trimmomatic", "1000"))
        self.label_17.setText(_translate("trimmomatic", "Batch size"))
        self.lineEdit.setText(_translate("trimmomatic", "5"))
        self.label_20.setText(_translate("trimmomatic", "Gradient clipping"))
        self.lineEdit_2.setText(_translate("trimmomatic", "10"))
        self.label_22.setText(_translate("trimmomatic", "Checkpoint interval"))
        self.lineEdit_4.setText(_translate("trimmomatic", "3600"))
        self.label_15.setText(_translate("trimmomatic", "Verbose"))
        self.checkBox.setText(_translate("trimmomatic", "Enable"))
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
