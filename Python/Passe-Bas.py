import numpy as np
from scipy.io import wavfile as wave
import matplotlib.pyplot as plt


#Passe Bas idéal

fc = 500
fe = 20000
N = 255

n = np.arange(0,254,1)
H = np.ones(7)
H = np.append(H,np.zeros(241))
H = np.append(H,np.ones(6))
print(len(H))

plt.figure('Passe Bas FREQ')
plt.subplot(2,1,1)
plt.plot(n,H)
plt.subplot(2,1,2)
SH = np.fft.fftshift(H)
Sn = np.arange(-fe/2,fe/2,fe/(N-1))
plt.plot(Sn,SH)

plt.figure('Rep temporelle')
plt.subplot(2,1,1)
h = np.fft.ifft(H)
plt.plot(n,h)
plt.subplot(2,1,2)
sh = np.append(h[128::],h[0:128])
#ntime = np.arange(0,1/fe*N,1/fe)
#ntime = np.append(ntime[128::]*-1,ntime[0:127])
ntime = n - (len(n)/2)
ntime = ntime * (1/fe)
plt.plot(ntime,sh)
plt.show()
