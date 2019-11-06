

### 백테스팅이란 무엇인가?  

__Backtesting__ = Back(과거 데이터를 사용) + Testing(알고리즘을 테스트) 

= 과거 데이터를 이용하여 개발된 알고리즘 및 널리 통용되고 있는 투자 전략(기존 알고리즘)을 검증해 보는 것.  

미래의 데이터가 없기 때문에 과거 데이터에 의존 



현재의 전략을 과거에 적용했다면 어떠한 수익률을 나타냈을 것인가에 대한 답변을 제공하는 것   

하지만 과거의 높은 수익률이 미래의 높은 수익률을 보장하는 것은 아니라는 것을 염두해야     

목적: 높은 수익률을 찾아내는 것이 아닌, __얼마나 현실을 잘 반영하는가__에 초점을 맞추어야 할 것  



전략 예시: 모멘텀 전략 등



### Zipline  

pandas의 패키지  

python 버전 안맞으면 쓰기 힘들다함 -> 안쓰기로 함  



### Backtesting.py

[Link]([https://kernc.github.io/backtesting.py/doc/examples/Strategies%20Library.html](https://kernc.github.io/backtesting.py/doc/examples/Strategies Library.html))  

일단 가벼움

multiple timeframe에 쓰일 수 있음

vectorized 나 event-based backtesting 모두에 쓰일 수 있음. 

cf) event-based backtesting -> recieves a data feed, or __"events"__, which trigger the algorithm to respond in real time  



### PyAlgoTrade  

development가 stop되었다고 나와있음  / 마지막 버전이 2년 전임 .. 





### Backtrader   

[Link](<https://github.com/backtrader/backtrader>)  

단점: ask and bid prices만 사용하는 거래 시뮬레이션    





__Reference__

<https://m.blog.naver.com/PostView.nhn?blogId=jin62486&logNo=221209090042&proxyReferer=https%3A%2F%2Fwww.google.com%2F>



<https://wikidocs.net/2874>



