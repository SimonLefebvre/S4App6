import numpy as np
from scipy.io import wavfile as wave
import matplotlib.pyplot as plt

#Main S4 App6       Simon Lefebvre & Gabriel Gaouette

#Filtres FIR 255 ou 256 coefficiens

#Passe-Bas à 500Hz
#Passe-Bande #1 1000 +-500
#Passe-Bande #2 2000 +- 500
#Passe-Bande #3 3500 +- 1000
#Passe-Haut #1 4490



#Passe-Haut

fc = 4490
fe = 20000
N = 254 #254 better than 255

print(fc/(fe/N))

n = np.arange(0,254,1)
H = np.zeros(57)
H = np.append(H,np.ones(N-(57*2)))
H = np.append(H,np.zeros(57))
print(len(H))


plt.figure('Passe Haut FREQ')
plt.subplot(2,1,1)
plt.plot(n,H)
plt.subplot(2,1,2)
SH = np.fft.fftshift(H)
Sn = np.arange(-fe/2,fe/2,fe/(N))
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
