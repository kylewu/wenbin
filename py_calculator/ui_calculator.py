# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created: Thu Jul 24 11:15:07 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CalDialog(object):
    def setupUi(self, CalDialog):
        CalDialog.setObjectName("CalDialog")
        CalDialog.setEnabled(True)
        CalDialog.resize(292,165)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        CalDialog.setWindowIcon(icon)
        self.verticalLayoutWidget = QtGui.QWidget(CalDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30,20,231,141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelInput = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelInput.setObjectName("labelInput")
        self.horizontalLayout.addWidget(self.labelInput)
        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.txtInput = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.txtInput.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtInput.sizePolicy().hasHeightForWidth())
        self.txtInput.setSizePolicy(sizePolicy)
        self.txtInput.setMinimumSize(QtCore.QSize(100,20))
        self.txtInput.setSizeIncrement(QtCore.QSize(10,10))
        self.txtInput.setBaseSize(QtCore.QSize(100,0))
        self.txtInput.setMaxLength(2)
        self.txtInput.setObjectName("txtInput")
        self.horizontalLayout.addWidget(self.txtInput)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelOutput = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelOutput.setObjectName("labelOutput")
        self.horizontalLayout_2.addWidget(self.labelOutput)
        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.txtOutput = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.txtOutput.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtOutput.sizePolicy().hasHeightForWidth())
        self.txtOutput.setSizePolicy(sizePolicy)
        self.txtOutput.setMinimumSize(QtCore.QSize(100,20))
        self.txtOutput.setObjectName("txtOutput")
        self.horizontalLayout_2.addWidget(self.txtOutput)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.btnExit = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnExit.setObjectName("btnExit")
        self.horizontalLayout_3.addWidget(self.btnExit)
        spacerItem3 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(CalDialog)
        QtCore.QObject.connect(self.btnExit,QtCore.SIGNAL("clicked()"),CalDialog.close)
        QtCore.QMetaObject.connectSlotsByName(CalDialog)

    def retranslateUi(self, CalDialog):
        CalDialog.setWindowTitle(QtGui.QApplication.translate("CalDialog", "IELTS Calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.labelInput.setText(QtGui.QApplication.translate("CalDialog", "         Score :", None, QtGui.QApplication.UnicodeUTF8))
        self.labelOutput.setText(QtGui.QApplication.translate("CalDialog", "Band Score :", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExit.setText(QtGui.QApplication.translate("CalDialog", "Exit", None, QtGui.QApplication.UnicodeUTF8))

