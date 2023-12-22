# DeepCube
Tensorflow/Keras implementation of [DeepCube paper](https://arxiv.org/pdf/1805.07470.pdf) by McAleer et al. that solves the Rubik's Cube using Deep Reinforcement Learning. We used a feed-forward network and a RNN network to compare the result. Both models are augmented with Monte Carlo Tree Search for solving the cube itself.

## Prerequisites
* [Tensorflow - v2.4.0](https://github.com/tensorflow/tensorflow)
* [pycuber](https://github.com/adrianliaw/PyCuber)
* [numpy](https://github.com/numpy/numpy)
* [matplotlib](https://github.com/matplotlib/matplotlib)

## Summary of the implementation of the algorithm in code:
Reference: https://github.com/azaharyan/DeepCube/tree/main <br />
This code implements a reinforcement learning model to solve the Rubik's Cube problem. The code can be broadly divided into the following parts:
### CubeEnv Class: 
This class represents the Rubik's Cube environment, managing the state of the cube and handling various actions. The get_one_hot_state() function returns the cube's state in One-Hot encoding, and the get_direct_children_if_not_solved() function obtains all possible next steps from the current state.
### MCTS (Monte Carlo Tree Search) Class: 
This class implements the MCTS algorithm. The train() function explores and expands the tree, while the backpropagate() function backpropagates rewards. It performs reinforcement learning through MCTS.
### Model Creation and Training: 
The buildModel() and compile_model() functions create and compile a Keras model. The adi() function trains the model for a given number of iterations.
Training data includes information about various states of the cube and the corresponding possible actions.
### Other Files: 
The remaining files mainly provide auxiliary functions necessary for running the environment, model, and training process. <br />
This implementation involves converting the cube's state into One-Hot encoding, performing reinforcement learning using MCTS, and training the model from training data. It uses MCTS to
solve the cube, finding the optimal actions as it progresses.

## Running
To run and train the model all you need to do is run training.ipynb file. 


