# Backtesting Methods 

### What is Backtesting? 

- 새로운 전략개발 또는 기존 전략의 검증을 위해 과거 데이터를 가지고, 실험하고자 하는 전략의 성과를 측정해 보는 과정이다. 
- 이 투자 전략을 과거에 똑같이 적용했다면 성과가 어땠을까? 

##### 1. Profit / Loss

		- 개발한 시스템에 특정 기간의 데이터를 입력해 trading을 실시한다. 그때 발생하게 되는 Profit과 Loss를 평가한다. 

- ![image-20191030214135464](C:\Users\양수형\AppData\Roaming\Typora\typora-user-images\image-20191030214135464.png)

- https://programmingfbf7290.tistory.com/entry/6-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A0%84-%ED%9B%84-%EC%88%98%EC%9D%B5%EC%9C%A8-%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%82%A4%EC%9B%80-open-api-%EC%A3%BC%EC%8B%9D-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D

- 단점 : 수익률 15% model vs 수익률 9% model => 둘 중 어느 하나가 낫다고 할 수 없다. 우연에 의해 한 두번의 고수익이 만들어 낸 수익률 일 수 있기 때문.

  

##### 2. Hit Ratio(적중률)

- 모델을 이용해 예측한 결과의 정확도를 의미한다. 

- Hit Ratio = 수익횟수/전체거래횟수

- 즉, 모델에 따라 거래를 했을 때 전체거래에서 수익을 발생시킨 비율. 

- If Hit Ratio=1, 모든 거래에서 수익을 발생시켰다. vs Hit Ratio = 0.4 , 10번의 거래 중 4번 수익을 냈다. 

  ​	model A : 수익률 15%, 적중률 10%. 

  ​	model B : 수익률 9%, 적중률 55% 

  ​	=> 이 경우 적중률이 높은 B 모델이 안정적이고 예측가능 하다. 

- 따라서 모델의 성능을 평가하는 데에 단순 Profit(수익률)보다 효과적이다.

- 뿐만 아니라 손실이 지속된다면 투자모델을 바꾸어야 하는지, 일시적 현상인지 고민을 해야 하는데, 만약 적중률이 높은 모델이라면 상대적으로 높은 신뢰도를 가지고 있기 때문에 유지할 수 있다. 하지만 그렇지 않은 모델의 경우 다시 투자모델을 생성해야 할지도. 

- 과거 데이터를 이용하기 때문에 머신러닝 모델의 경우 학습에 사용되었던 데이터와 테스트에 사용한 데이터가 중복되지 않도록 주의한다. 

  

##### 3. Drawdown

- Drawdown(손실률)은 상품(invetstment), 펀드 또는 선물에서 특정 기간동안 발생한 시세 고점에서 저점까지의 하락을 의미한다. 

- 잘못된 예측이 얼마나 되는지, 잘못된 예측의 기간이 얼마인지를 알려준다. 

- 따라서, 금융 리스크와 파산의 위험성에 대한 정보를 제공한다. 

- ![image-20191030214441712](C:\Users\양수형\AppData\Roaming\Typora\typora-user-images\image-20191030214441712.png)

- 최대 손실률(Maximum Drawdown), 손실 지속 기간(Drawdown duration), 손실 경향(Drawdown Curve) 등을 알 수 있다. 

- MDD(Maximum Drawdown) : 시세가 새 고점에 도달하기 전에 그 이전 고점에서 저점까지의 최대 손실을 의미한다. 계산 방식은 다음과 같다. 

  (저점값 - 고점값) / 고점값 * 100 %

  ![image-20191030222635688](C:\Users\양수형\AppData\Roaming\Typora\typora-user-images\image-20191030222635688.png)

  MDD 이해를 위한 그림 : 

  ![image-20191030222800514](C:\Users\양수형\AppData\Roaming\Typora\typora-user-images\image-20191030222800514.png)

  포트폴리오 1에서는 drawdown(낙폭)이 1번 발생했다. 따라서 MDD는 (65-130)/130 = -50% 로 계산된다. 

  ![image-20191030223006322](C:\Users\양수형\AppData\Roaming\Typora\typora-user-images\image-20191030223006322.png)

  포트폴리오 2에서는 Drawdown(낙폭)이 2번 발생했다. 이 두개의 (70-100)/100 = -30%와 (160-220)/220=-27% 중 MDD는 둘 중 큰 값인 -30%가 된다. 

- 수익률과 더불어 알고리즘 트레이딩을 지속해야 할 지 말지를 결정하는 데에 중요한 역할을 한다. 

##### 4. Sharpe Ratio

- 위험을 고려한 성능을 나타내는 수치이다. 

- Sharpe Ratio란 위험 자산에 투자함으로써 얻은 초과 수익의 정도를 나타내는 지표이다. 

- Sharpe Ratio = 초과수익률/초과수익률의 표준편차 (1994년 기준)

  <img src="C:\Users\양수형\AppData\Roaming\Typora\typora-user-images\image-20191030224518648.png" alt="image-20191030224518648" style="zoom:50%;" />

  분자 : 기준지표 수익률 대비 자산의 초과수익률

  분모 : 자산수익률의 표준편차

  ​	초과수익률은 펀드 수익률에서 무위험 수익률(국공채 수익률)을 차감하여 계산한다.

  ​	주식형 펀드의 경우 종합주가지수 또는 주식 수익률을 기준 수익률로 삼는다.

- ![image-20191030214552620](C:\Users\양수형\AppData\Roaming\Typora\typora-user-images\image-20191030214552620.png)

- Sharpe Ratio가 높으면 감수한 위험 대비 수익이 좋다는 의미이기 때문에 Sharpe Ratio가 높은 펀드가 좋은 펀드라고 볼 수 있다. 

- 일반적인 펀드 영역에서는 Sharpe Ratio가 1 정도면 그럭저럭 괜찮은 펀드, 2정도면 쓸만한 펀드, 3 이상이면 아주 괜찮은 펀드로 볼 수 있다.

- 주식형 펀드는 괜찮은 성능을 내고 있지만 Sharpe Ratio가 1에 미치지 못하는 경우가 많다. 이는 주식형 펀드의 경우 기준으로 삼는 수익률은 종합주가지수 또는 주식 수익률이지만 샤프 지수 계산 식에서 초과 수익률을 계산할 때는 국공채 수익률을 이용하는 것과 관련되어있다. 

- 따라서 Sharpe Ratio를 해석할 때 1보다 크거나 작다를 따지기 보다는 다른 펀드와의 상대적인 비교 용도로 사용하는 것이 좋다. 즉, 두 자산을 공동의 기준지표와 비교할 경우, 더 높은 Sharpe Ratio를 나타내는 자산이 동일 위험에 대해 더 높은 수익률을 제공한다. 

- 주의할 점은, 샤프 비율은 모든 변동성을 동일하게 취급한다. 즉, 상승편차(upside volatility)를 갖는 (높은 수익률을 갖는) 전략에 불이익을 주게 된다. 

  

#### Links

 https://jjeongil.tistory.com/678 

 https://www.mk.co.kr/news/business/view/2017/11/758574/ 

 https://www.investopedia.com/terms/d/drawdown.asp 

 [https://support.heybit.io/ko/articles/2388132-mdd%EB%8A%94-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80%EC%9A%94](https://support.heybit.io/ko/articles/2388132-mdd는-무엇인가요) 

 [https://ko.wikipedia.org/wiki/%EC%83%A4%ED%94%84_%EB%B9%84%EC%9C%A8](https://ko.wikipedia.org/wiki/샤프_비율) 