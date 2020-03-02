import sys, sqlite3
from PyQt5 import QtWidgets, QtGui, QtCore
from EditSpecimenDetails import *
from VerificationConcrete_rev01 import *

class Form_DialogEditSpecimenDetails(QtWidgets.QDialog):
    def __init__(self, AutoSpecimenID, ManualSpecimenID, MoldShape, Dimension, Wieght, Year, Mount, Day, UltimatForce):
        super().__init__()
        self.statusmode = 0
        self.AutoSpecimenID = AutoSpecimenID
        self.ManualSpecimenID = ManualSpecimenID
        self.MoldShape = MoldShape
        self.Dimension = Dimension
        self.Wieght = Wieght
        self.Year = Year
        self.Mount = Mount
        self.Day = Day
        self.UltimatForce = UltimatForce
        self.ui = Ui_DialogEditSpecimenDetails()
        self.ui.setupUi(self)
        self.ui.radioButtonCylindrical.toggled.connect(self.setCylindrical)
        self.ui.radioButtonCubic.toggled.connect(self.setCubic)
        self.ui.comboBoxYearTestDate.currentIndexChanged.connect(self.TrigerMount)
        self.ui.comboBoxMountTestDate.currentIndexChanged.connect(self.TrigerDay)
        self.PreviousData()
        self.ui.pushButtonCancelSpecimen.clicked.connect(self.close)
        self.ui.pushButtonEditSpecimen.clicked.connect(self.EditSpecimen)

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
    def PreviousData(self):
        self.ui.lineEditManualSpecimenID.setText(self.ManualSpecimenID)
        self.ui.lineEditWieght.setText(self.Wieght)
        self.ui.lineEditUltimatForce.setText(self.UltimatForce)
        
        if self.MoldShape == "استوانه‌ای":
            self.ui.radioButtonCylindrical.setChecked(True)
        else:
            self.ui.radioButtonCubic.setChecked(True)

        dim_index = self.ui.comboBoxDimention.findText(self.Dimension, QtCore.Qt.MatchFixedString)
        if dim_index >= 0:
            self.ui.comboBoxDimention.setCurrentIndex(dim_index)

        year_index = self.ui.comboBoxYearTestDate.findText(self.Year, QtCore.Qt.MatchFixedString)
        if year_index >= 0:
            self.ui.comboBoxYearTestDate.setCurrentIndex(year_index)

        mount_index = self.ui.comboBoxMountTestDate.findText(self.Mount, QtCore.Qt.MatchFixedString)
        if mount_index >= 0:
            self.ui.comboBoxMountTestDate.setCurrentIndex(mount_index)

        day_index = self.ui.comboBoxDayTestDate.findText(self.Day, QtCore.Qt.MatchFixedString)
        if day_index >= 0:
            self.ui.comboBoxDayTestDate.setCurrentIndex(day_index)
    
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
        len(self.ui.lineEditUltimatForce.text()) == 0)
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
        self.ui.lineEditUltimatForce.text().isdigit()
        or
        self.ui.lineEditUltimatForce.text().replace('.','',1).isdigit())
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

    def EditSpecimen(self):
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
                                a0 = self.AutoSpecimenID

                                a1 = Sp.Set_ManualSpecimenID(self.ui.lineEditManualSpecimenID.text())
                                cur.execute("UPDATE Specimen SET ManualSpecimenID=? WHERE AutoSpecimenID=?", (a1, a0))

                                a2 = Sp.Set_MoldShape(mold_shape)
                                cur.execute("UPDATE Specimen SET MoldShape=? WHERE AutoSpecimenID=?", (a2, a0))

                                a3 = Sp.Set_Dimension(self.ui.comboBoxDimention.currentText())
                                cur.execute("UPDATE Specimen SET Dimension=? WHERE AutoSpecimenID=?", (a3, a0))

                                a4 = Sp.Set_Wieght(self.ui.lineEditWieght.text())
                                cur.execute("UPDATE Specimen SET Wieght=? WHERE AutoSpecimenID=?", (a4, a0))

                                Sp.Set_SamplingDate(int(self.sampling_date.split("/")[0]),
                                                    int(self.sampling_date.split("/")[1]),
                                                    int(self.sampling_date.split("/")[2]))
                                a5 = Sp.Set_TestDate(int(self.ui.comboBoxYearTestDate.currentText()),
                                                    int(self.ui.comboBoxMountTestDate.currentText()),
                                                    int(self.ui.comboBoxDayTestDate.currentText()))
                                cur.execute("UPDATE Specimen SET TestDate=? WHERE AutoSpecimenID=?", (a5.strftime("%Y/%m/%d"), a0))

                                a6 = Sp.Set_UltimatForce(self.ui.lineEditUltimatForce.text())
                                cur.execute("UPDATE Specimen SET UltimatForce=? WHERE AutoSpecimenID=?", (a6, a0))

                                a7 = Sp.Set_Area()
                                cur.execute("UPDATE Specimen SET Area=? WHERE AutoSpecimenID=?", (a7, a0))

                                a8 = Sp.Set_Volume()
                                cur.execute("UPDATE Specimen SET Volume=? WHERE AutoSpecimenID=?", (a8, a0))

                                a9 = Sp.Set_Gamma()
                                cur.execute("UPDATE Specimen SET Gamma=? WHERE AutoSpecimenID=?", (a9, a0))

                                Sp.Set_Age() 
                                a10 = Sp.Age.days
                                cur.execute("UPDATE Specimen SET Age=? WHERE AutoSpecimenID=?", (a10, a0))

                                a11 = Sp.Set_CompressiveStrenght()
                                cur.execute("UPDATE Specimen SET CompressiveStrenght=? WHERE AutoSpecimenID=?", (a11, a0))
                                
                                Sp.Set_CementType(self.cement_type)
                                a12 = Sp.Set_Name()
                                cur.execute("UPDATE Specimen SET Name=? WHERE AutoSpecimenID=?", (a12, a0))

                                r1 = Sp.Get_r1()
                                cur.execute("UPDATE Specimen SET r1=? WHERE AutoSpecimenID=?", (r1, a0))

                                r2 = Sp.Get_r2()
                                cur.execute("UPDATE Specimen SET r2=? WHERE AutoSpecimenID=?", (r2, a0))

                                r3 = Sp.Get_r3()
                                cur.execute("UPDATE Specimen SET r3=? WHERE AutoSpecimenID=?", (r3, a0))

                                r4 = Sp.Cement_Conversion()
                                cur.execute("UPDATE Specimen SET r4=? WHERE AutoSpecimenID=?", (r4, a0))

                                a13 = Sp.Convert2Standard()
                                cur.execute("UPDATE Specimen SET StadardCompressionStrenght=? WHERE AutoSpecimenID=?", (a13, a0))
                                conn.commit()
                                print("Specimen Edit Successfully.")
                            except sqlite3.Error as err:
                                print(err)
                            finally:
                                conn.close()
                                self.close()
                        


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     w = Form_DialogEditSamplingDetails()
#     w.show()
#     sys.exit(app.exec_())


    

