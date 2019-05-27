class Hesaplama :
    def Tip_Listele(self) :
        variable=[("Birinci Dereceden Denklem"),("İkinci Dereceden Denklem"),("Sinüs Dalga"),("Modulation")]
        return variable
    
    def Birinci_Derece(self,scl_min,scl_max,coef_m,coef_n) :
        import matplotlib.pyplot as plt 
        import numpy as np

        x = np.linspace(scl_min,scl_max,50)
        y = coef_m * x + coef_n
        plt.plot(x, y)
        plt.title('y = {}x + {}'.format(coef_m,coef_n))
        plt.legend(loc='upper left')
        plt.grid()
        plt.show()

    def Ikinci_Derece(self,scl_min,scl_max,coef_a,coef_b,coef_c) :
        import matplotlib.pyplot as plt 
        import numpy as np

        x = np.linspace(scl_min,scl_max,50)
        y = coef_a * x**2 + coef_b * x + coef_c
        plt.plot(x, y)
        plt.title('y = {}x^2 + {}x + {}'.format(coef_a,coef_b,coef_c))
        plt.legend(loc='upper left')
        plt.grid()
        plt.show()

    def Sinus(self,scl_min,scl_max,Fs,amp,freq) :
        import matplotlib.pyplot as plt 
        import numpy as np

        t = np.arange(scl_min,scl_max,1/Fs) 
        y = amp*np.sin(2 * np.pi * freq * t)
        plt.plot(t, y)
        plt.title('y = {}*(2*π*{}*t)'.format(amp,freq))
        # plt.legend(loc='upper left')
        plt.grid()
        plt.show()

    def Modulation(self,scl_min,scl_max,Fs,car_amp,car_freq,sig_amp,sig_freq,tip) :
        import matplotlib.pyplot as plot
        import numpy as np
        import sys
        from scipy import signal

        m = sig_amp / car_amp
        t = np.arange(scl_min,scl_max,1/Fs)

        if (tip == 'Frequency Modulation'):
            y= np.sin(2 * np.pi * car_freq * t + m*np.sin(2 * np.pi * sig_freq * t))
        elif (tip == 'Amplitude Modulation') :
	        y= (1+m*np.sin(2 * np.pi * sig_freq * t))* np.sin(2 * np.pi * car_freq * t)
        
        n = len(y) # length of the signal
        k = np.arange(n)
        T = n/Fs
        frq = k/T # two sides frequency range
        frq = frq[range(n//2)] # one side frequency range
        Y = np.fft.fft(y)/n # fft computing and normalization
        Y = Y[range(n//2)]

        fig,myplot = plot.subplots(2, 1)
        myplot[0].plot(t,y)
        myplot[0].set_xlabel('Time')
        myplot[0].set_ylabel('Amplitude')

        myplot[1].plot(frq,abs(Y)) # plotting the spectrum
        myplot[1].set_xlabel('Freq (Hz)')
        myplot[1].set_ylabel('|Y(freq)|')
        
        plot.show()

