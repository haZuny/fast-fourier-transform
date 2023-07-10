import numpy as np
import matplotlib.pyplot as plt
from make_wave_from_np import *

# plt 그래프 사이즈 변경
plt.rcParams['figure.figsize'] = [20, 12]


'''
데이터간의 간격과 정의역 정의
'''
sRate = 1000  # 헤르츠 단위
array_x = np.arange(0, 1 ,1/sRate)  # x범위 

'''
잡음이 없을 때의 신호의 파형 
'''
# 진동수 50과 120을 갖는 파형이 합쳐져 만든 원래 신호
f = np.sin(2*np.pi*50*array_x) + np.sin(2*np.pi*120*array_x) 
f_clean = f

'''
원래 신호에 noise 추가
'''
# randn: 평균0, 표준편차 1인 난수 발생
f = f + 2.5 * np.random.randn(len(array_x))

'''
그래프, 노이즈와 클린 비교
'''
plt.plot(array_x, f, color='c', linewidth=1.5, label='Nosiy')
plt.plot(array_x, f_clean, color='k', linewidth=2, label='Clean')
plt.legend()
plt.xlim(array_x[0], array_x[-1])
plt.show()

'''
noise, clean wave 파일 생성
(5배 늘림)
'''
makeWaveFile(np.repeat(f, 5), sRate, len(array_x)*5, 'noise')
makeWaveFile(np.repeat(f_clean, 5), sRate, len(array_x)*5, 'clean')

#%% FFT 수행

n = len(array_x)
'''
fft 수행
'''
fft_noise = np.fft.fft(f, n) # 노이즈 데이터 fft 수행

'''
fft 결과 정리
'''
# 1. 결과를 절대값으로 바꿔줌
# 2. fft 연산의 결과는 복소수
# 3. a + bi 의 절대값은 sqrt(a^2 + b^2)
# 4. a^2 + b^2 = 복소수 * 켤레복소수(a+bi) * (a-bi)
fft_v = fft_noise * np.conj(fft_noise) / n # 절대값 변환 후 n으로 나눠서 정규화

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
indices = fft_v > 100
fft_filter = fft_noise * indices
# 푸리에 역변환
ifft = np.fft.ifft(fft_filter)

# 그래프 작성
plt.plot(array_x, f_clean, color='c', linewidth=2, label='Clean')
plt.plot(array_x, ifft, color='k', linewidth=1, label='Filter')
plt.xlim(array_x[0], array_x[-1])
plt.show()

'''
필터 wav 파일 생성
'''
makeWaveFile(np.repeat(ifft, 5), sRate, n*5, 'filter')
