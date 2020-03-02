import sys, sqlite3
from PyQt5 import QtWidgets, QtGui, QtCore
from DeleteSpecimenWarning import *

class Form_DialogDeleteSpecimen(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.statusmode = 0
        self.ui = Ui_DialogDeleteSpecimen()
        self.ui.setupUi(self)
        msg = "آیا مطمئن هستید که می‌خواهید « نمونه‌ » انتخاب شده را حذف نمایید؟"
        self.ui.labelDeleteMessege.setText(msg)
        self.ui.pushButtonCancelDelete.clicked.connect(self.close)
        self.ui.pushButtonYesDelete.clicked.connect(self.DeleteSpecimen)

    def setSpecimenID(self, specimen_id):
        self.specimen_id = specimen_id
        
    def DeleteSpecimen(self):
        conn = sqlite3.connect("MainDB.db")
        cur = conn.cursor()
        sqlexpr = "DELETE FROM Specimen WHERE AutoSpecimenID = %s" % self.specimen_id
        cur.execute(sqlexpr) 
        conn.commit()
        conn.close()
        self.close()
        self.statusmode = -1
        print("Specimen Deleted")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Form_DialogDeleteSpecimen()
    w.show()
    sys.exit(app.exec_())