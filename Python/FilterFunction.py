import numpy as np
import matplotlib.pyplot as plt
from scipy import signal



def MyFIRFilter(N, fe, fc, name, printName, printOption):

    fir_h: np.ndarray = signal.firwin(numtaps=N, cutoff=fc, pass_zero=name, window="blackman", fs=fe)
    fir_freq_fz, fir_h_dft_fz = signal.freqz(b=fir_h, a=1, worN=10000, fs=fe)
    fir_h_dft_tf: np.ndarray = np.abs(np.fft.fft(fir_h))
    fir_H = np.append(fir_h_dft_tf[int(N / 2)::], fir_h_dft_tf[0:int(N / 2)])

    if (printOption > 3):
        print("fir_freq_fz")
        print(fir_freq_fz)
        print("fir_h_dft_fz")
        print(fir_h_dft_fz)
        #print(fir_h_dft_tf)

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

        plt.plot(nn,20*np.log10(np.abs(fir_H)))
        plt.subplot(2,1,2)
        nHz = np.arange(-fe/2,fe/2,fe/N)
        plt.plot(nHz,20*np.log10(np.abs(fir_H)))
    return fir_H


def MyIIRFilter(N, PB_Gain, SB_Gain, wn, fe, Type, printName, printOption):

    [b, a] = signal.ellip(N=N, rp=PB_Gain, rs=SB_Gain, Wn=wn, fs=fe, btype=Type, output="ba")
    #[b, a] = signal.ellip(N=4, rp=1, rs=70, Wn=[950, 1050], fs=20000, btype="bandstop", output="ba")
    [w, h_dft] = signal.freqz(b, a, worN=10000, fs=fe)

    if (printOption>0):
        plt.figure()
        plt.plot(w, 20 * np.log10(np.abs(h_dft)))
        plt.title("IIRFilter " + printName)
        plt.xlabel("Fréquence [Hz]")
        plt.ylabel("Gain [dB]")
        plt.grid(which="both", axis="both")
        plt.tight_layout()

