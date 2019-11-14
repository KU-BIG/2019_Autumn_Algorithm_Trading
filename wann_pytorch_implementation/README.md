# Weight Agnostic Neural Networks PyTorch Implmentation



# What we need

## 1. Class converts matrix representating graph to PyTorch NN model

- shape(matrix) : [# of nodes x # of nodex] ?
  - As limitation exists for input and output layer, it might be reduced
  - activation fuction can be also represented in this format like below. In matrix, from node to node
    - 0 : no connection 
    - 1 : connection with linear activation function
    - 2 : connection with ReLU activation function
    - and so on..

## 2. NEAT Algorithm

- It might be already implemented in other packages
- If it is, just use it
- If not, implement like [this( sklearn-genetic)](https://pypi.org/project/sklearn-genetic/)
  - it should have estimator which caculate the fitness
  - GeneticSelectionCV() class 
  - GeneticSelectionCV().fit() performs search, it saves history and the optimal result inside the class
  - and so on .. (need further digging)

