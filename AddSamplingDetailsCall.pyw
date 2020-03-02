import sys, sqlite3, jdatetime
from PyQt5 import QtWidgets, QtGui, QtCore
from AddSamplingDetails import *

class Form_DialogAddSamplingDetails(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.statusmode = 0
        self.project_id = 0
        self.ui = Ui_DialogAddSamplingDetails()
        self.ui.setupUi(self)
        self.ui.comboBoxYear.currentIndexChanged.connect(self.TrigerMount)
        self.ui.comboBoxMount.currentIndexChanged.connect(self.TrigerDay)
        self.ui.pushButtonCancelSampling.clicked.connect(self.close)
        self.ui.pushButtonCreateSampling.clicked.connect(self.CreateNewSampling)

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

    def setProjectID(self, project_id):
        self.project_id = project_id

    def isValid_fc(self):
        Valid_fc = (
            self.ui.lineEdit_fc.text().isdigit()
            or
            self.ui.lineEdit_fc.text().replace('.','',1).isdigit())
        if not Valid_fc:
            return False
        return True
        
    def CreateNewSampling(self):
        fillCondition =(
            self.ui.comboBoxElement.currentIndex() == 0,
            len(self.ui.lineEditStory.text()) == 0,
            len(self.ui.lineEditLevel.text()) == 0,
            not self.ui.comboBoxDay.isEnabled(),
            self.ui.comboBoxDay.currentIndex()== 0,
            len(self.ui.lineEdit_fc.text()) == 0,
            self.ui.comboBoxCementType.currentIndex() == 0
        )
        if any(fillCondition):
            QMB = QtWidgets.QMessageBox.critical(self, "خطا", "لطفاً همه فیلدها را تکمیل نمایید.")
            return
        else:
            if not self.isValid_fc():
                QMB = QtWidgets.QMessageBox.critical(self, "خطا", "مقاومت مشخصه وارد شده نامعتبر است.")
                return
            else:
                try:
                    conn = sqlite3.connect('MainDB.db')
                    cur = conn.cursor()
                    sampling_date = jdatetime.datetime(int(self.ui.comboBoxYear.currentText()),int(self.ui.comboBoxMount.currentText()), int(self.ui.comboBoxDay.currentText()), locale='fa_IR')
                    SamplingInput = (
                        self.project_id,
                        self.ui.comboBoxElement.currentText(),
                        self.ui.lineEditStory.text(),
                        self.ui.lineEditLevel.text(),
                        sampling_date.strftime("%Y/%m/%d"),
                        self.ui.lineEdit_fc.text(),
                        self.ui.comboBoxCementType.currentText()
                    )
                    sqlexpr = "INSERT INTO Sampling (ProjectID, Element, Story, Level, SamplingDate, fc, CementType) VALUES (?, ?, ?, ?, ?, ?, ?)"
                    cur.execute(sqlexpr, SamplingInput)
                    conn.commit()
                    print("New Samplign Added")
                    self.statusmode = 1
                except sqlite3.Error as err:
                    print(err)
                finally:
                    conn.close()
                    self.close()
                    return self.statusmode

# if __name__ =="__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     w = Form_DialogAddSamplingDetails()
#     w.show()
#     sys.exit(app.exec_())