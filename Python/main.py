import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import FilterFunction as ff

fe = 20000
H_LP = ff.MyFIRFilter(255, fe, 500, "lowpass", "LowPass", 0)
H_BP1 = ff.MyFIRFilter(255, fe, [500, 1500], "bandpass", "BandPass#1", 0)
H_BP2 = ff.MyFIRFilter(255, fe, [1500, 2500], "bandpass", "BandPass#2", 0)
H_BP3 = ff.MyFIRFilter(255, fe, [2500, 4500], "bandpass", "BandPass#3", 0)
H_HP = ff.MyFIRFilter(255, fe, 4490, "highpass", "highpass", 0)
ff.MyIIRFilter(N=4, PB_Gain=1, SB_Gain=70, wn=[950, 1050], fe=20000, Type="bandstop", printName="bandstop", printOption=0)


n256 = np.arange(-fe/2,fe/2,fe/256)
n255 = np.arange(-fe/2,fe/2,fe/255)
plt.figure("Spectre des Filtres FIR")
plt.title("Spectre des Filtres FIR")
plt.semilogx(n255,20 * np.log10(H_LP),label="Low-Pass 500Hz")
plt.semilogx(n255,20 * np.log10(H_BP1),label="Band-Pass 500-1500Hz")
plt.semilogx(n255,20 * np.log10(H_BP2),label="Band-Pass 1500-2500Hz")
plt.semilogx(n255,20 * np.log10(H_BP3),label="Band-Pass 2500-4500Hz")
plt.semilogx(n255,20 * np.log10(H_HP),label="High-Pass 4490Hz")
plt.legend()
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Gain (dB)")
plt.grid(which='both')

plt.figure("Spectre des Filtres FIR2")
plt.title("Spectre des Filtres FIR2")
H_total = H_LP + H_BP1 + H_BP2 + H_BP3 + H_HP
plt.semilogx(n255,20 * np.log10(H_total),label="H_LP + H_BP1 + H_BP2 + H_BP3 + H_HP")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Gain (dB)")
plt.grid(which='both')
plt.legend()
plt.show()