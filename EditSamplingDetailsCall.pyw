import sys, sqlite3
import jdatetime
from PyQt5 import QtWidgets, QtGui, QtCore
from EditSamplingDetails import *
from VerificationConcrete_rev01 import *

class Form_DialogEditSamplingDetails(QtWidgets.QDialog):
    def __init__(self, SamplingID, Element, Story, Level, Year, Mount, Day, fc, CementType):
        super().__init__()
        self.statusmode = 0
        self.SamplingID = SamplingID
        self.Element = Element
        self.Story = Story
        self.Level = Level
        self.Year = Year
        self.Mount = Mount
        self.Day = Day
        self.fc = fc
        self.CementType = CementType        
        self.ui = Ui_DialogEditSamplingDetails()
        self.ui.setupUi(self)
        self.ui.comboBoxYear.currentIndexChanged.connect(self.TrigerMount)
        self.ui.comboBoxMount.currentIndexChanged.connect(self.TrigerDay)
        self.PreviousData()
        self.ui.pushButtonCancelSampling.clicked.connect(self.close)
        self.ui.pushButtonEditSampling.clicked.connect(self.AcceptDialog)

    def TrigerMount(self):
        if self.ui.comboBoxYear.currentIndex() == 0:
            self.ui.comboBoxMount.clear()
            self.ui.comboBoxMount.addItem("ماه")
            self.ui.comboBoxMount.setEnabled(False)
        else:
            self.ui.comboBoxMount.setEnabled(True)
            self.ui.comboBoxMount.clear()
            self.ui.comboBoxMount.addItem("ماه")
            for i in range(1, 13):
                self.ui.comboBoxMount.addItem(str(i).zfill(2))

    def TrigerDay(self):
        if self.ui.comboBoxMount.currentIndex() == 0:
            self.ui.comboBoxDay.clear()
            self.ui.comboBoxDay.addItem("روز")
            self.ui.comboBoxDay.setEnabled(False)
        else:
            self.ui.comboBoxDay.setEnabled(True)
            self.ui.comboBoxDay.clear()
            self.ui.comboBoxDay.addItem("روز")
            cond = self.ui.comboBoxYear.itemText(self.ui.comboBoxYear.currentIndex()) not in ("1399", "1403", "1408")
            Mount = self.ui.comboBoxMount.currentIndex()
            if cond:
                if 0 < Mount < 7:
                    for i in range(1,32):
                        self.ui.comboBoxDay.addItem(str(i).zfill(2))
                elif 6 < Mount < 12:
                    for i in range(1,31):
                        self.ui.comboBoxDay.addItem(str(i).zfill(2))
                else:
                    for i in range(1,30):
                        self.ui.comboBoxDay.addItem(str(i).zfill(2))
            else:
                if 0 < Mount < 7:
                    for i in range(1,32):
                        self.ui.comboBoxDay.addItem(str(i).zfill(2))
                elif 6 < Mount < 13:
                    for i in range(1,31):
                        self.ui.comboBoxDay.addItem(str(i).zfill(2))
    
    def PreviousData(self):
        self.ui.lineEditStory.setText(self.Story)
        self.ui.lineEditLevel.setText(self.Level)
        self.ui.lineEdit_fc.setText(self.fc)
        element_index = self.ui.comboBoxElement.findText(self.Element, QtCore.Qt.MatchFixedString)
        if element_index >= 0:
            self.ui.comboBoxElement.setCurrentIndex(element_index)
        year_index = self.ui.comboBoxYear.findText(self.Year, QtCore.Qt.MatchFixedString)
        if year_index >= 0:
            self.ui.comboBoxYear.setCurrentIndex(year_index)
        mount_index = self.ui.comboBoxMount.findText(self.Mount, QtCore.Qt.MatchFixedString)
        if mount_index >= 0:
            self.ui.comboBoxMount.setCurrentIndex(mount_index)
        day_index = self.ui.comboBoxDay.findText(self.Day, QtCore.Qt.MatchFixedString)
        if day_index >= 0:
            self.ui.comboBoxDay.setCurrentIndex(day_index)
        cement_type_index = self.ui.comboBoxCementType.findText(self.CementType, QtCore.Qt.MatchFixedString)
        if cement_type_index >= 0:
            self.ui.comboBoxCementType.setCurrentIndex(cement_type_index)

    def isValid_fc(self):
        Valid_fc = (
            self.ui.lineEdit_fc.text().isdigit()
            or
            self.ui.lineEdit_fc.text().replace('.','',1).isdigit())
        if not Valid_fc:
            return False
        return True

    def AcceptDialog(self):
        fillCondition =(
            self.ui.comboBoxElement.currentIndex() == 0,
            len(self.ui.lineEditStory.text()) == 0,
            len(self.ui.lineEditLevel.text()) == 0,
            not self.ui.comboBoxDay.isEnabled(),
            self.ui.comboBoxDay.currentIndex()== 0,
            len(self.ui.lineEdit_fc.text()) == 0,
            self.ui.comboBoxCementType.currentIndex() == 0)

        if any(fillCondition):
            QMB1 = QtWidgets.QMessageBox.critical(self, "خطا", "لطفاً همه فیلدها را تکمیل نمایید.")
            return
        else:
            if not self.isValid_fc():
                QMB = QtWidgets.QMessageBox.critical(self, "خطا", "مقاومت مشخصه وارد شده نامعتبر است.")
                return
            else:
                a4 = self.ui.comboBoxYear.currentText()
                a5 = self.ui.comboBoxMount.currentText()
                a6 = self.ui.comboBoxDay.currentText()
                d1 = jdatetime.datetime(int(a4), int(a5), int(a6))
                conn = sqlite3.connect("MainDB.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM Specimen WHERE SamplingID=%s" % self.SamplingID)
                dateValid = False
                for item in cur:
                    d2 = jdatetime.datetime(int(item[6].split('/')[0]),
                                            int(item[6].split('/')[1]),
                                            int(item[6].split('/')[2]))
                    delta = (d2-d1).days
                    # print(delta)
                    if delta<=0:
                        dateValid = True
                        break
                if dateValid:
                    QMB2 = QtWidgets.QMessageBox.critical(self, "خطا", "تاریخ نمونه‌گیری ویرایش شده نمی‌تواند بعد از تاریخ تست نمونه‌های موجود باشد.")
                else:
                    a0 = self.SamplingID
                    a1 = self.ui.comboBoxElement.currentText()
                    a2 = self.ui.lineEditStory.text()
                    a3 = self.ui.lineEditLevel.text()
                    a4 = self.ui.comboBoxYear.currentText()
                    a5 = self.ui.comboBoxMount.currentText()
                    a6 = self.ui.comboBoxDay.currentText()
                    a7 = self.ui.lineEdit_fc.text()
                    a8 = self.ui.comboBoxCementType.currentText()
                    a9 = a4+"/"+a5+"/"+a6
                    try:
                        conn = sqlite3.connect('MainDB.db')
                        cur = conn.cursor()
                        cur.execute("UPDATE Sampling SET Element=? WHERE SamplingID=?", (a1, a0))
                        cur.execute("UPDATE Sampling SET Story=? WHERE SamplingID=?", (a2, a0))
                        cur.execute("UPDATE Sampling SET Level=? WHERE SamplingID=?", (a3, a0))
                        cur.execute("UPDATE Sampling SET SamplingDate=? WHERE SamplingID=?", (a9, a0))
                        cur.execute("UPDATE Sampling SET fc=? WHERE SamplingID=?", (a7, a0))
                        cur.execute("UPDATE Sampling SET CementType=? WHERE SamplingID=?", (a8, a0))
                        conn.commit()   

                        cur.execute("SELECT * FROM Specimen WHERE SamplingID=%s" % self.SamplingID)
                        lst = list(cur)
                        if len(lst)!=0:
                            for specimen in lst:
                                Sp = Specimen()
                                b0 = specimen[1]
                                b1 = Sp.Set_MoldShape(specimen[3])
                                b2 = Sp.Set_Dimension(specimen[4])
                                b3 = Sp.Set_SamplingDate(int(a4), int(a5), int(a6))
                                b4 = Sp.Set_TestDate(int(specimen[6].split('/')[0]),
                                                    int(specimen[6].split('/')[1]),
                                                    int(specimen[6].split('/')[2]))
                                b5 = Sp.Set_Age()
                                cur.execute("UPDATE Specimen SET Age=? WHERE AutoSpecimenID=?", (b5, b0))
                                b6 = Sp.Set_UltimatForce(specimen[7])
                                b7 = Sp.Set_Area()
                                b8 = Sp.Set_CompressiveStrenght()
                                b9 = Sp.Set_Name()
                                b10 = Sp.Get_r1()
                                b11 = Sp.Get_r2()
                                b12 = Sp.Get_r3()
                                b13 = Sp.Set_CementType(a8)
                                r4 = Sp.Cement_Conversion()
                                cur.execute("UPDATE Specimen SET r4=? WHERE AutoSpecimenID=?", (r4, b0))
                                b14 = Sp.Convert2Standard()
                                cur.execute("UPDATE Specimen SET StadardCompressionStrenght=? WHERE AutoSpecimenID=?", (b14, b0))
                                conn.commit()
                        
                        print("Samplign Edited")
                        self.statusmode = 2
                    except sqlite3.Error as err:
                        print(err)
                    finally:
                        conn.close()
                        if self.statusmode ==2:
                            self.close()


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     w = Form_DialogEditSamplingDetails()
#     w.show()
#     sys.exit(app.exec_())