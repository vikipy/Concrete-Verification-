import jdatetime, math

class Projects:
    ProjectCount = 0
    def __init__(self):
        Projects.ProjectCount += 1
    def __del__(self):
        Projects.ProjectCount -= 1
    def initial_Data(self):
        self.ProjectID = None
        self.ProjectName = None
        self.Client = None
        self.Supervisor = None
        self.Address = None

class Sampling(Projects):
    SamplingCount = 0
    def __init__(self):
        Sampling.SamplingCount += 1
        super().__init__()
    def __del__(self):
        Sampling.SamplingCount -= 1
    def Set_SamplingID(self, SamplingID): # Input Data
        self.SamplingID = int(SamplingID)
        return self.SamplingID
    def Set_fc(self, fc): # Input Data
        self.fc = fc #in kg/cm2
    def Set_CementType(self, CementType): # Input Data
        self.CementType = CementType
        return self.CementType 
    def Set_Location(self, Story, Level):
        self.Story = Story
        self.Level = Level
    def Set_SamplingDate(self, yr, mo, dy): # Input Data
        self.SamplingDate = jdatetime.datetime(yr, mo, dy, locale='fa_IR')
        return self.SamplingDate
    

class Specimen(Sampling):
    SpecimenCount = 0
    def __init__(self):
        Specimen.SpecimenCount += 1
        super().__init__()
    def __del__(self):
        Specimen.SpecimenCount -= 1
    def Set_ManualSpecimenID(self, ManualSpecimenID): # Input Data
        self.ManualSpecimenID = ManualSpecimenID
        return self.ManualSpecimenID
    def Set_MoldShape(self, MoldShape): # Input Data
        self.MoldShape = MoldShape
        return self.MoldShape
    def Set_Dimension(self, Dimension): # Input Data
        self.Dimension = int(Dimension)    #in cm
        return self.Dimension
    def Set_Wieght(self, Wieght): # Input Data
        self.Wieght = float(Wieght) #in Kg
        return self.Wieght
    def Set_TestDate(self, yr, mo, dy): # Input Data
        self.TestDate = jdatetime.datetime(yr, mo, dy, locale='fa_IR')
        return self.TestDate
    def Set_UltimatForce(self,UltimateForce): # Input Data
        self.UltimateForce = float(UltimateForce) #in Kgf
        return self.UltimateForce
    def Set_Area(self): # Output Data
        if self.MoldShape == "Cubic":
            self.Area = round(self.Dimension ** 2, 2) #in cm2
        elif self.MoldShape == "Cylindrical":
            self.Area = round(0.25 * math.pi * self.Dimension ** 2, 2) #in cm2
        return self.Area
    def Set_Volume(self): # Output Data
        if self.MoldShape == "Cubic":
            self.Volume = round(self.Dimension ** 3, 2) #in cm3
        elif self.MoldShape == "Cylindrical":
            self.Volume = round(0.5 * math.pi * self.Dimension ** 3, 2) #in cm3
        return self.Volume
    def Set_Gamma(self): # Output Data
        self.Gamma = round(1000000 * self.Wieght/self.Volume, 2) #in kg/m3
        return self.Gamma
    def Set_Age(self): # Output Data 
        self.Age = self.TestDate - self.SamplingDate #in day
        return self.Age.days

    def Set_CompressiveStrenght(self): #Output Data
        self.CompressiveStrenght = round(self.UltimateForce/self.Area) #in kgf/cm2
        return self.CompressiveStrenght
    
    def Set_Name(self): # Output Data
        if self.MoldShape == "Cylindrical":
            self.Name = 'fcy_' + str(self.Dimension) + 'x' + str(2*self.Dimension)
        elif self.MoldShape == "Cubic":
            self.Name = 'fcu_' + str(self.Dimension)
        return self.Name
    
    def Get_r1(self): # To convert cylindrical specimens to standard cylindrical specimens
        if self.Name == "fcy_10x20":
            self.r1 = 1.02
        elif self.Name == "fcy_15x30":
            self.r1 = 1
        elif self.Name == "fcy_20x40":
            self.r1 = 0.97
        elif self.Name == "fcy_25x50":
            self.r1 = 0.95
        elif self.Name == "fcy_30x60":
            self.r1 = 0.91
        else:
            self.r1 = 1
        return self.r1

    def Get_r2(self): # To convert cubic specimens to cubic specimen with sides 20
        if self.Name == "fcu_10":
            self.r2 = 1.05
        elif self.Name == "fcu_15":
            self.r2 = 1
        elif self.Name == "fcu_20":
            self.r2 = 1
        elif self.Name == "fcu_25":
            self.r2 = 0.95
        elif self.Name == "fcu_30":
            self.r2 = 0.9
        else:
            self.r2 = 1
        return self.r2

    def Get_r3(self): # to convert Cubic Specimen to standard cylindrical specimens
        cnd = self.CompressiveStrenght
        if cnd <= 250:
            self.r3 = 1.25
        elif 250 < cnd <= 300:
            self.r3 = -0.001*cnd+1.5
        elif 300 < cnd <= 350:
            self.r3 = -0.0006*cnd+1.38
        elif 350 < cnd <= 400:
            self.r3 = -0.0006*cnd+1.38
        elif 400 < cnd <= 450:
            self.r3 = -0.0002*cnd+1.22
        elif 450 < cnd <= 500:
            self.r3 = -0.0004*cnd+1.31
        else:
            self.r3 = -0.0002*cnd+1.21
        return round(self.r3, 2)

    def Cement_Conversion(self): 
        # d = int(str(self.Age)[:2])
        d = self.Age.days
        if self.CementType == "I":
            if (1 <= d < 7):
                self.r4 = 0.06*d+0.24
            elif (7<= d < 28):
                self.r4 = 0.0162*d+0.5467
            elif (28 <= d < 90):
                self.r4 = 0.0032*d+0.9097
            else:
                self.r4 = 1.2
        elif self.CementType == "II":
            if (1 <= d < 7):
                self.r4 = 0.055*d+0.175
            elif (7<= d < 28):
                self.r4 = 0.0162*d+0.4467
            elif (28 <= d < 90):
                self.r4 = 0.0048*d+0.7645
            else:
                self.r4 = 1.2
        elif self.CementType == "III":
            if (1 <= d < 7):
                self.r4 = 0.0367*d+0.5333
            elif (7<= d < 28):
                self.r4 = 0.0148*d+0.6867
            elif (28 <= d < 90):
                self.r4 = 0.0016*d+1.0548
            else:
                self.r4 = 1.2
        elif self.CementType == "IV":
            if (1 <= d < 7):
                self.r4 = 0.0433*d+0.1267
            elif (7<= d < 28):
                self.r4 = 0.0152*d+0.3233
            elif (28 <= d < 90):
                self.r4 = 0.0073*d+0.5468
            else:
                self.r4 = 1.2
        else:
            if (1 <= d < 7):
                self.r4 = 0.05*d+0.15
            elif (7<= d < 28):
                self.r4 = 0.0167*d+0.3833
            elif (28 <= d < 90):
                self.r4 = 0.0056*d+0.6919
            else:
                self.r4 = 1.2
        return round(self.r4, 2)
            
    def Convert2Standard(self): # Final Strengh Convertion
        if self.MoldShape == "Cylindrical":
            self.StadardCompressionStrenght = round((1/self.r1)*(1/self.r4)*self.CompressiveStrenght)
        else:
            self.StadardCompressionStrenght = round((1/self.r2)*(1/self.r3)*(1/self.r4)*self.CompressiveStrenght)
        return self.StadardCompressionStrenght
