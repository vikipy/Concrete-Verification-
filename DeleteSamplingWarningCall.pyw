import sys, sqlite3
from PyQt5 import QtWidgets, QtGui, QtCore
from DeleteSamplingWarning import *

class Form_DialogDeleteSampling(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.statusmode = 0
        self.ui = Ui_DialogDeleteSampling()
        self.ui.setupUi(self)
        msg = "آیا مطمئن هستید که می‌خواهید نمونه‌گیری را حذف نمایید؟"
        self.ui.labelDeleteMessege.setText(msg)
        self.ui.pushButtonCancelDelete.clicked.connect(self.close)
        self.ui.pushButtonYesDelete.clicked.connect(self.DeleteSampling)

    def setSamplingID(self, samplgin_id):
        self.sampling_id = samplgin_id
        
    def DeleteSampling(self):
        conn = sqlite3.connect("MainDB.db")
        cur = conn.cursor()
        sqlexpr = "DELETE FROM Sampling WHERE SamplingID = %s" % self.sampling_id
        cur.execute(sqlexpr) 
        conn.commit()
        conn.close()
        self.close()
        self.statusmode = -1
        print("Sampling Deleted")


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     w = Form_DialogDeleteSampling()
#     w.show()
#     sys.exit(app.exec_())

