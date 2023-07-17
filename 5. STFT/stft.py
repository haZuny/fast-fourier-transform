import numpy as np
import matplotlib.pyplot as plt
import make_wave_from_np

def sin_wave(amp, freq, time):
    return amp * np.sin(2*np.pi*freq*time)

sampleTime = 0.001

time = np.arange(0, 3, sampleTime)

# 파동 생성
sin1 = sin_wave(1, 100, time)
sin2 = sin_wave(2, 150, time)
sin3 = sin_wave(4, 180, time)

# 파동 연결 + 노이즈 추가
sin_sum = sin1 + sin2 + sin3
sin_concat = np.concatenate((sin1, sin2, sin3, sin_sum))
sin_concat = sin_concat + np.random.rand(len(sin_concat))

# 소리 파일 생성
make_wave_from_np.makeWaveFile(sin_concat, 1000, len(sin_concat), "origin")

# 그래프
time = np.arange(0, 12, sampleTime)
plt.figure(figsize=(12,5))
plt.plot(time, sin_concat)
plt.grid()
plt.show()


n = len(sin_concat) 
k = np.arange(n)
Fs = 1/0.001; T = n/Fs
freq = k/T 
freq = freq[range(int(n/2))] 

# FFT
Y_origin = np.fft.fft(sin_concat)/n
Y = Y_origin[:n//2]

# fft 그래프
plt.plot(freq, abs(Y), 'r') 
plt.show()

# 필터링
filterFreq = Y_origin > 0.2
filteredGraph = filterFreq * Y_origin
filtered = np.fft.ifft(filteredGraph)

# 필터링된 파동 그래프
plt.figure(figsize=(12,5))
plt.plot(time, filtered)
plt.grid()
plt.show()

# 소리 파일 생성
make_wave_from_np.makeWaveFile(filtered, 1000, n, "filtered")

# STFT
from scipy import signal

# f: 주파수, t: 타임, Zxx: stft 결과
f, t, Zxx = signal.stft(sin_concat, 1000, nperseg=1000)

plt.pcolormesh(t, f, np.abs(Zxx))
plt.ylim([0,200])
plt.show()

filtered = np.abs(Zxx) > 0.1

Zxx = filtered * Zxx

plt.pcolormesh(t, f, np.abs(Zxx))
plt.ylim([0,200])
plt.show()

it, filtered = signal.istft(Zxx, 1000)

plt.figure(figsize=(12,5))
plt.plot(it, filtered)
plt.grid()
plt.show()

make_wave_from_np.makeWaveFile(filtered, 1000, n, "stft-filtered")
