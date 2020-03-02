import sys, sqlite3
import os.path
from MainWindow import *
from PyQt5 import QtGui, QtCore
import AddProjectDetailsCall as APDC
import DeleteProjectWarningCall as DPWC
import EditProjectDetailsCall as EPDC
import SamplingWindowCall as SWC

class Form_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.statusbar.showMessage("نرم افزار آماده استفاده است", 10000)
        self.Check_DB_Exist()
        self.DB_Connect()
        self.ui.CreateNewProject.triggered.connect(self.ConnectAddProject)
        self.ui.Help.triggered.connect(self.HelpWebSite)
        self.ui.DeleteProject.triggered.connect(self.ConnectDeleteProject)
        self.ui.EditProject.triggered.connect(self.ConnectEditProject)
        self.ui.AddSampling.triggered.connect(self.ConnectSamplingWindow)
        self.ui.tableViewProjects.clicked.connect(self.Enable)

    def HelpWebSite(self):
        MyLink = QtCore.QUrl("https://meysampirouzi.ir/")
        QtGui.QDesktopServices.openUrl(MyLink)
        
    def Enable(self):
        self.ui.EditProject.setEnabled(True)
        self.ui.DeleteProject.setEnabled(True)
        self.ui.ProjectsList.setEnabled(True)
        self.ui.AddSampling.setEnabled(True)

    def Disable(self):
        self.ui.EditProject.setEnabled(False)
        self.ui.DeleteProject.setEnabled(False)
        # self.ui.ProjectsList.setEnabled(False)
        self.ui.AddSampling.setEnabled(False)

    def Check_DB_Exist(self):
        if os.path.isfile('MainDB.db'):
            print ("Database exist.")
        else:
            print ("Database not exist and will be create now.")
            conn = sqlite3.connect("MainDB.db")
            cur = conn.cursor()
            sqlexpr1 = """
            CREATE TABLE IF NOT EXISTS Projects (
                ProjectID      INTEGER PRIMARY KEY AUTOINCREMENT,
                ContractNumber TEXT,
                ProjectName    TEXT,
                Client         TEXT,
                Supervisor     TEXT,
                Laboratory     TEXT,
                Address        TEXT
            );
            """
            sqlexpr2 = """
            CREATE TABLE IF NOT EXISTS Sampling (
                ProjectID          INTEGER REFERENCES Projects (ProjectID) ON DELETE CASCADE
                                                                        ON UPDATE CASCADE,
                SamplingID         INTEGER PRIMARY KEY AUTOINCREMENT,
                Element            TEXT,
                Story              TEXT,
                Level              TEXT,
                SamplingDate       TEXT,
                fc                 REAL,
                CementType         TEXT,
                VerificationStatus TEXT
            );
            """
            sqlexpr3 = """
            CREATE TABLE IF NOT EXISTS Specimen (
                SamplingID                 INTEGER REFERENCES Sampling (SamplingID) ON DELETE CASCADE
                                                                                    ON UPDATE CASCADE,
                AutoSpecimenID             INTEGER PRIMARY KEY AUTOINCREMENT,
                ManualSpecimenID           INTEGER,
                MoldShape                  TEXT,
                Dimension                  INTEGER,
                Wieght                     REAL,
                TestDate                   TEXT,
                UltimatForce               REAL,
                Area                       REAL,
                Volume                     REAL,
                Gamma                      REAL,
                Age                        INTEGER,
                CompressiveStrenght        REAL,
                Name                       TEXT,
                r1                         REAL,
                r2                         REAL,
                r3                         REAL,
                r4                         REAL,
                StadardCompressionStrenght REAL
            );
            """
            cur.execute(sqlexpr1)
            cur.execute(sqlexpr2)
            cur.execute(sqlexpr3)
            conn.commit()
            conn.close()

    def DB_Connect(self):
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["شناسه پروژه","شماره قرارداد","نام پروژه","کارفرما","مشاور","آزمایشگاه","آدرس"])
        self.ui.tableViewProjects.setModel(self.model)
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(9)
        self.ui.tableViewProjects.horizontalHeader().setFont(font)
        header = self.ui.tableViewProjects.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        # self.ui.tableViewProjects.resizeColumnsToContents()
        # self.ui.tableViewProjects.setColumnHidden(0, True)
        # self.ui.tableViewProjects.setColumnHidden(1, True)
        # self.ui.tableViewProjects.setColumnHidden(3, True)
        # self.ui.tableViewProjects.setColumnHidden(4, True)
        # self.ui.tableViewProjects.setColumnHidden(5, True)
        # self.ui.tableViewProjects.setColumnHidden(6, True)
        conn = sqlite3.connect("MainDB.db")
        cur = conn.cursor()
        sqlexpr = "SELECT * FROM Projects"
        cur.execute(sqlexpr)
        for row, pro in enumerate(cur):
            for col, data in enumerate(pro):
                item = QtGui.QStandardItem(str(data))
                self.model.setItem(row ,col, item)
        conn.close()
        self.Disable()
       
    def ConnectAddProject(self):
        self.d = APDC.Form_DialogAddProjectDetails()
        self.d.exec_()
        self.DB_Connect()
        if self.d.statusmode == 1:
            self.statusBar().showMessage("پروژه جدید اضافه گردید", 5000)
        else:
            self.statusBar().showMessage("ایجاد پروژه جدید لغو گردید", 5000)

    def ConnectDeleteProject(self):
        try:
            project_row = self.ui.tableViewProjects.selectionModel().selectedIndexes()
            project_id = project_row[0].data()
            project_name = project_row[2].data()
            self.d = DPWC.Form_DialogDeleteProject(project_id, project_name)
            self.d.exec_()
            if self.d.statusmode == -1:
                self.statusBar().showMessage(("پروژه %s حذف گردید" % project_name), 10000)
            else:
                self.statusBar().showMessage(("حذف پروژه %s لغو گردید" % project_name), 10000)
            self.DB_Connect()
            self.Disable()
        except IndexError:
            self.statusBar().showMessage("هیچ پروژه‌ای جهت حذف انتخاب نشده است.", 10000)
            print("No projects have been selected to delete.")
        finally:
            self.ui.tableViewProjects.clearSelection()
            self.Disable()

    def ConnectEditProject(self):
        try:
            project_row = self.ui.tableViewProjects.selectionModel().selectedIndexes()
            project_id = project_row[0].data()
            project_contractNumber = project_row[1].data()
            project_name = project_row[2].data()
            project_client = project_row[3].data()
            project_supervisor = project_row[4].data()
            project_labratory = project_row[5].data()
            project_address = project_row[6].data()
            self.d = EPDC.Form_DialogEditProjectDetails(project_id, project_contractNumber, project_name,
                                    project_client, project_supervisor, project_labratory, project_address)
            self.d.exec_()
            if self.d.statusmode == 1:
                self.statusBar().showMessage(("پروژه %s ویرایش گردید" % project_name), 10000)
            else:
                self.statusBar().showMessage(("ویرایش پروژه %s لغو گردید" % project_name), 10000)
                self.DB_Connect()
                self.Disable()
        except IndexError:
            self.statusBar().showMessage("هیچ پروژه‌ای جهت ویرایش انتخاب نشده است.", 10000)
            print("No projects selected for editing.")
        finally:
            self.ui.tableViewProjects.clearSelection()
            self.Disable()

    def ConnectSamplingWindow(self):
        try:
            project_row = self.ui.tableViewProjects.selectionModel().selectedIndexes()
            project_id = project_row[0].data()
            project_name = project_row[2].data()
            self.d = SWC.From_DialogSamplingWindow()
            self.d.setProjectID(project_id)
            self.d.DB_Connect()
            self.d.exec_()
            if self.d.statusmode == 1:
                self.statusBar().showMessage(("یک نمونه‌گیری جدید به پروزه %s اضافه گردید" % project_name), 10000)
            else:
                pass
        except IndexError:
            self.statusBar().showMessage("هیچ پروژه‌ای جهت نشان دادن نمونه‌گیری‌ها انتخاب نشده است.", 10000)
            print("No projects selected to showing Sampling.")
        finally:
            self.ui.tableViewProjects.clearSelection()
            self.Disable()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Form_MainWindow()
    w.show()
    sys.exit(app.exec_())
