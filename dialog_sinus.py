import sys
import os
from fonksiyon import Hesaplama
from PyQt5.QtWidgets import QApplication,QDialog,QTableWidgetItem,QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

class Dialog_Sinus(QDialog):
    def __init__(self, parent=None):
        super(Dialog_Sinus, self).__init__(parent)
        ## veritabanı ve arayüz dosyaları çağırılıyor
        self.pencere = uic.loadUi(os.getcwd()+r"\pencere_sinus.ui")
        self.fn = Hesaplama()
        self.pencere.bt_ciz.clicked.connect(self.Ciz)
        self.pencere.bt_cikis.clicked.connect(self.Cikis)
        self.pencere.bt_sifirla.clicked.connect(self.InitUI)


    def InitUI(self):
        self.pencere.txt_scl_min.setText("")
        self.pencere.txt_scl_max.setText("")
        self.pencere.txt_amp.setText("")
        self.pencere.txt_freq.setText("")
        self.pencere.txt_fs.setText("")

    def Ciz(self) :
        scl_min =  int(self.pencere.txt_scl_min.text())
        scl_max =  int(self.pencere.txt_scl_max.text())
        amp =  int(self.pencere.txt_amp.text())
        freq =  int(self.pencere.txt_freq.text())
        Fs =  int(self.pencere.txt_fs.text())
        self.fn.Sinus(scl_min,scl_max,Fs,amp,freq)

    def Cikis(self) :
        self.InitUI()
        self.pencere.close()