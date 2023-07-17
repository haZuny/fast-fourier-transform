
import numpy as np
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
fft_noise = np.fft.fft(wavArr, n) # 노이즈 데이터 fft 수행

'''
fft 결과 정리
'''
# 1. 결과를 절대값으로 바꿔줌
# 2. fft 연산의 결과는 복소수
# 3. a + bi 의 절대값은 sqrt(a^2 + b^2)
# 4. a^2 + b^2 = 복소수 * 켤레복소수(a+bi) * (a-bi)
fft_v = fft_noise * np.conj(fft_noise) # 절대값 변환
# 정규화, max, min은 15% 절삭
cutRate = int(n * 0.1 / 100)
fft_sorted = sorted(fft_v)
fftMax = fft_sorted[-cutRate]
fftMin = fft_sorted[cutRate]
fft_nomalize = (fft_v - fftMin) / (fftMax-fftMin)

'''
진동수로 정의역 정의
'''
# 최대 진동수 = 전체 샘플 수 / 2 (sin 함수 절반) 
freq = np.arange(n//2)

# 그래프 작성
plt.plot(freq, fft_v[:n//2])
plt.xlim(freq[0], freq[-1])
plt.show()


'''
noise 필터링
'''
# 진동수 밀도가 100 이상인 값만 필터링
indices = fft_nomalize > 0.1
fft_filter = fft_noise * indices
# 푸리에 역변환
ifft = np.fft.ifft(fft_filter)

# 그래프 작성
plt.plot(arr_x, wavArr, color='c', linewidth=2, label='Clean')
plt.plot(arr_x, ifft, color='k', linewidth=1, label='Filter')
plt.xlim(arr_x[0], arr_x[-1])
plt.show()

'''
필터 wav 파일 생성
'''
makeWaveFile(ifft, sRate, n, 'filter')
