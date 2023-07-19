# fast-fourier-transform
파이썬으로 소리 처리하기 연습(~푸리에변환)

### 3. 잡음 제거(인공적으로 만든 잡음 제거)
1. Clean Sound

https://github.com/haZuny/fast-fourier-transform/assets/64102831/f0baafbf-7fa8-4940-9bb3-f9036c78c9be

2. Noise Sound

https://github.com/haZuny/fast-fourier-transform/assets/64102831/69020ee8-2065-4d77-9b7b-de1cf3a4a89d

3. Filtered Sound

https://github.com/haZuny/fast-fourier-transform/assets/64102831/e474f9ee-b1ac-4c89-9a27-c63e19f15e53

### 4. 실제 클락션 소리 필터링(FFT로 잡음 제거 시도했으나 실패, 추후 SFFT로 잡음 제거 시도)
1. 원본 클락션 소리

https://github.com/haZuny/fast-fourier-transform/assets/64102831/0d4166f6-e0aa-460e-9453-b764bd28fe67

2. 노이즈 제거 클락션 소리

https://github.com/haZuny/fast-fourier-transform/assets/64102831/aee6f7d6-f9dd-407b-abab-f53734ee81ee

### 6. 실제 클락션 소리 필터링2(Short Time Fourier Transform)

1. 원본 클락션 소리

https://github.com/haZuny/fast-fourier-transform/assets/64102831/6103b4cb-5d66-4392-9d83-abd0a602b92f

2. 노이즈 제거 클락션 소리

https://github.com/haZuny/fast-fourier-transform/assets/64102831/6754179b-8347-4f0c-97bd-79cf687c9c97

<br><br>

# 푸리에 변환 정리

<details>
  <summary>PPT1 - Fourier Trasform</summary>
  
  ![슬라이드6](https://github.com/haZuny/fast-fourier-transform/assets/64102831/e032b9ee-0883-4c39-aef1-eb8652e87625)
  ![슬라이드7](https://github.com/haZuny/fast-fourier-transform/assets/64102831/a80e1144-5c20-4e4a-8134-12ffc09dcd05)
  ![슬라이드8](https://github.com/haZuny/fast-fourier-transform/assets/64102831/b600c71a-8ac8-4052-9bab-f08c8fee09d7)
  ![슬라이드9](https://github.com/haZuny/fast-fourier-transform/assets/64102831/71856166-a731-4a3b-97c7-73c8e459561f)
  ![슬라이드10](https://github.com/haZuny/fast-fourier-transform/assets/64102831/6ae98ef1-54bd-47ef-b1ba-a17c704631fe)
  ![슬라이드11](https://github.com/haZuny/fast-fourier-transform/assets/64102831/ed1d29c6-ab59-41e4-adef-8f8a3ee9fde9)
  ![슬라이드12](https://github.com/haZuny/fast-fourier-transform/assets/64102831/596a4fd9-dcf6-4b49-98df-15080ca5aa76)
  ![슬라이드13](https://github.com/haZuny/fast-fourier-transform/assets/64102831/925edeb6-6b66-40a4-9606-4e3edae06795)
  ![슬라이드14](https://github.com/haZuny/fast-fourier-transform/assets/64102831/98cd097f-5eb0-4be7-8b41-37e88d0c1031)
  ![슬라이드15](https://github.com/haZuny/fast-fourier-transform/assets/64102831/b20fd2ed-e800-4aec-af0e-48a2b4e7059e)
  ![슬라이드16](https://github.com/haZuny/fast-fourier-transform/assets/64102831/22091e53-f13b-4ca1-b7e9-b179de8503b7)
  ![슬라이드17](https://github.com/haZuny/fast-fourier-transform/assets/64102831/f0114096-7314-4a36-a620-6f522485698a)
  ![슬라이드18](https://github.com/haZuny/fast-fourier-transform/assets/64102831/32f0ed36-50bb-4cef-9af3-17b827fb2a7e)
</details>

<details>
  <summary>PPT2 - Short Time Fourier Transform</summary>

  ![슬라이드1](https://github.com/haZuny/fast-fourier-transform/assets/64102831/70bb503a-786a-49ab-a41f-0d34a8820c48)
  ![슬라이드2](https://github.com/haZuny/fast-fourier-transform/assets/64102831/50b4f65d-2a18-4f32-aa29-1ebd7247346f)
  ![슬라이드3](https://github.com/haZuny/fast-fourier-transform/assets/64102831/82943874-4f49-42ba-be70-ddb9b4432325)
  ![슬라이드4](https://github.com/haZuny/fast-fourier-transform/assets/64102831/f9a3db71-b7da-4cd0-84f6-8d259ac7dd4f)
  ![슬라이드5](https://github.com/haZuny/fast-fourier-transform/assets/64102831/81b3ae71-57ab-4e0a-942a-ecfbcf96b9c1)
  ![슬라이드6](https://github.com/haZuny/fast-fourier-transform/assets/64102831/a2cbe5a6-6e47-4319-96c9-267251ecd334)
  ![슬라이드7](https://github.com/haZuny/fast-fourier-transform/assets/64102831/78fae916-86f5-4749-b37c-944862dc7dbd)
  ![슬라이드8](https://github.com/haZuny/fast-fourier-transform/assets/64102831/a6c2abc1-d2af-4858-9c21-dcbc07f97d03)
  ![슬라이드9](https://github.com/haZuny/fast-fourier-transform/assets/64102831/85ecb2cc-c0bf-49b6-9264-2b9bf37cb818)
  ![슬라이드10](https://github.com/haZuny/fast-fourier-transform/assets/64102831/712d3faf-9ea0-4c2f-b378-9af02367705d)
  ![슬라이드11](https://github.com/haZuny/fast-fourier-transform/assets/64102831/bdfad50b-ac1f-440d-b72a-ab0e2468509c)
  ![슬라이드12](https://github.com/haZuny/fast-fourier-transform/assets/64102831/803cc57d-0ae3-4b3a-9c5c-e1cfdce8cad0)
  ![슬라이드13](https://github.com/haZuny/fast-fourier-transform/assets/64102831/76e2f0d1-decf-4834-bc52-8504bb3ef2fa)
  ![슬라이드14](https://github.com/haZuny/fast-fourier-transform/assets/64102831/52f17733-af64-4805-9c69-ac00bdfa7ede)
  ![슬라이드15](https://github.com/haZuny/fast-fourier-transform/assets/64102831/bbf05860-3a02-4021-baab-b083ccae21bb)
  ![슬라이드16](https://github.com/haZuny/fast-fourier-transform/assets/64102831/cdeca6f2-5e98-47ed-9ade-7968fbaec4af)
  ![슬라이드17](https://github.com/haZuny/fast-fourier-transform/assets/64102831/631dab23-bb9a-4f29-af85-4cf192d1d503)
  ![슬라이드18](https://github.com/haZuny/fast-fourier-transform/assets/64102831/5eb35637-6e15-4697-84d6-cf54ff04fe3d)
  ![슬라이드19](https://github.com/haZuny/fast-fourier-transform/assets/64102831/99a30306-1146-47f9-b63c-f34830f391f9)
</details>
