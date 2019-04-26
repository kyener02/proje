import sys
import os
from fonksiyon import Hesaplama
from PyQt5.QtWidgets import QApplication,QDialog,QTableWidgetItem,QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

class Dialog_Mod(QDialog):
    def __init__(self, parent=None):
        super(Dialog_Mod, self).__init__(parent)
        ## veritabanı ve arayüz dosyaları çağırılıyor
        self.pencere = uic.loadUi(os.getcwd()+r"\pencere_mod.ui")
        self.fn = Hesaplama()
        self.pencere.bt_ciz.clicked.connect(self.Ciz)
        self.pencere.bt_sifirla.clicked.connect(self.InitUI)
        self.pencere.bt_cikis.clicked.connect(self.Cikis)

    def InitUI(self) :
        self.pencere.txt_scl_min.setText("")
        self.pencere.txt_scl_max.setText("")
        self.pencere.txt_fs.setText("")
        self.pencere.txt_car_amp.setText("")
        self.pencere.txt_car_freq.setText("")
        self.pencere.txt_sig_amp.setText("")
        self.pencere.txt_sig_freq.setText("")
        self.pencere.txt_mod_tip.setText("")

    def Ciz(self) :
        scl_min = int(self.pencere.txt_scl_min.text())
        scl_max = int(self.pencere.txt_scl_max.text())
        Fs = int(self.pencere.txt_fs.text())
        car_amp = float(self.pencere.txt_car_amp.text())
        car_freq = int(self.pencere.txt_car_freq.text())
        sig_amp = float(self.pencere.txt_sig_amp.text())
        sig_freq = int(self.pencere.txt_sig_freq.text())
        tip = self.pencere.txt_mod_tip.text()
        self.fn.Modulation(scl_min,scl_max,Fs,car_amp,car_freq,sig_amp,sig_freq,tip)

    def Cikis(self) :
        self.InitUI()
        self.pencere.close()