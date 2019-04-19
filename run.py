import sys
import os
from fonksiyon import Hesaplama
from PyQt5.QtWidgets import QApplication,QMainWindow,QTableWidgetItem,QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic
from dialog import Dialog


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
        #Menü ile ilişkilendirme
        self.dialog = Dialog(self) 
        ## Ekranda Gösterim için
        self.win.show()


    def InitUI(self):
        self.win.sec_dnk_tip.clear()
        self.win.sec_dnk_tip.addItem("Seçiniz",-1)
        for a in self.fn.Tip_Listele():
            self.win.sec_dnk_tip.addItem(a)
        
    def Pencere_Ac(self) :
        self.dialog.pencere.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ana()
    sys.exit(app.exec_())