import sys, sqlite3
import jdatetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from AddSpecimenDetails import *
from VerificationConcrete_rev01 import *

class Form_DialogAddSpecimenDetails(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogAddSpecimenDetails()
        self.ui.setupUi(self)
        self.ui.radioButtonCylindrical.toggled.connect(self.setCylindrical)
        self.ui.radioButtonCubic.toggled.connect(self.setCubic)
        self.ui.comboBoxYearTestDate.currentIndexChanged.connect(self.TrigerMount)
        self.ui.comboBoxMountTestDate.currentIndexChanged.connect(self.TrigerDay)
        self.ui.pushButtonCancelSpecimen.clicked.connect(self.close)
        self.ui.pushButtonCreateSpecimen.clicked.connect(self.CreateNewSpecimen)
        
    def setCylindrical(self):
        self.ui.labelDimention.setText(" قطر (سانتی‌متر)")
        self.ui.comboBoxDimention.clear()
        for i in ('','10', '15', '20', '25', '30'):
            self.ui.comboBoxDimention.addItem(i)

    def setCubic(self):
        self.ui.labelDimention.setText(" ضلع (سانتی‌متر)")
        self.ui.comboBoxDimention.clear()
        for i in ('','10', '15', '20', '25', '30'):
            self.ui.comboBoxDimention.addItem(i)

    def TrigerMount(self):
        if self.ui.comboBoxYearTestDate.currentIndex() == 0:
            self.ui.comboBoxMountTestDate.clear()
            self.ui.comboBoxMountTestDate.addItem("ماه")
            self.ui.comboBoxMountTestDate.setEnabled(False)
        else:
            self.ui.comboBoxMountTestDate.setEnabled(True)
            self.ui.comboBoxMountTestDate.clear()
            self.ui.comboBoxMountTestDate.addItem("ماه")
            for i in range(1, 13):
                self.ui.comboBoxMountTestDate.addItem(str(i).zfill(2))

    def TrigerDay(self):
        if self.ui.comboBoxMountTestDate.currentIndex() == 0:
            self.ui.comboBoxDayTestDate.clear()
            self.ui.comboBoxDayTestDate.addItem("روز")
            self.ui.comboBoxDayTestDate.setEnabled(False)
        else:
            self.ui.comboBoxDayTestDate.setEnabled(True)
            self.ui.comboBoxDayTestDate.clear()
            self.ui.comboBoxDayTestDate.addItem("روز")
            cond = self.ui.comboBoxYearTestDate.itemText(self.ui.comboBoxYearTestDate.currentIndex()) not in ("1399", "1403", "1408")
            Mount = self.ui.comboBoxMountTestDate.currentIndex()
            if cond:
                if 0 < Mount < 7:
                    for i in range(1,32):
                        self.ui.comboBoxDayTestDate.addItem(str(i).zfill(2))
                elif 6 < Mount < 12:
                    for i in range(1,31):
                        self.ui.comboBoxDayTestDate.addItem(str(i).zfill(2))
                else:
                    for i in range(1,30):
                        self.ui.comboBoxDayTestDate.addItem(str(i).zfill(2))
            else:
                if 0 < Mount < 7:
                    for i in range(1,32):
                        self.ui.comboBoxDayTestDate.addItem(str(i).zfill(2))
                elif 6 < Mount < 13:
                    for i in range(1,31):
                        self.ui.comboBoxDayTestDate.addItem(str(i).zfill(2))

    def setSamplingID(self, sampling_id):
        self.sampling_id = sampling_id

    def setSamplingData(self, sampling_date):
        self.sampling_date = sampling_date
    
    def setFprimC(self, fc):
        self.fc = fc
    
    def setCementType(self, cement_type):
        self.cement_type = cement_type

    def isFill(self):
        fillCondition = (
        len(self.ui.lineEditManualSpecimenID.text()) == 0,
        not(self.ui.radioButtonCylindrical.isChecked() or self.ui.radioButtonCubic.isChecked()),
        self.ui.comboBoxDimention.currentIndex() == 0,
        len(self.ui.lineEditWieght.text()) == 0,
        self.ui.comboBoxDayTestDate.currentIndex() == 0,
        len(self.ui.lineEditWieghtUltimatForce.text()) == 0)
        if any(fillCondition):
            return False
        return True
    def isValidManualSpecimenID(self):
        ValidManualSpecimenID = self.ui.lineEditManualSpecimenID.text().isdigit()
        if not ValidManualSpecimenID:
            return False
        return True

    def isValidWieght(self):
        ValidWieght = (
            self.ui.lineEditWieght.text().isdigit()
            or
            self.ui.lineEditWieght.text().replace('.','',1).isdigit())
        if not ValidWieght:
            return False
        return True   

    
    def isValidUltimatForce(self):
        ValidUltimatForce = (
        self.ui.lineEditWieghtUltimatForce.text().isdigit()
        or
        self.ui.lineEditWieghtUltimatForce.text().replace('.','',1).isdigit())
        if not ValidUltimatForce:
            return False
        return True 

    def isValidTestDate(self):
        date_1 = jdatetime.datetime(int(self.sampling_date.split("/")[0]),
                                    int(self.sampling_date.split("/")[1]),
                                    int(self.sampling_date.split("/")[2]), locale='fa_IR')
        date_2 =jdatetime.datetime(int(self.ui.comboBoxYearTestDate.currentText()),
                                   int(self.ui.comboBoxMountTestDate.currentText()),
                                   int(self.ui.comboBoxDayTestDate.currentText()), locale='fa_IR')
        delta = date_2 - date_1
        if delta.days<=0:
            return False
        return True
            
    def CreateNewSpecimen(self):
        if not self.isFill():
            QMB = QtWidgets.QMessageBox.critical(self, "خطا", "لطفاً همه فیلدها را تکمیل نمایید.")
            return
        else:
            if not self.isValidManualSpecimenID():
                QMB = QtWidgets.QMessageBox.critical(self, "خطا", "شماره نمونه تنها می‌تواند عدد صحیح باشد.")
                return
            else:
                if not self.isValidWieght():
                    QMB = QtWidgets.QMessageBox.critical(self, "خطا", "وزن وارد شده برای نمونه نامعتبر است.")
                    return
                else:
                    if not self.isValidUltimatForce():
                        QMB = QtWidgets.QMessageBox.critical(self, "خطا", "نیروی نهایی وارد شده نامعتبر است.")
                        return
                    else:
                        if not self.isValidTestDate():
                            QMB = QtWidgets.QMessageBox.critical(self, "خطا", "تاریخ تست نمونه نمی‌تواند قبل از تاریخ نمونه‌گیری باشد.")
                            return
                        else:
                            try:
                                conn = sqlite3.connect("MainDB.db")
                                cur = conn.cursor()
                                Sp = Specimen()
                                if self.ui.radioButtonCubic.isChecked()==True:
                                    mold_shape = "Cubic"
                                if self.ui.radioButtonCylindrical.isChecked()==True:
                                    mold_shape = "Cylindrical"
                                a0 = Sp.Set_SamplingID(self.sampling_id)
                                a1 = Sp.Set_ManualSpecimenID(self.ui.lineEditManualSpecimenID.text())
                                a2 = Sp.Set_MoldShape(mold_shape)
                                a3 = Sp.Set_Dimension(self.ui.comboBoxDimention.currentText())
                                a4 = Sp.Set_Wieght(self.ui.lineEditWieght.text())
                                Sp.Set_SamplingDate(int(self.sampling_date.split("/")[0]),
                                                    int(self.sampling_date.split("/")[1]),
                                                    int(self.sampling_date.split("/")[2]))
                                a5 = Sp.Set_TestDate(int(self.ui.comboBoxYearTestDate.currentText()),
                                                    int(self.ui.comboBoxMountTestDate.currentText()),
                                                    int(self.ui.comboBoxDayTestDate.currentText()))
                                a6 = Sp.Set_UltimatForce(self.ui.lineEditWieghtUltimatForce.text())
                                a7 = Sp.Set_Area()
                                a8 = Sp.Set_Volume()
                                a9 = Sp.Set_Gamma()
                                a10 = Sp.Set_Age()
                                a11 = Sp.Set_CompressiveStrenght()
                                Sp.Set_CementType(self.cement_type)
                                a12 = Sp.Set_Name()
                                r1 = Sp.Get_r1()
                                r2 = Sp.Get_r2()
                                r3 = Sp.Get_r3()
                                r4 = Sp.Cement_Conversion()
                                a13 = Sp.Convert2Standard()
                                SpecimenInput = (a0, a1, a2, a3, a4, a5.strftime("%Y/%m/%d"), a6, a7, a8, a9, a10, a11,a12, r1, r2, r3, r4, a13)
                                sqlexpr = """INSERT INTO Specimen (SamplingID, ManualSpecimenID, MoldShape, Dimension, Wieght, TestDate, UltimatForce,
                                                        Area, Volume, Gamma, Age, CompressiveStrenght, Name, r1, r2, r3, r4, StadardCompressionStrenght)
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
                                cur.execute(sqlexpr, SpecimenInput)
                                conn.commit()
                                print("New Specimen Created.")
                            except sqlite3.Error as err:
                                print(err)
                            finally:
                                conn.close()
                                self.close()
    
# if __name__=="__main__":
#     app = QApplication(sys.argv)
#     w = Form_DialogAddSpecimenDetails()
#     w.show()
#     sys.exit(app.exec())