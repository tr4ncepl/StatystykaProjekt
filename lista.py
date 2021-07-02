# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os
from random import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
from matplotlib.backends.backend_template import FigureCanvas

from stats import *

module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, 'wypadki.csv')
wypadki = pd.read_csv(file_path, sep=';')
dolnoslaskie = wypadki[(wypadki.ID > 200000) & (wypadki.ID < 400000)]
dolnoslaskie = dolnoslaskie.reset_index(drop=True)
kujawsko = wypadki[(wypadki.ID > 400000) & (wypadki.ID < 600000)]
kujawsko = kujawsko.reset_index(drop=True)
lubelskie = wypadki[(wypadki.ID > 600000) & (wypadki.ID < 800000)]
lubelskie = lubelskie.reset_index(drop=True)
lubuskie = wypadki[(wypadki.ID > 800000) & (wypadki.ID < 1000000)]
lubuskie = lubuskie.reset_index(drop=True)
lodzkie = wypadki[(wypadki.ID > 1000000) & (wypadki.ID < 1200000)]
lodzkie = lodzkie.reset_index(drop=True)
malopolskie = wypadki[(wypadki.ID > 1200000) & (wypadki.ID < 1400000)]
malopolskie = malopolskie.reset_index(drop=True)
mazowieckie = wypadki[(wypadki.ID > 1400000) & (wypadki.ID < 1600000)]
mazowieckie = mazowieckie.reset_index(drop=True)
opolskie = wypadki[(wypadki.ID > 1600000) & (wypadki.ID < 1800000)]
opolskie = opolskie.reset_index(drop=True)
podkarpackie = wypadki[(wypadki.ID > 1800000) & (wypadki.ID < 2000000)]
podkarpackie = podkarpackie.reset_index(drop=True)
podlaskie = wypadki[(wypadki.ID > 2000000) & (wypadki.ID < 2200000)]
podlaskie = podlaskie.reset_index(drop=True)
pomorskie = wypadki[(wypadki.ID > 2200000) & (wypadki.ID < 2400000)]
pomorskie = pomorskie.reset_index(drop=True)
slaskie = wypadki[(wypadki.ID > 2400000) & (wypadki.ID < 2600000)]
slaskie = slaskie.reset_index(drop=True)
swietokrzyskie = wypadki[(wypadki.ID > 2600000) & (wypadki.ID < 2800000)]
swietokrzyskie = swietokrzyskie.reset_index(drop=True)
warmisko = wypadki[(wypadki.ID > 2800000) & (wypadki.ID < 3000000)]
warmisko = warmisko.reset_index(drop=True)
wielkopolskie = wypadki[(wypadki.ID > 3000000) & (wypadki.ID < 3200000)]
wielkopolskie = wielkopolskie.reset_index(drop=True)
zachodnio = wypadki[(wypadki.ID > 3200000) & (wypadki.ID < 3400000)]
zachodnio = zachodnio.reset_index(drop=True)


info1 = "dla całej Polski"
info2 = "wypadki w 2017 roku"




class PandasModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.values[index.row()][index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None



def about(item1):
    if(item1==0):
        nam = "wypadki w 2017"
        col = "w7"
    elif(item1==1):
        nam = "ranni w 2017"
        col = "r7"
    elif(item1==2):
        nam = "ofiary śmiertelne w 2017"
        col = "z7"
    elif(item1==3):
        nam = "wypadki w 2018"
        col = "w8"
    elif(item1==4):
        nam = "ranni w 2018"
        col = "r8"
    elif(item1==5):
        nam = "ofiary śmiertelne w 2018"
        col = "z8"
    return nam, col

def about2(type):
    if (type == 'Swietokrzyskie'):
        data = swietokrzyskie
        name = "woj. Świętokrzyskiego"
    elif (type == 'Polska'):
        data = wojewodztwa
        name = "całej Polski"
    elif (type == 'Lubelskie'):
        data = lubelskie
        name = "woj. Lubelskiego"
    elif (type == 'Lubuskie'):
        data = lubuskie
        name = "woj. Lubuskiego"
    elif (type == 'Wielkopolskie'):
        data = wielkopolskie
        name = "woj. Wielkopolskiego"
    elif (type == 'Mazowieckie'):
        data = mazowieckie
        name = "woj. Mazowieckiego"
    elif (type == 'Pomorskie'):
        data = pomorskie
        name = "woj. Pomorskiego"
    elif (type == 'Zachodniopomorskie'):
        data = zachodnio
        name = "woj. Zachodniopomorskiego"
    elif (type == 'Kujawskopomorskie'):
        data = kujawsko
        name = "woj. Kujawskopomorskiego"
    elif (type == 'Slaskie'):
        data = slaskie
        name = "woj. Śląskiego"
    elif (type == 'Dolnoslaskie'):
        data = dolnoslaskie
        name = "woj. Dolnośląskiego"
    elif (type == 'Lodzkie'):
        data = lodzkie
        name = "woj. Lódzkiego"
    elif (type == 'Opolskie'):
        data = opolskie
        name = "woj. Opolskiego"
    elif (type == 'Podkarpackie'):
        data = podkarpackie
        name = "woj. Podkarpackiego"
    elif (type[:9] == 'Warminsko'):
        data = warmisko
        name = "woj. Warmińsko-mazurskiego"
    elif (type == 'Podlaskie'):
        data = podlaskie
        name = "woj. Podlaskiego"
    elif (type == 'Malopolskie'):
        data = malopolskie
        name = "woj. Małopolskiego"
    return data, name


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lstStudents = QtWidgets.QListWidget(self.centralwidget)
        self.lstStudents.setGeometry(QtCore.QRect(560, 40, 121, 291))
        self.lstStudents.setObjectName("lstStudents")
        item = QtWidgets.QListWidgetItem()
        self.lstStudents.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstStudents.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstStudents.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstStudents.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstStudents.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstStudents.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstStudents.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstStudents.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstStudents.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstStudents.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstStudents.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstStudents.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstStudents.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstStudents.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstStudents.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstStudents.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstStudents.addItem(item)


        self.lstStudents.clicked.connect(self.pressed)

        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(760, 10, 591, 231))
        self.tableView.setObjectName("tableView")
        model = PandasModel(wojewodztwa)
        self.tableView.setModel(model)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 340, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 521, 421))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("maps/polska.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 470, 521, 241))
        self.plainTextEdit.setObjectName("plainTextEdit")
        summary = show_info(wojewodztwa,"r7", info1, info2)
        self.plainTextEdit.insertPlainText(summary)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(120, 440, 161, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 440, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.pressed)

        print(self.comboBox.currentText())

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(820, 250, 521, 421))
        self.label_3.setText("")
        multiple2017(wojewodztwa,"całej Polski")
        self.label_3.setPixmap(QtGui.QPixmap("wykresy\ogolne2017.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(680, 360, 111, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.buttonwyk = QtWidgets.QPushButton(self.centralwidget)
        self.buttonwyk.setGeometry(QtCore.QRect(700, 530, 75, 23))
        self.buttonwyk.setObjectName("buttonwyk")

        self.buttonwyk.clicked.connect(self.pressedWykres)

        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(680, 420, 111, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")

        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(680, 480, 111, 21))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(700, 333, 81, 20))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(710, 390, 51, 16))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(710, 450, 51, 16))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(580, 10, 141, 21))
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 420, 101, 61))
        self.label_8.setObjectName("label_8")



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 882, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.lstStudents.isSortingEnabled()
        self.lstStudents.setSortingEnabled(False)
        item = self.lstStudents.item(0)
        item.setText(_translate("MainWindow", "Polska"))
        item = self.lstStudents.item(1)
        item.setText(_translate("MainWindow", "Malopolskie"))
        item = self.lstStudents.item(2)
        item.setText(_translate("MainWindow", "Swietokrzyskie"))
        item = self.lstStudents.item(3)
        item.setText(_translate("MainWindow", "Lubelskie"))
        item = self.lstStudents.item(4)
        item.setText(_translate("MainWindow", "Lubuskie"))
        item = self.lstStudents.item(5)
        item.setText(_translate("MainWindow", "Wielkopolskie"))
        item = self.lstStudents.item(6)
        item.setText(_translate("MainWindow", "Mazowieckie"))
        item = self.lstStudents.item(7)
        item.setText(_translate("MainWindow", "Pomorskie"))
        item = self.lstStudents.item(8)
        item.setText(_translate("MainWindow", "Zachodniopomorskie"))
        item = self.lstStudents.item(9)
        item.setText(_translate("MainWindow", "Kujawskopomorskie"))
        item = self.lstStudents.item(10)
        item.setText(_translate("MainWindow", "Slaskie"))
        item = self.lstStudents.item(11)
        item.setText(_translate("MainWindow", "Dolnoslaskie"))
        item = self.lstStudents.item(12)
        item.setText(_translate("MainWindow", "Lodzkie"))
        item = self.lstStudents.item(13)
        item.setText(_translate("MainWindow", "Opolskie"))
        item = self.lstStudents.item(14)
        item.setText(_translate("MainWindow", "Podkarpackie"))
        item = self.lstStudents.item(15)
        item.setText(_translate("MainWindow", "Warminsko-mazurskie"))
        item = self.lstStudents.item(16)
        item.setText(_translate("MainWindow", "Podlaskie"))


        self.comboBox.setItemText(0, _translate("MainWindow", "Wypadki 2017"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Ranni 2017"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Ofiary smiertelne 2017"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Wypadki 2018"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Ranni 2018"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Ofiary smiertelne 2018"))
        self.pushButton.setText(_translate("MainWindow", "Pokaż"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Ogólne 2017"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Ogólne 2018"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Pudełkowy"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Regresja"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Histogram"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Korelacja 1"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Korelacja 2"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Statystyki"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "Pojedyńcze"))
        self.buttonwyk.setText(_translate("MainWindow", "Pokaż"))

        self.comboBox_3.setItemText(0, _translate("MainWindow", "Wypadki 2017"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Ranni 2017"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Ofiary smiertelne 2017"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Wypadki 2018"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Ranni 2018"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "Ofiary smiertelne 2018"))

        self.comboBox_4.setItemText(0, _translate("MainWindow", "Wypadki 2017"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Ranni 2017"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Ofiary smiertelne 2017"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Wypadki 2018"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "Ranni 2018"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "Ofiary smiertelne 2018"))

        self.label_4.setText(_translate("MainWindow", "Typ wykresu"))
        self.label_5.setText(_translate("MainWindow", "Zmienna x"))
        self.label_6.setText(_translate("MainWindow", "Zmienna y"))
        self.label_7.setText(_translate("MainWindow", "Kliknij aby wybrać "))
        self.label_8.setText(_translate("MainWindow", "Wybierz dane :"))

        self.lstStudents.setSortingEnabled(__sortingEnabled)

    def pressed(self):
        type = self.lstStudents.currentItem().text()
        type2 = self.comboBox.currentIndex()
        if(type == 'Swietokrzyskie'):
            info1="dla województwa Świetokrzyskiego"
            info2, colname = about(type2)
            summary = show_info(swietokrzyskie,colname, info1, info2)
            self.plainTextEdit.clear()
            self.plainTextEdit.insertPlainText(summary)
            newmodel = PandasModel(swietokrzyskie)
            self.tableView.setModel(newmodel)
            self.label_2.setPixmap(QtGui.QPixmap("maps/swiet.png"))
        elif(type=='Polska'):
            info1 = "dla całej Polski"
            info2 , colname = about(type2)
            summary = show_info(wojewodztwa,colname, info1, info2)
            self.plainTextEdit.clear()
            self.plainTextEdit.insertPlainText(summary)
            newmodel=PandasModel(wojewodztwa)
            self.tableView.setModel(newmodel)
            self.label_2.setPixmap(QtGui.QPixmap("maps/polska.png"))
        elif(type=='Lubelskie'):
            info1 = "dla województwa Lubelskiego"
            info2, colname = about(type2)
            summary = show_info(lubelskie,colname, info1, info2)
            self.plainTextEdit.clear()
            self.plainTextEdit.insertPlainText(summary)
            newmodel = PandasModel(lubelskie)
            self.tableView.setModel(newmodel)
            self.label_2.setPixmap(QtGui.QPixmap("maps/lubelskie.png"))
        elif (type == 'Lubuskie'):
            info1 = "dla województwa Lubuskiego"
            info2, colname = about(type2)
            summary = show_info(lubuskie,colname, info1, info2)
            self.plainTextEdit.clear()
            self.plainTextEdit.insertPlainText(summary)
            newmodel = PandasModel(lubuskie)
            self.tableView.setModel(newmodel)
            self.label_2.setPixmap(QtGui.QPixmap("maps/lubuskie.png"))
        elif (type == 'Wielkopolskie'):
            info1 = "dla województwa Wielkopolskiego"
            info2, colname = about(type2)
            summary = show_info(wielkopolskie,colname, info1, info2)
            self.plainTextEdit.clear()
            self.plainTextEdit.insertPlainText(summary)
            newmodel = PandasModel(wielkopolskie)
            self.tableView.setModel(newmodel)
            self.label_2.setPixmap(QtGui.QPixmap("maps/wielk.png"))
        elif (type == 'Mazowieckie'):
            info1 = "dla województwa Mazowieckiego"
            info2, colname = about(type2)
            summary = show_info(mazowieckie,colname, info1, info2)
            self.plainTextEdit.clear()
            self.plainTextEdit.insertPlainText(summary)
            newmodel = PandasModel(mazowieckie)
            self.tableView.setModel(newmodel)
            self.label_2.setPixmap(QtGui.QPixmap("maps/maz.png"))
        elif (type == 'Pomorskie'):
            info1 = "dla województwa Pomorskiego"
            info2, colname = about(type2)
            summary = show_info(pomorskie,colname, info1, info2)
            self.plainTextEdit.clear()
            self.plainTextEdit.insertPlainText(summary)
            newmodel = PandasModel(pomorskie)
            self.tableView.setModel(newmodel)
            self.label_2.setPixmap(QtGui.QPixmap("maps/pom.png"))
        elif (type == 'Zachodniopomorskie'):
            info1 = "dla województwa Zachodniopomorskiego"
            info2, colname = about(type2)
            summary = show_info(zachodnio,colname, info1, info2)
            self.plainTextEdit.clear()
            self.plainTextEdit.insertPlainText(summary)
            newmodel = PandasModel(zachodnio)
            self.tableView.setModel(newmodel)
            self.label_2.setPixmap(QtGui.QPixmap("maps/zach.png"))
        elif (type == 'Kujawskopomorskie'):
            info1 = "dla województwa Kujawskopomorskiego"
            info2, colname = about(type2)
            summary = show_info(kujawsko,colname, info1, info2)
            self.plainTextEdit.clear()
            self.plainTextEdit.insertPlainText(summary)
            newmodel = PandasModel(kujawsko)
            self.tableView.setModel(newmodel)
            self.label_2.setPixmap(QtGui.QPixmap("maps/kujaw.png"))
        elif (type == 'Slaskie'):
            info1 = "dla województwa Śląskiego"
            info2, colname = about(type2)
            summary = show_info(slaskie,colname, info1, info2)
            self.plainTextEdit.clear()
            self.plainTextEdit.insertPlainText(summary)
            newmodel = PandasModel(lubelskie)
            self.tableView.setModel(newmodel)
            self.label_2.setPixmap(QtGui.QPixmap("maps/slask.png"))
        elif (type == 'Dolnoslaskie'):
            info1 = "dla województwa Dolnośląskiego"
            info2, colname = about(type2)
            summary = show_info(dolnoslaskie,colname, info1, info2)
            self.plainTextEdit.clear()
            self.plainTextEdit.insertPlainText(summary)
            newmodel = PandasModel(dolnoslaskie)
            self.tableView.setModel(newmodel)
            self.label_2.setPixmap(QtGui.QPixmap("maps/dolno.png"))
        elif (type == 'Lodzkie'):
            info1 = "dla województwa Lodzkiego"
            info2, colname = about(type2)
            summary = show_info(lodzkie,colname, info1, info2)
            self.plainTextEdit.clear()
            self.plainTextEdit.insertPlainText(summary)
            newmodel = PandasModel(lodzkie)
            self.tableView.setModel(newmodel)
            self.label_2.setPixmap(QtGui.QPixmap("maps/lodzkie.png"))
        elif (type == 'Opolskie'):
            info1 = "dla województwa Opolskiego"
            info2, colname = about(type2)
            summary = show_info(opolskie,colname, info1, info2)
            self.plainTextEdit.clear()
            self.plainTextEdit.insertPlainText(summary)
            newmodel = PandasModel(opolskie)
            self.tableView.setModel(newmodel)
            self.label_2.setPixmap(QtGui.QPixmap("maps/opol.png"))
        elif (type == 'Podkarpackie'):
            info1 = "dla województwa Podkarpackiego"
            info2, colname = about(type2)
            summary = show_info(podkarpackie,colname, info1, info2)
            self.plainTextEdit.clear()
            self.plainTextEdit.insertPlainText(summary)
            newmodel = PandasModel(podkarpackie)
            self.tableView.setModel(newmodel)
            self.label_2.setPixmap(QtGui.QPixmap("maps/podkarp.png"))
        elif (type[:9] == 'Warminsko'):
            info1 = "dla województwa Warminsko-mazurskiego"
            info2, colname = about(type2)
            summary = show_info(warmisko,colname, info1, info2)
            self.plainTextEdit.clear()
            self.plainTextEdit.insertPlainText(summary)
            newmodel = PandasModel(warmisko)
            self.tableView.setModel(newmodel)
            self.label_2.setPixmap(QtGui.QPixmap("maps/warm.png"))
        elif (type == 'Podlaskie'):
            info1 = "dla województwa Podlaskiego"
            info2, colname = about(type2)
            summary = show_info(podlaskie,colname, info1, info2)
            self.plainTextEdit.clear()
            self.plainTextEdit.insertPlainText(summary)
            newmodel = PandasModel(podlaskie)
            self.tableView.setModel(newmodel)
            self.label_2.setPixmap(QtGui.QPixmap("maps/podl.png"))
        elif (type == 'Malopolskie'):
            info1 = "dla województwa Małopolskiego"
            info2, colname = about(type2)
            summary = show_info(malopolskie,colname, info1, info2)
            self.plainTextEdit.clear()
            self.plainTextEdit.insertPlainText(summary)
            newmodel = PandasModel(malopolskie)
            self.tableView.setModel(newmodel)
            self.label_2.setPixmap(QtGui.QPixmap("maps/malo.png"))

    def pressedWykres(self):
        type = self.lstStudents.currentItem().text()
        type2 = self.comboBox_2.currentIndex()
        type3 = self.comboBox_3.currentIndex()
        type4 = self.comboBox_4.currentIndex()


        if(type2==0):
            atr1, atr2 = about2(type)
            multiple2017(atr1, atr2)
            self.label_3.setPixmap(QtGui.QPixmap("wykresy\ogolne2017.png"))
        elif(type2==1):
            atr1, atr2 = about2(type)
            multiple2018(atr1,atr2)
            self.label_3.setPixmap(QtGui.QPixmap("wykresy\ogolne2018.png"))
        elif(type2==2):
            a1, a4 = about2(type)
            a3, a2 = about(type3)
            mb(a1, a2,a3,a4)
            self.label_3.setPixmap(QtGui.QPixmap("wykresy\mboxplot.png"))
        elif(type2==3):
            a1,a4 = about2(type)
            a5,a2 = about(type3)
            a6,a3 = about(type4)
            testregresion(a1,a2,a3,a4,a5,a6)
            self.label_3.setPixmap(QtGui.QPixmap("wykresy\mregresja.png"))
        elif(type2==4):
            a1,a3 = about2(type)
            a4,a2 = about(type3)
            mhitbox(a1,a2,a4,a3)
            self.label_3.setPixmap(QtGui.QPixmap("wykresy\mhistogram.png"))
        elif(type2==5):
            a1,a6=about2(type)
            a4,a2 = about(type3)
            a5,a3=about(type4)
            relationship(a1,a2,a3,a4,a5,a6)
            self.label_3.setPixmap(QtGui.QPixmap("wykresy\mrelacja1.jpg"))
        elif(type2==6):
            a1, a6 = about2(type)
            a4, a2 = about(type3)
            a5, a3 = about(type4)
            show_test(a1, a2, a3, a4, a5, a6)
            self.label_3.setPixmap(QtGui.QPixmap("wykresy\mrelacja2.jpg"))
        elif(type2==7):
            a1, a3=about2(type)
            a4, a2 = about(type3)
            stats_plot(a1, a2, a3, a4)
            self.label_3.setPixmap((QtGui.QPixmap("wykresy\mstats.jpg")))
        elif(type2==8):
            a1, a3 = about2(type)
            a4, a2 = about(type3)
            mplotbar(a1,a2,a3,a4)
            self.label_3.setPixmap((QtGui.QPixmap("wykresy\mbox.png")))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
