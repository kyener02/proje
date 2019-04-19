class Hesaplama :
    def Birinci_Derece(self,scl_min,scl_max,coef_m,coef_n) :
        import matplotlib.pyplot as plt 
        import numpy as np

        x = np.linspace(scl_min,scl_max,50)
        y = coef_m * x + coef_n
        plt.plot(x, y)
        plt.title('y={}x+{}'.format(coef_m,coef_n))
        plt.legend(loc='upper left')
        plt.grid()
        plt.show()

    def Tip_Listele(self) :
        variable=[("Birinci Dereceden Denklem"),("İkinci Dereceden Denklem")]
        return variable




