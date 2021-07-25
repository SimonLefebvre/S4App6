import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import FilterFunction as ff


ff.MyFIRFilter(256, 20000, 500, "lowpass", "LowPass", 0)
ff.MyFIRFilter(255, 20000, [500, 1500], "bandpass", "BandPass#1", 0)
ff.MyFIRFilter(255, 20000, [1500, 2500], "bandpass", "BandPass#2", 0)
ff.MyFIRFilter(255, 20000, [2500, 4500], "bandpass", "BandPass#3", 0)
ff.MyFIRFilter(255, 20000, 4490, "highpass", "highpass", 0)
ff.MyIIRFilter(N=4, PB_Gain=1, SB_Gain=70, wn=[950, 1050], fe=20000, Type="bandstop", printName="bandstop", printOption=1)
plt.show()