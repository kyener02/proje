import sys
import os
from fonksiyon import Hesaplama
from PyQt5.QtWidgets import QApplication,QDialog,QTableWidgetItem,QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

class Dialog_Iki(QDialog):
    def __init__(self, parent=None):
        super(Dialog_Iki, self).__init__(parent)
        ## veritabanı ve arayüz dosyaları çağırılıyor
        self.pencere = uic.loadUi(os.getcwd()+r"\pencere_derece2.ui")
        self.fn = Hesaplama()
        self.pencere.bt_ciz.clicked.connect(self.Ciz)
        self.pencere.bt_cikis.clicked.connect(self.Cikis)
        self.pencere.bt_sifirla.clicked.connect(self.InitUI)


    def InitUI(self):
        self.pencere.txt_scl_min.setText("")
        self.pencere.txt_scl_max.setText("")
        self.pencere.txt_coef_a.setText("")
        self.pencere.txt_coef_b.setText("")
        self.pencere.txt_coef_c.setText("")

    def Ciz(self) :
        try :
            scl_min =  float(self.pencere.txt_scl_min.text())
            scl_max =  float(self.pencere.txt_scl_max.text())
            coef_a =  float(self.pencere.txt_coef_a.text())
            coef_b =  float(self.pencere.txt_coef_b.text())
            coef_c =  float(self.pencere.txt_coef_c.text())
            self.fn.Ikinci_Derece(scl_min,scl_max,coef_a,coef_b,coef_c)
        except :
            QMessageBox.warning(self,"Hata","Geçerli Bir Değer Girin.",QMessageBox.Ok)

    def Cikis(self) :
        self.InitUI()
        self.pencere.close()