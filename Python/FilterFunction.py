import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def MyFIRFilter(N, fe, fc, name, printName, printOption):

    fir_h: np.ndarray = signal.firwin(numtaps=N, cutoff=fc, pass_zero=name, window="blackman", fs=fe)#blackman
    fir_freq_fz, fir_h_dft_fz = signal.freqz(b=fir_h, a=1,whole = True, worN=1024, fs=fe)
    fir_h_dft_tf: np.ndarray = np.abs(np.fft.fft(fir_h))
    fir_H = np.append(fir_h_dft_tf[int(N / 2)::], fir_h_dft_tf[0:int(N / 2)])

    if (printOption > 3):
        plt.figure('Freq_FZ' + printName)
        plt.plot(fir_freq_fz,np.abs(fir_h_dft_fz))
        print('len')
        print(len(fir_h_dft_fz))
        print(fir_h_dft_fz)
        with open(printName+"file.h", "w") as fd:
            fd.write(f"int32c H[{len(fir_h_dft_fz)}] = {{\n")
            for c in fir_h_dft_fz:
                real = np.round(np.power(2,13) * float(c.real))
                imag = np.round(np.power(2,13) * float(c.imag))
                fd.write(f"{{{int(real)},{int(imag)}}},\n")
            fd.write("};\n")

    if(printOption > 2):
        plt.figure('N = 25X' + printName)
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

    return fir_h_dft_fz


def MyIIRFilter(N, PB_Gain, SB_Gain, wn, fe, Type, printName, printOption):

    sos = signal.ellip(N=N, rp=PB_Gain, rs=SB_Gain, Wn=wn, fs=fe, btype=Type, output="sos")
    sos13 = np.trunc(sos * np.power(2,13)) / np.power(2,13)
    sos5 = np.trunc(sos * np.power(2, 5)) / np.power(2, 5)



    #[b, a] = signal.ellip(N=4, rp=1, rs=70, Wn=[950, 1050], fs=20000, btype="bandstop", output="ba")
    w, h_dft = signal.sosfreqz(sos, worN=10000, fs=fe)
    [w13, h_dft13] = signal.sosfreqz(sos13, worN=10000, fs=fe)
    [w5, h_dft5] = signal.sosfreqz(sos5, worN=10000, fs=fe)

    if (printOption > 1):
        sos13 = sos13 * np.power(2,13)
        print("b13")
        print(sos13)
        with open("IIRcoeffs", "w") as fd:
            fd.write(f"int32_t IIRCoeffs[N_SOS_SECTIONS][6] = {{\n")
            for cc in range(4):
                fd.write(f"{{ ")
                for c in range(6):
                    fd.write(f"{int(sos13[cc][c])}")
                    if c < 5:
                        fd.write(f", ")
                fd.write(f"}},\n")
            fd.write("};\n")


    if (printOption>0):
        plt.figure()
        plt.semilogx(w, 20 * np.log10(np.abs(h_dft)),label="Normal Floats")
        plt.semilogx(w13, 20 * np.log10(np.abs(h_dft13)), label="Q2.13")
        plt.semilogx(w5, 20 * np.log10(np.abs(h_dft5)), label="Q2.5")
        plt.title("IIRFilter " + printName)
        plt.xlabel("Fréquence [Hz]")
        plt.ylabel("Gain [dB]")
        plt.grid(which="both", axis="both")
        plt.legend()
        plt.tight_layout()

