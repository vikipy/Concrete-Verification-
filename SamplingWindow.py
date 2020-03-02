# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SamplingWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogSamplingWindow(object):
    def setupUi(self, DialogSamplingWindow):
        DialogSamplingWindow.setObjectName("DialogSamplingWindow")
        DialogSamplingWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogSamplingWindow.resize(600, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogSamplingWindow.sizePolicy().hasHeightForWidth())
        DialogSamplingWindow.setSizePolicy(sizePolicy)
        DialogSamplingWindow.setMinimumSize(QtCore.QSize(600, 400))
        DialogSamplingWindow.setMaximumSize(QtCore.QSize(600, 400))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(11)
        DialogSamplingWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ImageIcons/Icons/Sampling.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogSamplingWindow.setWindowIcon(icon)
        DialogSamplingWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        DialogSamplingWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        DialogSamplingWindow.setModal(True)
        self.pushButtonAddSampling = QtWidgets.QPushButton(DialogSamplingWindow)
        self.pushButtonAddSampling.setGeometry(QtCore.QRect(560, 75, 32, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAddSampling.sizePolicy().hasHeightForWidth())
        self.pushButtonAddSampling.setSizePolicy(sizePolicy)
        self.pushButtonAddSampling.setMinimumSize(QtCore.QSize(32, 32))
        self.pushButtonAddSampling.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButtonAddSampling.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ImageIcons/Icons/AddRowIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAddSampling.setIcon(icon1)
        self.pushButtonAddSampling.setIconSize(QtCore.QSize(28, 28))
        self.pushButtonAddSampling.setFlat(True)
        self.pushButtonAddSampling.setObjectName("pushButtonAddSampling")
        self.pushButtonDelSampling = QtWidgets.QPushButton(DialogSamplingWindow)
        self.pushButtonDelSampling.setEnabled(False)
        self.pushButtonDelSampling.setGeometry(QtCore.QRect(525, 75, 32, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDelSampling.sizePolicy().hasHeightForWidth())
        self.pushButtonDelSampling.setSizePolicy(sizePolicy)
        self.pushButtonDelSampling.setMinimumSize(QtCore.QSize(32, 32))
        self.pushButtonDelSampling.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButtonDelSampling.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ImageIcons/Icons/DeleteRow.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDelSampling.setIcon(icon2)
        self.pushButtonDelSampling.setIconSize(QtCore.QSize(28, 28))
        self.pushButtonDelSampling.setFlat(True)
        self.pushButtonDelSampling.setObjectName("pushButtonDelSampling")
        self.pushButtonEditSampling = QtWidgets.QPushButton(DialogSamplingWindow)
        self.pushButtonEditSampling.setEnabled(False)
        self.pushButtonEditSampling.setGeometry(QtCore.QRect(490, 75, 32, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonEditSampling.sizePolicy().hasHeightForWidth())
        self.pushButtonEditSampling.setSizePolicy(sizePolicy)
        self.pushButtonEditSampling.setMinimumSize(QtCore.QSize(32, 32))
        self.pushButtonEditSampling.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButtonEditSampling.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ImageIcons/Icons/EditRowIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonEditSampling.setIcon(icon3)
        self.pushButtonEditSampling.setIconSize(QtCore.QSize(28, 28))
        self.pushButtonEditSampling.setFlat(True)
        self.pushButtonEditSampling.setObjectName("pushButtonEditSampling")
        self.line = QtWidgets.QFrame(DialogSamplingWindow)
        self.line.setGeometry(QtCore.QRect(0, 68, 600, 10))
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label02 = QtWidgets.QLabel(DialogSamplingWindow)
        self.label02.setGeometry(QtCore.QRect(530, 40, 60, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label02.sizePolicy().hasHeightForWidth())
        self.label02.setSizePolicy(sizePolicy)
        self.label02.setMinimumSize(QtCore.QSize(60, 25))
        self.label02.setMaximumSize(QtCore.QSize(60, 25))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(8)
        self.label02.setFont(font)
        self.label02.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label02.setObjectName("label02")
        self.labelContractNumber = QtWidgets.QLabel(DialogSamplingWindow)
        self.labelContractNumber.setEnabled(True)
        self.labelContractNumber.setGeometry(QtCore.QRect(450, 40, 80, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelContractNumber.sizePolicy().hasHeightForWidth())
        self.labelContractNumber.setSizePolicy(sizePolicy)
        self.labelContractNumber.setMinimumSize(QtCore.QSize(80, 25))
        self.labelContractNumber.setMaximumSize(QtCore.QSize(60, 25))
        self.labelContractNumber.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.labelContractNumber.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelContractNumber.setText("")
        self.labelContractNumber.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelContractNumber.setObjectName("labelContractNumber")
        self.label03 = QtWidgets.QLabel(DialogSamplingWindow)
        self.label03.setGeometry(QtCore.QRect(375, 10, 60, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label03.sizePolicy().hasHeightForWidth())
        self.label03.setSizePolicy(sizePolicy)
        self.label03.setMinimumSize(QtCore.QSize(60, 25))
        self.label03.setMaximumSize(QtCore.QSize(60, 25))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label03.setFont(font)
        self.label03.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label03.setObjectName("label03")
        self.labelProjectName = QtWidgets.QLabel(DialogSamplingWindow)
        self.labelProjectName.setEnabled(True)
        self.labelProjectName.setGeometry(QtCore.QRect(225, 10, 150, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelProjectName.sizePolicy().hasHeightForWidth())
        self.labelProjectName.setSizePolicy(sizePolicy)
        self.labelProjectName.setMinimumSize(QtCore.QSize(150, 25))
        self.labelProjectName.setMaximumSize(QtCore.QSize(150, 20))
        self.labelProjectName.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.labelProjectName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelProjectName.setText("")
        self.labelProjectName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelProjectName.setObjectName("labelProjectName")
        self.label04 = QtWidgets.QLabel(DialogSamplingWindow)
        self.label04.setGeometry(QtCore.QRect(375, 40, 60, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label04.sizePolicy().hasHeightForWidth())
        self.label04.setSizePolicy(sizePolicy)
        self.label04.setMinimumSize(QtCore.QSize(60, 25))
        self.label04.setMaximumSize(QtCore.QSize(60, 25))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(10)
        self.label04.setFont(font)
        self.label04.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label04.setObjectName("label04")
        self.labelClient = QtWidgets.QLabel(DialogSamplingWindow)
        self.labelClient.setEnabled(True)
        self.labelClient.setGeometry(QtCore.QRect(225, 40, 150, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelClient.sizePolicy().hasHeightForWidth())
        self.labelClient.setSizePolicy(sizePolicy)
        self.labelClient.setMinimumSize(QtCore.QSize(150, 25))
        self.labelClient.setMaximumSize(QtCore.QSize(150, 25))
        self.labelClient.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.labelClient.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelClient.setText("")
        self.labelClient.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelClient.setObjectName("labelClient")
        self.label05 = QtWidgets.QLabel(DialogSamplingWindow)
        self.label05.setGeometry(QtCore.QRect(160, 10, 60, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label05.sizePolicy().hasHeightForWidth())
        self.label05.setSizePolicy(sizePolicy)
        self.label05.setMinimumSize(QtCore.QSize(60, 25))
        self.label05.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(10)
        self.label05.setFont(font)
        self.label05.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label05.setObjectName("label05")
        self.labelSupervisor = QtWidgets.QLabel(DialogSamplingWindow)
        self.labelSupervisor.setEnabled(True)
        self.labelSupervisor.setGeometry(QtCore.QRect(10, 10, 150, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSupervisor.sizePolicy().hasHeightForWidth())
        self.labelSupervisor.setSizePolicy(sizePolicy)
        self.labelSupervisor.setMinimumSize(QtCore.QSize(150, 25))
        self.labelSupervisor.setMaximumSize(QtCore.QSize(150, 20))
        self.labelSupervisor.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.labelSupervisor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelSupervisor.setText("")
        self.labelSupervisor.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelSupervisor.setObjectName("labelSupervisor")
        self.label06 = QtWidgets.QLabel(DialogSamplingWindow)
        self.label06.setGeometry(QtCore.QRect(160, 40, 60, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label06.sizePolicy().hasHeightForWidth())
        self.label06.setSizePolicy(sizePolicy)
        self.label06.setMinimumSize(QtCore.QSize(60, 25))
        self.label06.setMaximumSize(QtCore.QSize(60, 25))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(10)
        self.label06.setFont(font)
        self.label06.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label06.setObjectName("label06")
        self.labelLaboratory = QtWidgets.QLabel(DialogSamplingWindow)
        self.labelLaboratory.setEnabled(True)
        self.labelLaboratory.setGeometry(QtCore.QRect(10, 40, 150, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLaboratory.sizePolicy().hasHeightForWidth())
        self.labelLaboratory.setSizePolicy(sizePolicy)
        self.labelLaboratory.setMinimumSize(QtCore.QSize(150, 25))
        self.labelLaboratory.setMaximumSize(QtCore.QSize(150, 20))
        self.labelLaboratory.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.labelLaboratory.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelLaboratory.setText("")
        self.labelLaboratory.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelLaboratory.setObjectName("labelLaboratory")
        self.label01 = QtWidgets.QLabel(DialogSamplingWindow)
        self.label01.setGeometry(QtCore.QRect(530, 10, 60, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label01.sizePolicy().hasHeightForWidth())
        self.label01.setSizePolicy(sizePolicy)
        self.label01.setMinimumSize(QtCore.QSize(60, 25))
        self.label01.setMaximumSize(QtCore.QSize(60, 25))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(9)
        self.label01.setFont(font)
        self.label01.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label01.setObjectName("label01")
        self.labelProjectID = QtWidgets.QLabel(DialogSamplingWindow)
        self.labelProjectID.setEnabled(True)
        self.labelProjectID.setGeometry(QtCore.QRect(450, 10, 80, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelProjectID.sizePolicy().hasHeightForWidth())
        self.labelProjectID.setSizePolicy(sizePolicy)
        self.labelProjectID.setMinimumSize(QtCore.QSize(80, 25))
        self.labelProjectID.setMaximumSize(QtCore.QSize(60, 25))
        self.labelProjectID.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelProjectID.setText("")
        self.labelProjectID.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelProjectID.setObjectName("labelProjectID")
        self.tableView = QtWidgets.QTableView(DialogSamplingWindow)
        self.tableView.setGeometry(QtCore.QRect(10, 110, 580, 280))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMinimumSize(QtCore.QSize(580, 280))
        self.tableView.setMaximumSize(QtCore.QSize(580, 280))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(10)
        self.tableView.setFont(font)
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setTabKeyNavigation(True)
        self.tableView.setProperty("showDropIndicator", True)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.verticalHeader().setHighlightSections(True)
        self.pushButtonAddSpecimen = QtWidgets.QPushButton(DialogSamplingWindow)
        self.pushButtonAddSpecimen.setEnabled(False)
        self.pushButtonAddSpecimen.setGeometry(QtCore.QRect(10, 75, 32, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAddSpecimen.sizePolicy().hasHeightForWidth())
        self.pushButtonAddSpecimen.setSizePolicy(sizePolicy)
        self.pushButtonAddSpecimen.setMinimumSize(QtCore.QSize(32, 32))
        self.pushButtonAddSpecimen.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButtonAddSpecimen.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ImageIcons/Icons/Slump.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAddSpecimen.setIcon(icon4)
        self.pushButtonAddSpecimen.setIconSize(QtCore.QSize(28, 33))
        self.pushButtonAddSpecimen.setFlat(True)
        self.pushButtonAddSpecimen.setObjectName("pushButtonAddSpecimen")

        self.retranslateUi(DialogSamplingWindow)
        QtCore.QMetaObject.connectSlotsByName(DialogSamplingWindow)

    def retranslateUi(self, DialogSamplingWindow):
        _translate = QtCore.QCoreApplication.translate
        DialogSamplingWindow.setWindowTitle(_translate("DialogSamplingWindow", "نمونه‌گیری"))
        self.label02.setText(_translate("DialogSamplingWindow", "شماره قرارداد:"))
        self.label03.setText(_translate("DialogSamplingWindow", "نام پروژه:"))
        self.label04.setText(_translate("DialogSamplingWindow", "نام کارفرما:"))
        self.label05.setText(_translate("DialogSamplingWindow", "مشاور:"))
        self.label06.setText(_translate("DialogSamplingWindow", "آزمایشگاه:"))
        self.label01.setText(_translate("DialogSamplingWindow", "شناسه پروژه:"))
import ImageIcons_rc
