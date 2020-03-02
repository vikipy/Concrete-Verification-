import sys, sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui
from AddProjectDetails import *

class Form_DialogAddProjectDetails(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.statusmode = 0
        self.uiAdd = Ui_DialogAddProjectDetails()
        self.uiAdd.setupUi(self)
        self.uiAdd.pushButtonCancel.clicked.connect(self.close)
        self.uiAdd.pushButtonCreatNewProject.clicked.connect(self.AcceptDialog)

    def AcceptDialog(self):
        fillCondition = (
            len(self.uiAdd.lineEditContractNumber.text()) == 0,
            len(self.uiAdd.lineEditProjectName.text()) == 0,
            len(self.uiAdd.lineEditClient.text()) == 0,
            len(self.uiAdd.lineEditSupervisor.text()) == 0,
            len(self.uiAdd.lineEditLabratory.text()) == 0,
            len(self.uiAdd.lineEditAddress.text()) == 0
        )
        if any(fillCondition):
            QMB = QtWidgets.QMessageBox.critical(self, "خطا", "لطفاً همه فیلدها را تکمیل نمایید.")
        else:
            try:
                conn = sqlite3.connect("MainDB.db")
                cur = conn.cursor()
                sqlexpr = "INSERT INTO Projects (ContractNumber, ProjectName, Client, Supervisor, Laboratory, Address) VALUES (?, ?, ?, ?, ?, ?)"
                ProjectInput = (
                    self.uiAdd.lineEditContractNumber.text(),
                    self.uiAdd.lineEditProjectName.text(),
                    self.uiAdd.lineEditClient.text(),
                    self.uiAdd.lineEditSupervisor.text(),
                    self.uiAdd.lineEditLabratory.text(),
                    self.uiAdd.lineEditAddress.text()
                )
                cur.execute(sqlexpr, ProjectInput)
                conn.commit()
                self.statusmode = 1
                print("New Project Added.")
            except sqlite3.OperationalError:
                print("There seems to be a problem in sql opration.")
            finally:
                conn.close()
                self.close()
                return self.statusmode

# if __name__ == "__main__":
#     appAdd = QtWidgets.QApplication(sys.argv)
#     wAdd = Form_DialogAddProjectDetails()
#     wAdd.show()
#     sys.exit(appAdd.exec_())
