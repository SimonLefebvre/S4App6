import numpy as np
import matplotlib.pyplot as plt
from scipy import signal



def MyFilter(N, fe, fc, name, printName, printOption):

    fir_h: np.ndarray = signal.firwin(numtaps=N, cutoff=fc, pass_zero=name, window="blackman", fs=fe)
    fir_h_dft_tf: np.ndarray = np.abs(np.fft.fft(fir_h))

    if(printOption > 2):
        plt.figure('N = 256' + printName)
        plt.subplot(2,1,1)
        plt.plot(fir_h)
        plt.subplot(2,1,2)
        plt.plot(fir_h_dft_tf)
    if (printOption > 1):
        plt.figure('Normalized impultion repsonse' + printName)
        plt.subplot(2,1,1)
        nn = np.arange(-N/2,N/2,1)
        plt.plot(nn,fir_h)
        plt.subplot(2,1,2)
        nTime = np.arange((-N/2) * (1/fe),(N/2)*(1/fe),(1/fe))
        plt.plot(nTime,fir_h)
    if (printOption > 0):
        plt.figure('Normalized FREQ' + printName)
        plt.subplot(2,1,1)
        nn = np.arange(-N/2,N/2,1)
        fir_H = np.append(fir_h_dft_tf[int(N/2)::],fir_h_dft_tf[0:int(N/2)])
        plt.plot(nn,fir_H)
        plt.subplot(2,1,2)
        nHz = np.arange(-fe/2,fe/2,fe/N)
        plt.plot(nHz,fir_H)
