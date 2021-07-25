import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import FilterFunction as ff


ff.MyFilter(256,20000,500,"lowpass", "LowPass",1)
ff.MyFilter(255,20000,[500, 1500],"bandpass","BandPass#1",1)
ff.MyFilter(255,20000,[1500, 2500],"bandpass","BandPass#2",1)
ff.MyFilter(255,20000,[2500, 4500],"bandpass","BandPass#3",1)
ff.MyFilter(255,20000,4490,"highpass","highpass",1)
plt.show()