import numpy as np
import wave, math

'''
1. 샘플링 레이트 설정
'''
sRate = 44100 # 1초 몇개로 쪼갤건지, 헤르츠 단위
nSamples = sRate * 5   # 전체 길이

'''
2. 각 샘플의 데이터를 저장할 array 생성
'''
# 0~nSmaples까지의 값을 가지는 배열 생성
x_array = np.arange(nSamples)
# 초로 변환
x = x_array/float(sRate)

'''
3. 소리 데이터 만들기
'''
# 220Hz의 정현파(사인파) 만들어 보기. 
# A=sin(2pift), A:진폭, f:주파수, t:시간 
vals = np.sin(2*math.pi*220.0*x)


'''
4. 데이터를 16비트로 변환
'''
# sin을 거친 vals는 -1~1 사이값을 가짐
# 위의 값을 16비트 값으로 바꿔줌(2^16/2-1 = 32767)
# /2: 절반은 양수, 절반은 음수
# -1: 양수는 0을 포함하므로 -1
# int16: –32,768 ~ 32,767
data = np.array(vals*32767, 'int16')

'''
5. wav파일 생성
'''
# wav 파일 오픈
files = wave.open('test.wav', 'wb')
# 데이터 파일에 적재
# wave파일 생성에 필요한 매개변수 설정: 단일채널(모노), 2바이트(16비트), 비압축 포맷으로 설정 
# (채널 개수, 하나의 rate에 몇 바이트 사용할 것인지, 샘플링레이트, 전체 레이트 길이, 압축 방식, 압축 이름)
files.setparams((1, 2, sRate, nSamples, 'NONE', 'uncompressed'))
files.writeframes(data)
files.close()

# 그래프(0.1초까지만)
import matplotlib.pyplot as plt
plt.plot(x[0:4410], vals[:4410])