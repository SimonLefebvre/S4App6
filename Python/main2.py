import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile as wave
from scipy import signal




#N1 = 255 #impaire pour passe bande
N = 256
fe = 20000
fc = 500


fir_h: np.ndarray = signal.firwin(numtaps=N, cutoff=fc, pass_zero="lowpass", window="blackman", fs=fe)
fir_h_dft_tf: np.ndarray = np.abs(np.fft.fft(fir_h))

plt.figure('N = 256')
plt.subplot(2,1,1)
plt.plot(fir_h)

plt.subplot(2,1,2)
plt.plot(fir_h_dft_tf)


plt.figure('Normalized impultion repsonse')
plt.subplot(2,1,1)
nn = np.arange(-N/2,N/2,1)
plt.plot(nn,fir_h)
plt.subplot(2,1,2)
nTime = np.arange((-N/2) * (1/fe),(N/2)*(1/fe),(1/fe))
plt.plot(nTime,fir_h)


plt.figure('Normalized FREQ')
plt.subplot(2,1,1)
nn = np.arange(-N/2,N/2,1)
fir_H = np.append(fir_h_dft_tf[int(N/2)::],fir_h_dft_tf[0:int(N/2)])
plt.plot(nn,fir_H)
plt.subplot(2,1,2)
nHz = np.arange(-fe/2,fe/2,fe/N)
plt.plot(nHz,fir_H)
plt.show()