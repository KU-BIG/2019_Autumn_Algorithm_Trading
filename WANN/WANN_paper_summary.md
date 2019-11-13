## Weight Agnostic Neural Networks  



#### Abstract 

weight parameter가 architecture에 비해 얼마나 더 중요한지에 대한 의문심을 제기하고 있음 

어떠한 weight parameters를 학습하지 않고, 어느 정도의 architecture만을 가지고 특정한 task를 수행할 수 있는지에 대한 궁금증을 가지게 됨  

-> __explicit weight training을 하지 않고, task를 수행할 수 있는 neural network architectures를 찾는 search method를 제안하는 논문__        



#### 1 Introduction    

motivation: 태어나고 얼마 있지 않은 후에 오리들이 헤엄칠 수 있고 turkeys들이 predators를 시각적으로 인식할 수 있음. (태어나고 어떠한 학습이 이루어지지 않았음에도 불구하고 특정한 task를 수행할 수 있음)    

트레이닝 과정에서, 네트워크는 single shared weight value 를 사용함.  

몇십년 간 도메인에 따라서 적용할 수 있는 모델들이 달랐음: 이미지 분야에서는 CNN, 시계열에서는 RNN이나 LSTM. (각 모델들이 하나의 task밖에 수행하지 못한다는 의미인 것 같음)   -> WANN을 통해서 random weights에 대해서 various tasks를 수행하고자 하였음    

Q: Inductive biases가 정확히 무슨 의미?   



여하튼 weight의 중요성을 강조하지 않으면서 architecture을 찾고자 하였음. 

__적용한 원칙__   

1) assignining a __single shared weight parameter to every network connection__       

2) evaluating the network __on a wide range__ of this single weight parameter       

=> fixed network(네트워크의 architecture가 고정)에서 weight를 optimize하는 것 대신에, 다양한 범위를 가진 weight 내에서 잘 perform할 수 있는 network architecture가 되도록 optimize하겠다   



논문에서 제안한 search method를 MNIST 데이터를 이용해서 supervised learning domain에 적용해 보았는데,

test accuracy가 92% 이상이었음    



논문에서 제안한  search method는 gradient-based method가 아니라는 점에 의의가 있음.    



#### 2 Related Work    



__1. Architecture Search__     

논문 method는 NEAT, an established topology search algorithm에 근거하고 있음. -> weight랑 structure of networks를 동시에 optimize 시킬 수 있음   



#### 3 Weight Agnostic Neural Network Search  

creating network architectures which encode solutions(아마도 논문에서 제안하는 방법론을 지칭하는 게 아닐까 싶음. encode solutions라는 게 특정 task를 수행할 수 있게 한다는 의미라고 해석하였음) 는 NAS와는 다른 문제이다.   



NAS의 목적은 인간이 디자인한 architecture보다, __트레이닝 시__ 더 좋은 성능을 내는 architectures를 만들어 내는 것.  -> 결국 training을 해야 함.     



weight를 random distribution에서 얻어내는 것은, 특정 task의 performance가 오직 network topology 에 의한 것이라고 보장할 수 있음

![](C:\Users\USER\Documents\GitHub\2019_Autumn_Algorithm_Trading\WANN\image8.png)  







 

