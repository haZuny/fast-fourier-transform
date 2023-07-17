import numpy as np
import wave, math

def makeWaveFile(arr, sRate, nSamples, fileName):
    # 데이터 -1~1 사이로 정규화
    maxVal = max(-min(arr), max(arr))
    val = arr/maxVal
    # 16비트 전환
    data = (val * 32767).astype(np.int16)
    # wav 파일 생성
    files = wave.open(fileName + '.wav', 'wb')
    files.setparams((1, 2, sRate, nSamples, 'NONE', 'uncompressed'))
    files.writeframes(data)
    files.close()    