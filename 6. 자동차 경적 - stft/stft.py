import numpy as np
from scipy import signal
from scipy.io.wavfile import *
import matplotlib.pyplot as plt
from make_wave_from_np import *

# plt 그래프 사이즈 변경
plt.rcParams['figure.figsize'] = [20, 12]

'''
wav 파일 오픈
'''
wavF = read("경적.wav")
sRate = wavF[0]  # 헤르츠 단위
wavArr = np.array(wavF[1][:, 1], dtype = float)
print(wavArr)
n = len(wavArr)
arr_x = np.arange(n,) / sRate


'''
그래프
'''
plt.plot(arr_x, wavArr, linewidth=1.5)
plt.xlim(arr_x[0], arr_x[-1])
plt.show()

'''
fft 수행
'''
f, t, Zxx = signal.stft(wavArr, sRate)

plt.ylim([0, 2500])
plt.pcolormesh(t, f, np.abs(Zxx))
plt.show()


'''
noise 필터링
'''
# 진동수 밀도가 100 이상인 값만 필터링
indices = np.abs(Zxx) > 1000
print(max(Zxx[0]))
filtered = indices * Zxx

plt.ylim([0, 2500])
plt.pcolormesh(t, f, np.abs(filtered))
plt.show()

# 푸리에 역변환
istft = signal.istft(filtered, sRate)

# 그래프 작성
plt.plot(arr_x, wavArr, color='c', linewidth=2, label='Clean')
plt.plot(arr_x, istft[1], color='k', linewidth=1, label='Filter')
plt.xlim(arr_x[0], arr_x[-1])
plt.show()

'''
필터 wav 파일 생성
'''
makeWaveFile(istft[1], sRate, n, 'filter')
