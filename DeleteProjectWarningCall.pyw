import sys, sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui
from DeleteProjectWarning import *

class Form_DialogDeleteProject(QtWidgets.QDialog):
    def __init__(self, project_id, project_name):
        super().__init__()
        self.statusmode = 0
        self.project_id = project_id
        self.project_name = project_name
        self.uiDel = Ui_DialogDeleteProject()
        self.uiDel.setupUi(self)
        msg = "آیا مطمئن هستید که می‌خواهید پروژه %s حذف گردد." % self.project_name
        self.uiDel.labelDeleteMessege.setText(msg)
        self.uiDel.pushButtonCancelDelete.clicked.connect(self.close)
        self.uiDel.pushButtonYesDelete.clicked.connect(self.DeleteProjet)

    def DeleteProjet(self):
        conn = sqlite3.connect("MainDB.db")
        cur = conn.cursor()
        sqlexpr = "DELETE FROM Projects WHERE ProjectID = %s" % self.project_id
        cur.execute(sqlexpr) 
        conn.commit()
        conn.close()
        print("Project deleted.")
        self.close()
        self.statusmode = -1

# if __name__ == "__main__":
#     appDel = QtWidgets.QApplication(sys.argv)
#     wDel = Form_DialogDeleteProject()
#     wDel.show()
#     sys.exit(appDel.exec_())

