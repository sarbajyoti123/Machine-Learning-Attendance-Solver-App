
                        # <==============================ATTANDANCE SOLVER MODEL================================================>
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip,QPushButton,QWidget,QLineEdit,QLabel
import sys
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "ATTENDANCE SOLVER"        
        self.top = 100        
        self.left = 100        
        self.width = 680        
        self.height = 500
        
        self.linedit=QLineEdit(self)
        self.linedit.move(150,80)
        self.linedit.resize(200,30)
        self.label1=QLabel("ENTER THE EXCEL PAGE NAME",self)
        self.label1.resize(220,30)
        self.label1.move(150,50)

        self.linedit1=QLineEdit(self) 
        self.linedit1.move(150,150)
        self.linedit1.resize(40,30)
        self.label1=QLabel("FROM",self)
        self.label1.resize(50,30)
        self.label1.move(100,150)
        
        self.label1=QLabel("TO",self)
        self.label1.resize(50,30)
        self.label1.move(210,150)
        self.linedit2=QLineEdit(self) 
        self.linedit2.move(250,150)
        self.linedit2.resize(40,30)

        self.label1=QLabel("TOTAL(COLUMN)",self)
        self.label1.resize(100,40)
        self.label1.move(340,145)
        self.linedit3=QLineEdit(self) 
        self.linedit3.move(450,150)
        self.linedit3.resize(40,30)

        self.linedit4=QLineEdit(self) 
        self.linedit4.move(150,250)
        self.linedit4.resize(40,30)
        self.label1=QLabel("MONTH",self)
        self.label1.resize(50,30)
        self.label1.move(100,250)

        self.label1=QLabel("TOTAL NO OF CLASS COMPLETED->",self)
        self.label1.resize(210,30)
        self.label1.move(230,250)
        self.linedit5=QLineEdit(self) 
        self.linedit5.move(450,250)
        self.linedit5.resize(50,30)

        self.linedit6=QLineEdit(self) 
        self.linedit6.move(250,330)
        self.linedit6.resize(40,30)
        self.label1=QLabel("YOUR SERIAL NO==>",self)
        self.label1.resize(150,30)
        self.label1.move(100,330)
        
        button = QPushButton("COMPUTE",self)
        button.move(100,400)
        button.setToolTip("Click To Check")
        button.clicked.connect(self.main)
        self.label2=QLabel(self)
        self.label2.resize(350,30)
        self.label2.move(250,400)


        self.InitWindow()

    def InitWindow(self):
        # self.label3=QLabel(self)
        # pix=QPixmap('game5.jpg')
        # self.label3.setPixmap(pix)
        # self.label3.setGeometry(100,100,680,500)
        self.setWindowIcon(QtGui.QIcon("iron.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
    def main(self):
        excel=self.linedit.text()
        from1=self.linedit1.text()
        from2=int(from1)
        to1=self.linedit2.text()
        to2=int(to1)
        colmn1=self.linedit3.text()
        colmn2=int(colmn1)
        month3=self.linedit4.text()
        month=int(month3)
        cl2=self.linedit5.text()
        cl=int(cl2)
        serial1=self.linedit6.text()
        serial=int(serial1)
             
        month1=month+1
        dataset = pd.read_excel(excel)
        x=dataset.iloc[:,from2:to2].values
        y=dataset.iloc[:,colmn2].values
        from sklearn.model_selection import train_test_split
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
        from sklearn.preprocessing import StandardScaler
        sc_x=StandardScaler()
        x_train=sc_x.fit_transform(x_train)
        x_test=sc_x.transform(x_test)

        from sklearn.decomposition import PCA
        pca=PCA(n_components=1)
        x_train=pca.fit_transform(x_train)
        x_test=pca.transform(x_test)
        explained_varience=pca.explained_variance_ratio_

        from sklearn.ensemble import RandomForestRegressor
        regressor=RandomForestRegressor(n_estimators=300,random_state=0)
        regressor.fit(x_train,y_train)

        # from sklearn.model_selection import cross_val_score
        # accuracies=cross_val_score(estimator=regressor,X=x_train,y=y_train,cv=10,n_jobs=-1)
        # accuracies.mean()
        # accuracies.std()

        # print(regressor.predict([[serial]]))
        serial1=regressor.predict([[serial]])
        ans=serial1
        c=98
        cal= ans * month1
        cal1= cl + c
        cal2=cal/cal1
        fans=cal2*100
      
        if fans<75.0:
            cal3=75.0-fans
            # print(cal3)
            self.label2.setText(f"Attendance {str(fans)}% and {str(cal3)}% needed")
        else:
            self.label2.setText(f"Attendance {str(fans)}%")
        sys.setrecursionlimit(100000)
        print(sys.getrecursionlimit())

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

