### GCP랑 Docker 세팅

__한 일__      

- [x] gcp 계정 만들기
- [x] gpu 승인 받기
- [x] ssh 접속 위해서 putty로 키 설정하고 접속 명령어만 치면 서버 접속 가능한 상태로 만들기
- [x] cpu 인스턴스, gpu 인스턴스 만들고 서버 접속 가능한 상태로 만들기   
- [x] cpu 서버랑 gpu 서버에 docker 세팅하고 nvidia 드라이버 다운받기  

__해야 할 일__  

- [ ] gpu 서버 내에 파이썬 환경 세팅하기(jupyterlab) + 여러 파이썬 모듈들 설치  
- [ ] 데이터 수집 코드, backtesting, WANN(혹은 다른 트레이딩 전략) gpu 인스턴스 내에 환경세팅하기   





### 데이터 수집(주가 데이터 인프라)  

\- 분단위 주가 긁어오기 위함

- [ ] <s>증권사 API 붙여서 긁어와야 함</s> -> 현우오빠가 해결했음 
- [ ] [대신증권 API 튜토리얼](<https://wikidocs.net/2870>)  : 계좌 개설해야 해서 다음주 중에 개설한 후 할것  -> 후순위로 밀려남  
- [x] 도커 세팅할것  - gcp 이용했음    

\- 일단 회사 리스트 확인하고 데이터 봐야함    

- [ ] 코드 followup on gcp   



### Backtesting Method  

- [x] 포괄적인 개념조사 및 정리

- [x] <s>패키지 zipline 사용방법 digging</s>s  

[	zipline](<https://wikidocs.net/2874>)   

- [x] backtesting.py 튜토리얼 followup - 애매한 부분들 존재하기는 함  


### WANN

- [x] 관련논문 읽고정리  -> wann docks 읽는 것으로 대체    
- [ ] gpu 서버에 세팅하기 ( git clone, jupyterlab 서버세팅 등)     
- [ ] github 코드 튜토리얼  -> 근데 이 wann을 계속 쓸지 모르겠음    
- [ ] WANN 대체 알고리즘 있는지 찾아보기     

__MNIST에 대해__   

1. reproducing 해서, 논문에서 똑같은 세팅으로 하고  
  backpropagation을 적용했을 때 성능 차이가 얼마나 나는지 실험(with REINFORCE)    

  backpropagation이 잘 적용되지 않는다면 그 이유가 무엇일까? 잘 사용되지 않는 activation function(various actiavation) 때문에 optimization landscape가 발생한다고 document에 나와있음.   

  

  - 논문에서 사용한것처럼 다양한 activation사용하면서 backprop -> 논문에서 제시된 1~4 (random weight, .., ..., fine-tune)과 비교 -> 성능이 얼마나 떨어지는지
  - ReLU만 사용해서 MNIST에 대한 best topology 찾고, backprop으로 fine tune -> 논문에서 제시한 성능이랑 얼마나 차이나는지 + params. 가 얼마나 차이나는지
  - Gradient Vanshing을 크게 일으킬것으로 기대되는 activation빼고 사용하여 위와 같은 방법으로 비교



성능이 낮다 하면 activation function을 relu만 쓰거나 아니면 relu, sigmoid, tanh와 같은 일반적인 activation function을 썼을 때 어떻게 되는지 -> 성능차이랑 네트워크 사이즈가 너무 커지지는 않는지..(relu같은 거 쓰면 네트워크 complexity가 작아서 네트워크 사이즈가 커질 수 있다는 단점)   

2. Visualization -> pytorch에서 제공하는 메소드 쓸듯.(예쁘진 않음)         











