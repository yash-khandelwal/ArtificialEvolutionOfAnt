from typing import List, Callable, NewType, Optional
import numpy as np


ActivationFunction = NewType('ActivationFunction', Callable[[np.ndarray], np.ndarray])

# cell 1
class NeuralNetwork:
  def __init__(self, X, Y, n_h, params=None):
    self.input_nodes = layer_sizes(X, Y)[0]
    self.ouput_nodes = layer_sizes(X, Y)[2]
    self.hidden_nodes = n_h
    self.layer_nodes = [X.shape[0]]
    self.layer_nodes.extend(n_h)
    self.layer_nodes.append(Y.shape[0])
    self.params = {}
    self.initialize_parameters(self.input_nodes, self.hidden_nodes, self.ouput_nodes)

  def forward_propagation(self, X):
    A_prev = X
    L = len(self.layer_nodes) - 1  # len(self.params) // 2

    # Feed hidden layers
    for l in range(1, L):
        W = self.params['W' + str(l)]
        b = self.params['b' + str(l)]
        Z = np.dot(W, A_prev) + b
        A_prev = relu(Z)
        # self.params['A' + str(l)] = A_prev

    # Feed output
    W = self.params['W' + str(L)]
    b = self.params['b' + str(L)]
    Z = np.dot(W, A_prev) + b
    out = sigmoid(Z)
    # self.params['A' + str(L)] = out

    return out

  def initialize_parameters(self, n_x, n_h, n_y):
    """
    Argument:
    n_x -- size of the input layer
    n_h -- size of the hidden layer
    n_y -- size of the output layer
    
    Returns:
    params -- python dictionary containing your parameters:
                    W1 -- weight matrix of shape (n_h, n_x)
                    b1 -- bias vector of shape (n_h, 1)
                    W2 -- weight matrix of shape (n_y, n_h)
                    b2 -- bias vector of shape (n_y, 1)
    """
    
    for l in range(1, len(self.layer_nodes)):
      self.params['W' + str(l)] = np.random.uniform(-1, 1, size=(self.layer_nodes[l], self.layer_nodes[l-1]))
      self.params['b' + str(l)] = np.random.uniform(-1, 1, size=(self.layer_nodes[l], 1))
    # ### START CODE HERE ### (≈ 4 lines of code)
    # # W1 = np.random.randn(n_h, n_x)
    # # For Tanh only
    # W1 = np.random.normal(-1, 1, size=(n_h, n_x))
    # # b1 = np.zeros(shape=(n_h, 1))
    # b1 = np.random.normal(-1, 1, size=(n_h, 1))
    # # W2 = np.random.randn(n_y, n_h)
    # W2 = np.random.normal(-1, 1, size=(n_y, n_h))
    # # b2 = np.zeros(shape=(n_y, 1))
    # b2 = np.random.normal(-1, 1, size=(n_y, 1))
    # ### END CODE HERE ###

def layer_sizes(X, Y):
    """
    Arguments:
    X -- input dataset of shape (input size, number of examples)
    Y -- labels of shape (output size, number of examples)
    
    Returns:
    n_x -- the size of the input layer
    n_h -- the size of the hidden layer
    n_y -- the size of the output layer
    """
    ### START CODE HERE ### (≈ 3 lines of code)
    n_x = X.shape[0] # size of input layer
    n_h = 16
    n_y = Y.shape[0] # size of output layer
    ### END CODE HERE ###
    return (n_x, n_h,  n_y)



relu = ActivationFunction(lambda X: np.maximum(0, X))
sigmoid = ActivationFunction(lambda X: 1.0 / (1.0 + np.exp(-X)))
def softmax(z):
    """Softmax function"""
    return np.exp(z) / np.sum(np.exp(z))

# def sigmoid(x):
#     return 1/(1+np.exp(-x))

def MinMaxScaler(x, min, max):
  return  (x - min) / (max - min)
