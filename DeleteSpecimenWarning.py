# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeleteSpecimenWarning.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogDeleteSpecimen(object):
    def setupUi(self, DialogDeleteSpecimen):
        DialogDeleteSpecimen.setObjectName("DialogDeleteSpecimen")
        DialogDeleteSpecimen.resize(300, 120)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogDeleteSpecimen.sizePolicy().hasHeightForWidth())
        DialogDeleteSpecimen.setSizePolicy(sizePolicy)
        DialogDeleteSpecimen.setMinimumSize(QtCore.QSize(300, 120))
        DialogDeleteSpecimen.setMaximumSize(QtCore.QSize(300, 120))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(10)
        DialogDeleteSpecimen.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ImageIcons/Icons/Warning.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogDeleteSpecimen.setWindowIcon(icon)
        DialogDeleteSpecimen.setLayoutDirection(QtCore.Qt.RightToLeft)
        DialogDeleteSpecimen.setAutoFillBackground(False)
        DialogDeleteSpecimen.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.pushButtonYesDelete = QtWidgets.QPushButton(DialogDeleteSpecimen)
        self.pushButtonYesDelete.setGeometry(QtCore.QRect(65, 80, 50, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonYesDelete.sizePolicy().hasHeightForWidth())
        self.pushButtonYesDelete.setSizePolicy(sizePolicy)
        self.pushButtonYesDelete.setMinimumSize(QtCore.QSize(50, 25))
        self.pushButtonYesDelete.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonYesDelete.setFont(font)
        self.pushButtonYesDelete.setObjectName("pushButtonYesDelete")
        self.pushButtonCancelDelete = QtWidgets.QPushButton(DialogDeleteSpecimen)
        self.pushButtonCancelDelete.setGeometry(QtCore.QRect(135, 80, 100, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonCancelDelete.sizePolicy().hasHeightForWidth())
        self.pushButtonCancelDelete.setSizePolicy(sizePolicy)
        self.pushButtonCancelDelete.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButtonCancelDelete.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonCancelDelete.setFont(font)
        self.pushButtonCancelDelete.setObjectName("pushButtonCancelDelete")
        self.labelDeleteMessege = QtWidgets.QLabel(DialogDeleteSpecimen)
        self.labelDeleteMessege.setGeometry(QtCore.QRect(20, 10, 260, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDeleteMessege.sizePolicy().hasHeightForWidth())
        self.labelDeleteMessege.setSizePolicy(sizePolicy)
        self.labelDeleteMessege.setMinimumSize(QtCore.QSize(260, 60))
        self.labelDeleteMessege.setMaximumSize(QtCore.QSize(260, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDeleteMessege.setFont(font)
        self.labelDeleteMessege.setText("")
        self.labelDeleteMessege.setScaledContents(False)
        self.labelDeleteMessege.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDeleteMessege.setWordWrap(True)
        self.labelDeleteMessege.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.labelDeleteMessege.setObjectName("labelDeleteMessege")

        self.retranslateUi(DialogDeleteSpecimen)
        QtCore.QMetaObject.connectSlotsByName(DialogDeleteSpecimen)

    def retranslateUi(self, DialogDeleteSpecimen):
        _translate = QtCore.QCoreApplication.translate
        DialogDeleteSpecimen.setWindowTitle(_translate("DialogDeleteSpecimen", "هشدار"))
        self.pushButtonYesDelete.setText(_translate("DialogDeleteSpecimen", "بله"))
        self.pushButtonCancelDelete.setText(_translate("DialogDeleteSpecimen", "انصراف"))
import ImageIcons_rc
