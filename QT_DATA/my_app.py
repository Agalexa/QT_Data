
from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget, plot
import pandas as pd 
import pyqtgraph as pg
import sys 
import os


confirm_df = pd.read_csv("COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-confirmed.csv")
country_df = pd.read_csv('info/info.csv')

ja_df = confirm_df [ confirm_df['Country/Region'] == "Japan"]
ch_df = confirm_df [ confirm_df['Country/Region'] == "China"]
us_df = confirm_df [ confirm_df['Country/Region'] == "US"]
it_df = confirm_df [ confirm_df['Country/Region'] == "Italy"]
sp_df = confirm_df [ confirm_df['Country/Region'] == "Spain"]
uk_df = confirm_df [ confirm_df['Country/Region'] == "United Kingdom"]
th_df = confirm_df [ confirm_df['Country/Region'] == "Thailand"]
ge_df = confirm_df [ confirm_df['Country/Region'] == "Germany"]
sk_df = confirm_df [ confirm_df['Country/Region'] == "Korea"]

y = len(confirm_df.columns)- 1
dates = confirm_df.columns[4:y]

ja_ff = ja_df[ja_df.columns[4:y]]
ch_ff = ch_df[ch_df.columns[4:y]]
us_ff = us_df[us_df.columns[4:y]]
it_ff = it_df[it_df.columns[4:y]]
sp_ff = sp_df[sp_df.columns[4:y]]
uk_ff = uk_df[uk_df.columns[4:y]]
th_ff = th_df[th_df.columns[4:y]]
ge_ff = ge_df[ge_df.columns[4:y]]
sk_ff = sk_df[ge_df.columns[4:y]]


ja_list = []
ch_list = []
us_list = []
it_list = []
sp_list = []
uk_list = []
th_list = []
ge_list = []
sk_list = []

for x in ja_ff:
    ja_list.append(ja_df[x].sum())
    
for x in ch_ff:
    ch_list.append(ch_df[x].sum())
    
for x in us_ff:
    us_list.append(us_df[x].sum())

for x in it_ff:
    it_list.append(it_df[x].sum())
    
for x in sp_ff:
    sp_list.append(sp_df[x].sum())
    
for x in uk_ff:
    uk_list.append(uk_df[x].sum())
    
for x in th_ff:
    th_list.append(th_df[x].sum())
    
for x in ge_ff:
    ge_list.append(ge_df[x].sum())
    
for x in sk_ff:
    sk_list.append(sk_df[x].sum())

days = []
for x in range(1,62):
    days.append(x)



class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        uic.loadUi('mainwindow.ui', self)

        self.comboY.addItem("China")
        self.comboY.addItem("US")
        self.comboY.addItem("Italy")
        self.comboY.addItem("Korea")

        self.comboX.addItem("China")
        self.comboX.addItem("US")
        self.comboX.addItem("Italy")
        self.comboX.addItem("Korea")

        self.submit.clicked.connect(self.pressed)

    def plot1(self, tot_days, tot_infected):
        self.Graphwidget.plot(tot_days, tot_infected)
    
    def plot2(self, tot_days, tot_infected):
        self.Graphwidget2.plot(tot_days, tot_infected)    

    def pressed(self):
        firstgra = self.comboX.currentText()
        secgra = self.comboY.currentText()

        if (firstgra == "US"):
            self.plot1(days,us_list)
        elif(firstgra == "Italy"):
            self.plot1(days,it_list)  
        elif(firstgra == "China"):
            self.plot1(days,ch_list)  
        elif(firstgra == "Korea"):
            self.plot1(days,sk_list)
        else:
            pass  

        if (secgra == "US"):
            self.plot2(days,us_list)
        elif(secgra == "Italy"):
            self.plot2(days,it_list)  
        elif(secgra == "China"):
            self.plot2(days,ch_list)  
        elif(secgra == "Korea"):
            self.plot2(days,sk_list)
        else:
            pass          








def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
    
  


main()
