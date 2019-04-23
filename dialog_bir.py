import sys
import os
from fonksiyon import Hesaplama
from PyQt5.QtWidgets import QApplication,QDialog,QTableWidgetItem,QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

class Dialog_Bir(QDialog):
    def __init__(self, parent=None):
        super(Dialog_Bir, self).__init__(parent)
        ## veritabanı ve arayüz dosyaları çağırılıyor
        self.pencere = uic.loadUi(os.getcwd()+r"\pencere_derece1.ui")
        self.fn = Hesaplama()
        self.pencere.bt_ciz.clicked.connect(self.Ciz)
        self.pencere.bt_cikis.clicked.connect(self.Cikis)
        self.pencere.bt_sifirla.clicked.connect(self.InitUI)


    def InitUI(self):
        self.pencere.txt_scl_min.setText("")
        self.pencere.txt_scl_max.setText("")
        self.pencere.txt_coef_m.setText("")
        self.pencere.txt_coef_n.setText("")

    def Ciz(self) :
        scl_min =  int(self.pencere.txt_scl_min.text())
        scl_max =  int(self.pencere.txt_scl_max.text())
        coef_m =  int(self.pencere.txt_coef_m.text())
        coef_n =  int(self.pencere.txt_coef_n.text())
        self.fn.Birinci_Derece(scl_min,scl_max,coef_m,coef_n)
    
    def Cikis(self) :
        self.InitUI()
        self.pencere.close()