# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiscrcpy/ui/settings.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(441, 447)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 441, 408))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.b1c2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.b1c2.setObjectName("b1c2")
        self.gridLayout.addWidget(self.b1c2, 10, 4, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 11, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 11, 1, 1, 1)
        self.a1 = QtWidgets.QCheckBox(self.layoutWidget)
        self.a1.setObjectName("a1")
        self.gridLayout.addWidget(self.a1, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(25, 0))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 10, 3, 1, 1)
        self.a4 = QtWidgets.QCheckBox(self.layoutWidget)
        self.a4.setObjectName("a4")
        self.gridLayout.addWidget(self.a4, 4, 0, 1, 1)
        self.a6d1 = QtWidgets.QToolButton(self.layoutWidget)
        self.a6d1.setObjectName("a6d1")
        self.gridLayout.addWidget(self.a6d1, 6, 1, 1, 1)
        self.b2c1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.b2c1.setObjectName("b2c1")
        self.gridLayout.addWidget(self.b2c1, 11, 2, 1, 1)
        self.a3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.a3.setObjectName("a3")
        self.gridLayout.addWidget(self.a3, 3, 0, 1, 1)
        self.a8c1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.a8c1.setObjectName("a8c1")
        self.gridLayout.addWidget(self.a8c1, 7, 1, 1, 5)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setEnabled(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.a9 = QtWidgets.QCheckBox(self.layoutWidget)
        self.a9.setObjectName("a9")
        self.gridLayout.addWidget(self.a9, 8, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 10, 1, 1, 1)
        self.updatebutton = QtWidgets.QPushButton(self.layoutWidget)
        self.updatebutton.setObjectName("updatebutton")
        self.gridLayout.addWidget(self.updatebutton, 12, 2, 1, 4)
        self.a6 = QtWidgets.QCheckBox(self.layoutWidget)
        self.a6.setObjectName("a6")
        self.gridLayout.addWidget(self.a6, 6, 0, 1, 1)
        self.a5c1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.a5c1.setObjectName("a5c1")
        self.gridLayout.addWidget(self.a5c1, 5, 1, 1, 5)
        self.a8 = QtWidgets.QCheckBox(self.layoutWidget)
        self.a8.setObjectName("a8")
        self.gridLayout.addWidget(self.a8, 7, 0, 1, 1)
        self.b1c1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.b1c1.setObjectName("b1c1")
        self.gridLayout.addWidget(self.b1c1, 10, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setEnabled(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 3, 1, 1)
        self.b1 = QtWidgets.QCheckBox(self.layoutWidget)
        self.b1.setObjectName("b1")
        self.gridLayout.addWidget(self.b1, 10, 0, 1, 1)
        self.a2c1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.a2c1.setEnabled(False)
        self.a2c1.setObjectName("a2c1")
        self.gridLayout.addWidget(self.a2c1, 1, 2, 1, 1)
        self.b2c2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.b2c2.setObjectName("b2c2")
        self.gridLayout.addWidget(self.b2c2, 11, 4, 1, 2)
        self.b2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.b2.setObjectName("b2")
        self.gridLayout.addWidget(self.b2, 11, 0, 1, 1)
        self.a2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.a2.setEnabled(False)
        self.a2.setObjectName("a2")
        self.gridLayout.addWidget(self.a2, 1, 0, 1, 1)
        self.b0 = QtWidgets.QCheckBox(self.layoutWidget)
        self.b0.setObjectName("b0")
        self.gridLayout.addWidget(self.b0, 9, 0, 1, 1)
        self.b0c1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.b0c1.setObjectName("b0c1")
        self.gridLayout.addWidget(self.b0c1, 9, 1, 1, 5)
        self.a5 = QtWidgets.QCheckBox(self.layoutWidget)
        self.a5.setObjectName("a5")
        self.gridLayout.addWidget(self.a5, 5, 0, 1, 1)
        self.a6c1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.a6c1.setObjectName("a6c1")
        self.gridLayout.addWidget(self.a6c1, 6, 2, 1, 4)
        self.a2c2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.a2c2.setEnabled(False)
        self.a2c2.setObjectName("a2c2")
        self.gridLayout.addWidget(self.a2c2, 1, 4, 1, 2)
        self.a3e1 = QtWidgets.QSpinBox(self.layoutWidget)
        self.a3e1.setObjectName("a3e1")
        self.gridLayout.addWidget(self.a3e1, 3, 1, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Settings"))
        self.label_6.setText(_translate("MainWindow", "h"))
        self.label_5.setText(_translate("MainWindow", "w"))
        self.a1.setText(_translate("MainWindow", "Always on Top"))
        self.label_4.setText(_translate("MainWindow", "y"))
        self.a4.setText(_translate("MainWindow", "Prefer Text"))
        self.a6d1.setText(_translate("MainWindow", "..."))
        self.a3.setText(_translate("MainWindow", "Max Frame / second (FPS)"))
        self.label.setText(_translate("MainWindow", "x"))
        self.a9.setText(_translate("MainWindow", "Borderless Window"))
        self.label_3.setText(_translate("MainWindow", "x"))
        self.updatebutton.setText(_translate("MainWindow", "Update"))
        self.a6.setText(_translate("MainWindow", "Record File"))
        self.a8.setText(_translate("MainWindow", "Serial"))
        self.label_2.setText(_translate("MainWindow", "y"))
        self.b1.setText(_translate("MainWindow", "Window position"))
        self.b2.setText(_translate("MainWindow", "Window size"))
        self.a2.setText(_translate("MainWindow", "Crop Width"))
        self.b0.setText(_translate("MainWindow", "Window Title"))
        self.a5.setText(_translate("MainWindow", "Push Target"))
