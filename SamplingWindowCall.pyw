import sys, sqlite3
from PyQt5 import QtWidgets, QtGui, QtCore
from SamplingWindow import *
import AddSamplingDetailsCall as ASDC
import DeleteSamplingWarningCall as DSWC
import EditSamplingDetailsCall as ESDC
import SpecimenWindowCall as SpWC

class From_DialogSamplingWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.project_id = 0
        self.statusmode = 0
        self.ui = Ui_DialogSamplingWindow()
        self.ui.setupUi(self)
        self.ui.tableView.clicked.connect(self.Enable)
        self.ui.pushButtonAddSampling.clicked.connect(self.ConnectAddSampling)
        self.ui.pushButtonDelSampling.clicked.connect(self.ConnectDelSampling)
        self.ui.pushButtonEditSampling.clicked.connect(self.ConnectEditSampling)
        self.ui.pushButtonAddSpecimen.clicked.connect(self.ConnectSpecimen)
        
    def Enable(self):
        self.ui.pushButtonDelSampling.setEnabled(True)
        self.ui.pushButtonEditSampling.setEnabled(True)
        self.ui.pushButtonAddSpecimen.setEnabled(True)

    def Disable(self):
        self.ui.pushButtonDelSampling.setEnabled(False)
        self.ui.pushButtonEditSampling.setEnabled(False)
        self.ui.pushButtonAddSpecimen.setEnabled(False)
    
    def setProjectID(self, project_id):
        self.project_id = project_id

    def DB_Connect(self):
        try:
            conn = sqlite3.connect("MainDB.db")
            cur = conn.cursor()

            cur.execute("SELECT * FROM Projects WHERE ProjectID=%s" % self.project_id)
            lst = list(cur)
            self.ui.labelProjectID.setText(str(lst[0][0]))
            self.ui.labelContractNumber.setText(str(lst[0][1]))
            self.ui.labelProjectName.setText(str(lst[0][2]))
            self.ui.labelClient.setText(str(lst[0][3]))
            self.ui.labelSupervisor.setText(str(lst[0][4]))
            self.ui.labelLaboratory.setText(str(lst[0][5]))

            cur.execute("SELECT SamplingID, Element, Story, Level, SamplingDate, fc, CementType FROM Sampling WHERE ProjectID=%s" % self.project_id)
            self.model = QtGui.QStandardItemModel()
            headers_name = ["شناسه نمونه‌گیری", "المان", "طبقه", "تراز", "تاریخ نمونه‌گیری", "مقاومت مشخصه", "نوع سیمان"]
            self.model.setHorizontalHeaderLabels(headers_name)
            self.ui.tableView.setModel(self.model)
            font = QtGui.QFont()
            font.setFamily("B Titr")
            font.setPointSize(9)
            self.ui.tableView.horizontalHeader().setFont(font)
            self.ui.tableView.resizeColumnsToContents()
            header = self.ui.tableView.horizontalHeader()       
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)   
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)    
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
            for row, sampling in enumerate(cur):
                for col, data in enumerate(sampling):
                    item = QtGui.QStandardItem(str(data))
                    self.model.setItem(row ,col, item)

        except sqlite3.OperationalError as err:
            print(err)
        finally:
            conn.close()

    def ConnectAddSampling(self):
        self.d = ASDC.Form_DialogAddSamplingDetails()
        self.d.setProjectID(self.project_id)
        self.d.exec_()
        self.statusmode = self.d.statusmode
        self.DB_Connect()

    def ConnectDelSampling(self):
        try:
            sampling_row = self.ui.tableView.selectionModel().selectedIndexes()
            sampling_id = sampling_row[0].data()
            self.d = DSWC.Form_DialogDeleteSampling()
            self.d.setSamplingID(sampling_id)
            self.d.exec_()
            self.DB_Connect()
            self.Disable()
        except IndexError:
            print("No Sampling Selected for Deleting.")
        finally:
            self.ui.tableView.clearSelection()

    def ConnectEditSampling(self):
        try:
            sampling_row = self.ui.tableView.selectionModel().selectedIndexes()
            sampling_id = sampling_row[0].data()
            element = sampling_row[1].data()
            story = sampling_row[2].data()
            level = sampling_row[3].data()
            sampling_date = sampling_row[4].data().split("/")
            fc = sampling_row[5].data()
            cement_type = sampling_row[6].data()
            self.d = ESDC.Form_DialogEditSamplingDetails(sampling_id, element, story, level, sampling_date[0],
                                                         sampling_date[1], sampling_date[2], fc, cement_type)
            self.d.exec_()
            self.DB_Connect()
            self.Disable()
        except IndexError:
            print("No Sampling Selected for Deleting.")
        finally:
            self.ui.tableView.clearSelection()

    def ConnectSpecimen(self):
        try:
            sampling_row = self.ui.tableView.selectionModel().selectedIndexes()
            sampling_id = sampling_row[0].data()
            sampling_date = sampling_row[4].data()
            fc = sampling_row[5].data()
            cement_type = sampling_row[6].data()
            self.d = SpWC.Form_DialogSpecimenWindow()
            self.d.setSamplingID(sampling_id)
            self.d.setSamplingDate(sampling_date)
            self.d.setFprimC(fc)
            self.d.setCementType(cement_type)
            self.d.DB_Connect()
            self.d.exec_()
            
        except IndexError:
            print("No Sampling Selected of Showing Specimens.")
        finally:
            self.ui.tableView.clearSelection()
            self.Disable()


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     w = From_DialogSamplingWindow()
#     w.show()
#     sys.exit(w.exec_())
