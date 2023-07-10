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
'''
makeWaveFile(np.repeat(f, 5), sRate, len(array_x)*5, 'noise')
makeWaveFile(np.repeat(f_clean, 5), sRate, len(array_x)*5, 'clean')
