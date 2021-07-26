import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import FilterFunction as ff

fe = 20000
H_LP = ff.MyFIRFilter(256, fe, 500, "lowpass", "LowPass", 0)
H_BP1 = ff.MyFIRFilter(255, fe, [500, 1500], "bandpass", "BandPass#1", 0)
H_BP2 = ff.MyFIRFilter(255, fe, [1500, 2500], "bandpass", "BandPass#2", 0)
H_BP3 = ff.MyFIRFilter(255, fe, [2500, 4500], "bandpass", "BandPass#3", 0)
H_HP = ff.MyFIRFilter(255, fe, 4490, "highpass", "highpass", 0)
ff.MyIIRFilter(N=4, PB_Gain=1, SB_Gain=70, wn=[950, 1050], fe=20000, Type="bandstop", printName="bandstop", printOption=0)

# FIR filters .h COEFICIENTS
with open("FIR.h", "w") as fd:
    fd.write(f"int32c H_LP[{len(H_LP)}] = {{\n")
    for c in H_LP:
        real = np.round(np.power(2, 13) * float(c.real))
        imag = np.round(np.power(2, 13) * float(c.imag))
        fd.write(f"{{{int(real)},{int(imag)}}},\n")
    fd.write("};\n")
    fd.write(f"int32c H_BP1[{len(H_BP1)}] = {{\n")
    for c in H_BP1:
        real = np.round(np.power(2, 13) * float(c.real))
        imag = np.round(np.power(2, 13) * float(c.imag))
        fd.write(f"{{{int(real)},{int(imag)}}},\n")
    fd.write("};\n")
    fd.write(f"int32c H_BP2[{len(H_BP2)}] = {{\n")
    for c in H_BP2:
        real = np.round(np.power(2, 13) * float(c.real))
        imag = np.round(np.power(2, 13) * float(c.imag))
        fd.write(f"{{{int(real)},{int(imag)}}},\n")
    fd.write("};\n")
    fd.write(f"int32c H_BP3[{len(H_BP3)}] = {{\n")
    for c in H_BP3:
        real = np.round(np.power(2, 13) * float(c.real))
        imag = np.round(np.power(2, 13) * float(c.imag))
        fd.write(f"{{{int(real)},{int(imag)}}},\n")
    fd.write("};\n")
    fd.write(f"int32c H_HP[{len(H_HP)}] = {{\n")
    for c in H_HP:
        real = np.round(np.power(2, 13) * float(c.real))
        imag = np.round(np.power(2, 13) * float(c.imag))
        fd.write(f"{{{int(real)},{int(imag)}}},\n")
    fd.write("};\n")
#   END OF WRTITING IN FILE FIR.h

n1024 = np.arange(-fe/2,fe/2,fe/1024)
plt.figure("Spectre des Filtres FIR")
plt.title("Spectre des Filtres FIR")

H_LP = np.append(H_LP[512::], H_LP[0:512])
H_BP1 = np.append(H_BP1[512::], H_BP1[0:512])
H_BP2 = np.append(H_BP2[512::], H_BP2[0:512])
H_BP3 = np.append(H_BP3[512::], H_BP3[0:512])
H_HP = np.append(H_HP[512::], H_HP[0:512])

plt.semilogx(n1024,20 * np.log10(H_LP),label="Low-Pass 500Hz")
plt.semilogx(n1024,20 * np.log10(H_BP1),label="Band-Pass 500-1500Hz")
plt.semilogx(n1024,20 * np.log10(H_BP2),label="Band-Pass 1500-2500Hz")
plt.semilogx(n1024,20 * np.log10(H_BP3),label="Band-Pass 2500-4500Hz")
plt.semilogx(n1024,20 * np.log10(H_HP),label="High-Pass 4490Hz")
plt.legend()
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Gain (dB)")
plt.grid(which='both')

plt.figure("Spectre des Filtres FIR2")
plt.title("Spectre des Filtres FIR2")
H_total = H_LP + H_BP1 + H_BP2 + H_BP3 + H_HP
plt.semilogx(n1024,20 * np.log10(H_total),label="H_LP + H_BP1 + H_BP2 + H_BP3 + H_HP")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Gain (dB)")
plt.grid(which='both')
plt.legend()

#hanning file

x = np.hanning(1024)
x = np.round(x * np.power(2, 13))
plt.figure("hanning")
plt.plot(x)



with open("hanning.h", "w") as fd:
    fd.write(f"int32c window[{1024}] = {{\n")
    for c in x:
        fd.write(f"{int(c)},\n")
    fd.write("};\n")

plt.show()