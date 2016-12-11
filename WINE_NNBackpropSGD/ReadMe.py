""" 
Neural Networks
Back Propagation
Stochastic Grad Descent
"""

'''
DATASET  :::
    Alcohol
    Malic Acid
    Ash
    Ash Alcalinity
    Magnesium
    Total Phenols
    Flavanoids
    Nonflavanoid Phenols
    Proanthocyanins
    Color Intensity
    Hue
    OD280/OD315 of dedulted wines
    Proline
'''

"""
1. Initialize a network :  initialize_network(4,2,2)
    x1                      
    x2      h1      y1      
    x3      h2      y2      
    x4      bias            
    bias

A network is basically layers of weights
Layer1: W1[X,X,X,X,X]   W2[X,X,X,X,X]   Wbias[X,X,X,X,X]
Layer2: W1[X,X,x]       W2[X,X,X]

2. Forward Propagate: Neuron Activation
activation = sum(weight_i * input_i) + bias

3. Forward Propagate: Neuron output
output = 1 / (1 + e^(-activation))

4. Forward Propagate: Neuron Transfer
This will give a list of outputs.
In example case : Y1, Y2
for each neuron in each layer we added output of that neuron

5. Back Propagate Error: Transfer Derivative
Given an output value from a neuron, we need to calculate its slope.
sigmoid fn derivative : derivative = output * (1.0 - output)

6. Back Propagate Error: Error Backpropagation
The first step is to calculate the error for each output neuron, this will 
give us our error signal (input) to propagate backwards through the network.
For final layer : error_1 = (expected_Y1 - output_Y1) * transfer_derivative(output_Y1)
The error signal for a neuron in the hidden layer is calculated as the 
weighted error of each neuron in the output layer. 
Hidden Layer & output Layer : error = (W1 * error_1) * transfer_derivative(output_H1)
Input Layer & Hidden Layer : error = (w1 * error_1) * transfer_derivative(output_I1)
for each neuron in each layer we added error of that neuron

7. Train Network : Stochastic Gradient Method: Updating Weights
Network weights are updated as follows: weight = weight + learning_rate * error * input
The same procedure can be used for updating the bias weight, except 
there is no input term, or input is the fixed value of 1.0.

8. Train Network : Stochastic Gradient Method
This involves first looping for a fixed number of epochs and within each 
epoch updating the network for each row in the training dataset.
The expected number of output values is used to transform class values 
in the training data into a one hot encoding. That is a binary vector with 
one column for each class value to match the output of the network. This is 
required to calculate the error for the output layer.

"""