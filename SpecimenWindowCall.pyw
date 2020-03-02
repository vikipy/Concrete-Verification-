import sys, sqlite3
from PyQt5 import QtWidgets, QtGui, QtCore
from SpecimenWindow import *
import AddSpecimenDetailsCall as ASpDC
import DeleteSpecimenWarningCall as DSpWC
import EditSpecimenDetailsCall as ESpDC

class Form_DialogSpecimenWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogSpecimenWindow()
        self.ui.setupUi(self)
        self.ui.tableViewInputSpecimen.clicked.connect(self.Enable)
        self.ui.tableViewInputSpecimen.clicked.connect(self.ShowOutput)
        self.ui.pushButtonAddSpecimen.clicked.connect(self.ConnectAddSpecimen)
        self.ui.pushButtonDelSpecimen.clicked.connect(self.ConnectDelSpecimen)
        self.ui.pushButtonEditSpecimen.clicked.connect(self.ConnectEditSpecimen)

    def Enable(self):
        self.ui.pushButtonEditSpecimen.setEnabled(True)
        self.ui.pushButtonDelSpecimen.setEnabled(True)

    def Disable(self):
        self.ui.pushButtonEditSpecimen.setEnabled(False)
        self.ui.pushButtonDelSpecimen.setEnabled(False)
        self.ui.labelArea.clear()
        self.ui.labelVolume.clear()
        self.ui.labelGama.clear()
        self.ui.labelAge.clear()
        self.ui.labelCompressiveStrenght.clear()
        self.ui.labelStadardCompressionStrenght.clear()

    def setSamplingID(self, sampling_id):
        self.sampling_id = sampling_id

    def setSamplingDate(self, sampling_date):
        self.sampling_date = sampling_date

    def setCementType(self, cement_type):
        self.cement_type = cement_type

    def setFprimC(self, fc):
        self.fc = fc

    def DB_Connect(self):
        try:
            conn = sqlite3.connect("MainDB.db")
            cur = conn.cursor()

            cur.execute("SELECT * FROM Sampling WHERE SamplingID=%s" %self.sampling_id)
            lst = list(cur)
            self.ui.labelSampingID.setText(str(lst[0][1]))
            self.ui.labelSampingDate.setText(str(lst[0][5]))
            self.ui.labelfc.setText(str(lst[0][6]))
            self.ui.labelCement_type.setText(str(lst[0][7]))
            fc = lst[0][6]
 
            cur.execute("SELECT AutoSpecimenID, ManualSpecimenID, MoldShape, Dimension, Wieght, TestDate, UltimatForce FROM Specimen WHERE SamplingID=%s" % self.sampling_id)
            self.model = QtGui.QStandardItemModel()
            headers_name = ["شناسه نمونه", "شماره نمونه", "شکل قالب", "اندازه", "وزن", "تاریخ تست", "نیروی نهایی"]
            self.model.setHorizontalHeaderLabels(headers_name)
            self.ui.tableViewInputSpecimen.setModel(self.model)
            font = QtGui.QFont()
            font.setFamily("B Titr")
            font.setPointSize(9)
            self.ui.tableViewInputSpecimen.horizontalHeader().setFont(font)
            self.ui.tableViewInputSpecimen.resizeColumnsToContents()
            header = self.ui.tableViewInputSpecimen.horizontalHeader()       
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)   
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)    
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
            for row, specimen in enumerate(cur):
                for col, data in enumerate(specimen):
                    if str(data)=="Cylindrical":
                        data = "استوانه‌ای"
                    if str(data)=="Cubic":
                        data = "مکعبی"
                    item = QtGui.QStandardItem(str(data))
                    self.model.setItem(row ,col, item)
            cur.execute("SELECT StadardCompressionStrenght FROM Specimen WHERE SamplingID=%s" % self.sampling_id)
            Xi = [i[0] for i in cur]
            if len(Xi) < 3:
                pass
            else:
                Xmin = min(Xi)
                Xm = round(sum(Xi)/len(Xi),2)
                if Xmin >= fc:
                    self.ui.labelSamplingStatus.setPixmap(QtGui.QPixmap(":/ImageIcons/Icons/SuccessIcon.png"))
                    self.ui.labelSamplingStatus.setScaledContents(True)
                    self.ui.labelMin.setText(str(Xmin))
                    self.ui.labelMean.setText(str(Xm))
                    self.ui.labelExplain.setText("گام اول بند (9-10-8-5): بتن قابل قبول است.")
                elif (Xm >= fc+15 and Xmin >= fc-40):
                    self.ui.labelSamplingStatus.setPixmap(QtGui.QPixmap(":/ImageIcons/Icons/SuccessIcon.png"))
                    self.ui.labelSamplingStatus.setScaledContents(True)
                    self.ui.labelMin.setText(str(Xmin))
                    self.ui.labelMean.setText(str(Xm))
                    self.ui.labelExplain.setText("گام دوم بند (9-10-8-5): بتن قابل قبول است.")
                elif (Xmin < fc-40 and Xm < fc):
                    self.ui.labelSamplingStatus.setPixmap(QtGui.QPixmap(":/ImageIcons/Icons/FailIcon.png"))
                    self.ui.labelSamplingStatus.setScaledContents(True)
                    self.ui.labelMin.setText(str(Xmin))
                    self.ui.labelMean.setText(str(Xm))
                    self.ui.labelExplain.setText("عدم پذیرش قطعی بتن.")
                else:
                    self.ui.labelSamplingStatus.setPixmap(QtGui.QPixmap(":/ImageIcons/Icons/Warning.png"))
                    self.ui.labelSamplingStatus.setScaledContents(True)
                    self.ui.labelMin.setText(str(Xmin))
                    self.ui.labelMean.setText(str(Xm))
                    self.ui.labelExplain.setText("گام سوم بند (9-10-8-5): بتن غیر قابل قبول است.")

 
        except sqlite3.OperationalError as err:
            print(err)
        finally:
            conn.close()
            self.Disable()

    def ConnectAddSpecimen(self):
        self.d = ASpDC.Form_DialogAddSpecimenDetails()
        self.d.setSamplingID(self.sampling_id)
        self.d.setSamplingData(self.sampling_date)
        self.d.setFprimC(self.fc)
        self.d.setCementType(self.cement_type)
        self.d.exec_()
        self.DB_Connect()

    def ConnectDelSpecimen(self):
        try:
            specimen_row = self.ui.tableViewInputSpecimen.selectionModel().selectedIndexes()
            specimen_id = specimen_row[0].data()
            self.d = DSpWC.Form_DialogDeleteSpecimen()
            self.d.setSpecimenID(specimen_id)
            self.d.exec_()
            self.DB_Connect()
            self.Disable()
        except IndexError:
            print("No Specimen Selected for Deleting.")
        finally:
            self.ui.tableViewInputSpecimen.clearSelection()

    def ConnectEditSpecimen(self):
        try:
            speciment_row = self.ui.tableViewInputSpecimen.selectionModel().selectedIndexes()
            auto_sepcimen_id = speciment_row[0].data()
            maual_specimen_id = speciment_row[1].data()
            mold_shape = speciment_row[2].data()
            dimension = speciment_row[3].data()
            wieght = speciment_row[4].data()
            test_date = speciment_row[5].data().split("/")
            ultimat_force = speciment_row[6].data()
            self.d = ESpDC.Form_DialogEditSpecimenDetails(auto_sepcimen_id, maual_specimen_id, mold_shape, dimension,
                                                    wieght, test_date[0], test_date[1], test_date[2], ultimat_force)
            self.d.setSamplingID(self.sampling_id)
            self.d.setSamplingData(self.sampling_date)
            self.d.setFprimC(self.fc)
            self.d.setCementType(self.cement_type)
            self.d.exec_()
            self.DB_Connect()
            self.Disable()
        except IndexError:
            print("No Speciment Selected for Edit.")
        finally:
            self.ui.tableViewInputSpecimen.clearSelection()

    def ShowOutput(self):
        specimen_row = self.ui.tableViewInputSpecimen.selectionModel().selectedIndexes()
        specimen_id = specimen_row[0].data()
        conn = sqlite3.connect("MainDB.db")
        cur = conn.cursor()
        cur.execute("SELECT Area, Volume, Gamma, Age, CompressiveStrenght, StadardCompressionStrenght FROM Specimen WHERE AutoSpecimenID=%s" % specimen_id)
        lst = list(cur)
        self.ui.labelArea.setText(str(lst[0][0]))
        self.ui.labelVolume.setText(str(lst[0][1]))
        self.ui.labelGama.setText(str(lst[0][2]))
        self.ui.labelAge.setText(str(lst[0][3]))
        self.ui.labelCompressiveStrenght.setText(str(lst[0][4]))
        self.ui.labelStadardCompressionStrenght.setText(str(lst[0][5]))



# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     w = Form_DialogSpecimenWindow()
#     w.show()
#     sys.exit(app.exec_())