# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeleteProjectWarning.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogDeleteProject(object):
    def setupUi(self, DialogDeleteProject):
        DialogDeleteProject.setObjectName("DialogDeleteProject")
        DialogDeleteProject.resize(300, 120)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogDeleteProject.sizePolicy().hasHeightForWidth())
        DialogDeleteProject.setSizePolicy(sizePolicy)
        DialogDeleteProject.setMinimumSize(QtCore.QSize(300, 120))
        DialogDeleteProject.setMaximumSize(QtCore.QSize(300, 120))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(10)
        DialogDeleteProject.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ImageIcons/Icons/Warning.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogDeleteProject.setWindowIcon(icon)
        DialogDeleteProject.setLayoutDirection(QtCore.Qt.RightToLeft)
        DialogDeleteProject.setAutoFillBackground(False)
        DialogDeleteProject.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.pushButtonYesDelete = QtWidgets.QPushButton(DialogDeleteProject)
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
        self.pushButtonCancelDelete = QtWidgets.QPushButton(DialogDeleteProject)
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
        self.labelDeleteMessege = QtWidgets.QLabel(DialogDeleteProject)
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

        self.retranslateUi(DialogDeleteProject)
        QtCore.QMetaObject.connectSlotsByName(DialogDeleteProject)

    def retranslateUi(self, DialogDeleteProject):
        _translate = QtCore.QCoreApplication.translate
        DialogDeleteProject.setWindowTitle(_translate("DialogDeleteProject", "هشدار"))
        self.pushButtonYesDelete.setText(_translate("DialogDeleteProject", "بله"))
        self.pushButtonCancelDelete.setText(_translate("DialogDeleteProject", "انصراف"))
import ImageIcons_rc
