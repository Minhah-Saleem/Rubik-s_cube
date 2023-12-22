# Rubik-s_cube
Solving Rubik's cube using Reinforcement Learning <br />
Reference: https://github.com/azaharyan/DeepCube/tree/main <br />
This code implements a reinforcement learning model to solve the Rubik's Cube problem. The
code can be broadly divided into the following parts:<br />
CubeEnv Class: This class represents the Rubik's Cube environment, managing the state of
the cube and handling various actions. The get_one_hot_state() function returns the cube's
state in One-Hot encoding, and the get_direct_children_if_not_solved() function obtains all
possible next steps from the current state.<br />
MCTS (Monte Carlo Tree Search) Class: This class implements the MCTS algorithm. The
train() function explores and expands the tree, while the backpropagate() function
backpropagates rewards. It performs reinforcement learning through MCTS.<br />
Model Creation and Training: The buildModel() and compile_model() functions create and
compile a Keras model. The adi() function trains the model for a given number of iterations.
Training data includes information about various states of the cube and the corresponding
possible actions.<br />
Other Files: The remaining files mainly provide auxiliary functions necessary for running the
environment, model, and training process.<br />
This implementation involves converting the cube's state into One-Hot encoding, performing
reinforcement learning using MCTS, and training the model from training data. It uses MCTS to
solve the cube, finding the optimal actions as it progresses.<br />
This project began with a careful analysis of the details of the "Solving the Rubik’s Cube Without
Human Knowledge" paper (S McAleer et al., 2018) and providing an overview and summary of
the ADI algorithm.<br />
The next steps of the project involved the actual implementation of the algorithm. The
implementation specifically focused on replicating the results presented in the original paper,
utilizing open resources such as GitHub.<br />
While the implementation results were documented in the report, the high inference time
prevented the confirmation of the paper's results. Although, it was confirmed that for our system
specification, a fully scrambled cube CAN take more than 60 mins to be solved, negating the
paper’s claims.
