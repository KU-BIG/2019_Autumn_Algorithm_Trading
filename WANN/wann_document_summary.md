## Weight Agnostic Neural Network



#### Introduction  



랜덤으로 weight 가 초기화 되어 있어도 특정한 task를 수행할 수 있는 뉴럴넷 구조를 찾는 논문.  

동물이 태어나자마자 걸을 수 있다는 것에서 영감을 얻은 연구: 막 탄생된 생명체는 학습 없이 complex motor나 sensory tasks를 할 수 있다 -> training 없이 네트워크 아키텍처를 구성할 수 있다(?) (가중치 학습 말하는 거겠죵?)

weight를 학습하는 것이 아니라, 구조를 학습하는 것   





#### Idea  

가중치를 학습하지 않고 그냥 한번 랜덤하게 설정한 후에, 네트워크 아키텍처를 탐색함으로써 

좋은 퍼포먼스를 내고자 하는 것



#### Finding WANNs   

1. 작은 사이즈의 neural network architecture 들의 집단에서 시작함    

   매우 적은 connection인 상태에서 시작함  

2. well-establihed topology search algorithm을 사용해서,

   single connection이나 single node를 더하는 과정을 반복함으로써 architecture를 진화시키기  





![](C:\Users\USER\Documents\GitHub\2019_Autumn_Algorithm_Trading\WANN\image2.png) 



left: inputs와 outputs가 부분적으로만 연결된 minimal network topology(그냥 노드랑 아크 있고 어떻게든 연결해 놓은 형태)에서 시작    

Middle: 네트워크 구조는 다음 세 가지 방법들 중 하나에 의하여 변경됨    

​				(1) Insert Node: 이미 존재하는 connection(wiring) 을 나누면서 새로운 노드가 삽입됨

​				(2) Add Connection: 이미 존재하는 연결되어 있지 않은 두 노드들을 연결하는 connection이 생김

​				(3) Change Activation: 한 hidden node의 activation function을 변경, ex) linear, step, sin, cosine, 					  Gaussian, tanh, sigmoid, inverse, absolute value, ReLU     



또한 중요한 것은 필요한 만큼만 복잡한 네트워크 아키텍처를 찾는 것이 중요하다는 것이다. 

따라서 네트워크의 __performance__과 __complexity__를 동시에 최적화 해야 할 것임  

이때 multi-objective optimization에서 파생된 techniques를 이용함    



![](C:\Users\USER\Documents\GitHub\2019_Autumn_Algorithm_Trading\WANN\image8.png)   



1번부터 4번까지 진행한 후에 2번에서부터 다시 반복함.  







또 이 모델의 장점은 같은 architectures를 여러 개로 copy한 후에, weight를 다르게 해서 ensemble을 수행할 수 있고, 그 결과 성능이 더 올라갔다(mnist classification에 대해서).  









__Reference__

[WANN 정리한 도큐먼트](<https://towardsdatascience.com/weight-agnostic-neural-networks-fce8120ee829>)    

[open source github](<https://github.com/google/brain-tokyo-workshop/tree/master/WANNRelease>)    

[paper](<https://arxiv.org/pdf/1906.04358.pdf>)   

