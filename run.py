import sys
import os
from fonksiyon import Hesaplama
from PyQt5.QtWidgets import QApplication,QMainWindow,QTableWidgetItem,QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic
from dialog_bir import Dialog_Bir
from dialog_iki import Dialog_Iki
from dialog_sinus import Dialog_Sinus


class Ana(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()
        ## veritabanı ve arayüz dosyaları çağırılıyor
        self.win = uic.loadUi(os.getcwd()+r"\design.ui")
        self.fn = Hesaplama()
        ## Arayüzdeki nesneler veritabanından dolduruluyor
        self.InitUI()
        ## Arayüzdeki Nesnelere Fonksiyonlar Atanıyor
        self.win.bt_cikis.clicked.connect(self.win.close)
        self.win.bt_sec.clicked.connect(self.Pencere_Ac)
        self.win.bt_yeni.clicked.connect(self.InitUI)
        self.win.action_cikis.triggered.connect(self.win.close)
        #Menü ile ilişkilendirme
        self.git_bir = Dialog_Bir(self)
        self.git_iki = Dialog_Iki(self)
        self.git_sinus = Dialog_Sinus(self)
        ## Ekranda Gösterim için
        self.win.show()


    def InitUI(self):
        self.win.sec_dnk_tip.clear()
        self.win.sec_dnk_tip.addItem("Seçiniz",-1)
        for a in self.fn.Tip_Listele():
            self.win.sec_dnk_tip.addItem(a)
        
    def Pencere_Ac(self) :
        secim = self.win.sec_dnk_tip.currentText()
        if secim == "Birinci Dereceden Denklem" :
            self.git_bir.pencere.show()
        elif secim == "İkinci Dereceden Denklem" :
            self.git_iki.pencere.show()
        elif secim == "Sinüs Dalga" :
            self.git_sinus.pencere.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ana()
    sys.exit(app.exec_())