import subprocess # 파이썬에서 다른 프로세스를 실행하고(ex. shell) 출력 결과를 가져올 수 있게 해주는 라이브러리

# call: 인자로 넘겨진 값들을 이용하여 프로세스 실행
# (명령어, 옵션(i: input 받음), stdin, stdout)
subprocess.call(['ffmpeg', '-i', 'sample.mp3', 'test222.wav'])
