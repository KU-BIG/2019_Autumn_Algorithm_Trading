#### backtesting.py 튜토리얼 보고 생각한 것들     



\- 튜토리얼에서는 simple moving average(sma) 전략이 좋은지를 판단하였음



\- 만약 backtesting.py를 그대로 사용한다면  

GOOG 자리에 우리가 사용하고자 하는 회사들의 주가 데이터(전처리 완료된)가 들어갈 것임  -> __Stock_data__ 라고 임의로 이렇게 부르자. 

\- Strategy 메소드는 그냥 그대로 호출하고, SmaCross 대신에 새로운 class를 짜주어야 하는데, 

예를 들어 Sma 전략 대신 WANN 을 사용한다면 WANN을 이용해서 어떤 경우에 사고(buy), 어떤 경우에 팔지(sell) 를 새로운 class 내에 로직을 짜 주어야 할것.  



````python
# 아래 코드들은 애매한 생각에 기반한 수도코드임.. 
# 튜토리얼에서는 SMA 함수를 짜줬는데 WANN을 사용하려면 이런 식으로 따로 코딩해주어야 함  

def WANN_output(values, n):
	
	output = WANN(values)
	
	return output  
````



```python
# 아래 코드들은 애매한 생각에 기반한 수도코드임.. 

from backtesting import Strategy 

class WANN_logic(Strategy):
	
	def init(self):
		self. ~~~ 어쩌구저쩌구
		
	def next(self):
		if ~
			self.buy()
		
		elif ~
			self.
```



 그러고 나서 backtesting 하는 코드는 아마도 다음처럼 될 것(optimization 아직 적용하지 않음)  

```python
from backtesting import Backtest

bt = Backtest(Stock_data, WANN_logic, cash = 10000, commision = .002)
```



