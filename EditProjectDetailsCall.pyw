import sys, sqlite3
from PyQt5 import QtWidgets, QtGui, QtCore
from EditProjectDetails import *

class Form_DialogEditProjectDetails(QtWidgets.QDialog):
    def __init__(self, ProjectID, ContractNumber, ProjectName, Client, Supervisor, Labratory, Address):
        super().__init__()
        self.statusmode = 0
        self.ProjectID = ProjectID
        self.ContractNumber = ContractNumber
        self.ProjectName = ProjectName
        self.Client = Client
        self.Supervisor = Supervisor
        self.Labratory = Labratory
        self.Address = Address
        self.uiEdit = Ui_DialogEditProjectDetails()
        self.uiEdit.setupUi(self)
        self.PreviousData()
        self.uiEdit.pushButtonCancel.clicked.connect(self.close)
        self.uiEdit.pushButtonEditProject.clicked.connect(self.AcceptDialog)

    def PreviousData(self):
        self.uiEdit.lineEditContractNumber.setText(self.ContractNumber)
        self.uiEdit.lineEditProjectName.setText(self.ProjectName)
        self.uiEdit.lineEditClient.setText(self.Client)
        self.uiEdit.lineEditSupervisor.setText(self.Supervisor)
        self.uiEdit.lineEditLabratory.setText(self.Labratory)
        self.uiEdit.lineEditAddress.setText(self.Address)

    def AcceptDialog(self):
        fillCondition = (
            len(self.uiEdit.lineEditContractNumber.text()) == 0,
            len(self.uiEdit.lineEditProjectName.text()) == 0,
            len(self.uiEdit.lineEditClient.text()) == 0,
            len(self.uiEdit.lineEditSupervisor.text()) == 0,
            len(self.uiEdit.lineEditLabratory.text()) == 0,
            len(self.uiEdit.lineEditAddress.text()) == 0
        )
        if any(fillCondition):
            QMB = QtWidgets.QMessageBox.critical(self, "خطا", "لطفاً همه فیلدها را تکمیل نمایید.")
        else:
            a1 = self.uiEdit.lineEditContractNumber.text()
            a2 = self.uiEdit.lineEditProjectName.text()
            a3 = self.uiEdit.lineEditClient.text()
            a4 = self.uiEdit.lineEditSupervisor.text()
            a5 = self.uiEdit.lineEditLabratory.text()
            a6 = self.uiEdit.lineEditAddress.text()
            a7 = self.ProjectID
            try:
                conn = sqlite3.connect("MainDB.db")
                cur = conn.cursor()
                cur.execute("UPDATE Projects SET ContractNumber=? WHERE ProjectID=?", (a1, a7))
                cur.execute("UPDATE Projects SET ProjectName=? WHERE ProjectID=?", (a2, a7))
                cur.execute("UPDATE Projects SET Client=? WHERE ProjectID=?", (a3, a7))
                cur.execute("UPDATE Projects SET Supervisor=? WHERE ProjectID=?", (a4, a7))
                cur.execute("UPDATE Projects SET Laboratory=? WHERE ProjectID=?", (a5, a7))
                cur.execute("UPDATE Projects SET Address=? WHERE ProjectID=?", (a6, a7))
                conn.commit()
                self.statusmode = 1
                print("Project successfully edited.")
            except sqlite3.OperationalError:
                print("There seems to be a problem in sql opration.")
            finally:
                conn.close()
                self.close()
                return self.statusmode
   
# if __name__ == "__main__":
#     appEdit = QtWidgets.QApplication(sys.argv)
#     wEdit = Form_DialogEditProjectDetails()
#     wEdit.show()
#     sys.exit(appEdit.exec_())
