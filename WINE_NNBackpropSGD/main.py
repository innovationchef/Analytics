import pandas as pd
import numpy as np
from random import seed
from random import random
from math import exp
import math
wine = pd.read_csv('wine.csv')
wine.sample(frac=1)  #trying to randomize the dataset
"""Data Normalization"""
def normalize(array):
	MAX = np.amax(array)
	MIN = np.amin(array)
	LEN = np.shape(array)[0]
	for i in range(0,LEN):
		array[i] = (array[i]-MIN)/(MAX-MIN)
	return array


alchl = normalize(wine['Alcohol'].as_matrix())
malicH = normalize(wine['Malic Acid'].as_matrix())
ash = normalize(wine['Ash'].as_matrix())
ashOH = normalize(wine['Ash Alcalinity'].as_matrix())
magnm = normalize(wine['Magnesium'].as_matrix())
phenols = normalize(wine['Total Phenols'].as_matrix())
flav = normalize(wine['Flavanoids'].as_matrix())
nonflav = normalize(wine['Nonflavanoid Phenols'].as_matrix())
pac = normalize(wine['Proanthocyanins'].as_matrix())
clr = normalize(wine['Color Intensity'].as_matrix())
hue = normalize(wine['Hue'].as_matrix())
val = normalize(wine['OD280/OD315 of dedulted wines'].as_matrix())
proline = normalize(wine['Proline'].as_matrix())
wineType = wine['Type'].as_matrix()

def initialize_network(n_inputs, n_hidden, n_outputs):
	network = list()
	hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	network.append(hidden_layer)
	output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(output_layer)
	return network
def activate(weights, inputs):
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
	return activation
def transfer(activation):
	return 1.0 / (1.0 + exp(-activation))
def forward_propagate(network, row):
	inputs = row
	for layer in network:
		new_inputs = []
		for neuron in layer:
			activation = activate(neuron['weights'], inputs)
			neuron['output'] = transfer(activation)
			new_inputs.append(neuron['output'])
		inputs = new_inputs
	return inputs
def transfer_derivative(output):
	return output * (1.0 - output)
def backward_propagate_error(network, expected):
	for i in reversed(range(len(network))):
		layer = network[i]
		errors = list()
		if i != len(network)-1:
			for j in range(len(layer)):
				error = 0.0
				for neuron in network[i + 1]:
					error += (neuron['weights'][j] * neuron['delta'])
				errors.append(error)
		else:
			for j in range(len(layer)):
				neuron = layer[j]
				errors.append(expected[j] - neuron['output'])
		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])
def update_weights(network, row, l_rate):
	for i in range(len(network)):
		inputs = row
		if i != 0:
			inputs = [neuron['output'] for neuron in network[i - 1]]
		for neuron in network[i]:
			for j in range(len(inputs)-1):
				neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
			neuron['weights'][-1] += l_rate * neuron['delta']
def train_network(network, train, l_rate, n_epoch, n_outputs):
	for epoch in range(n_epoch):
		sum_error = 0
		for row in train:
			outputs = forward_propagate(network, row)
			expected = [0 for i in range(n_outputs)]
			expected[int(row[-1])-1] = 1
			sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
			backward_propagate_error(network, expected)
			update_weights(network, row, l_rate)
		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
def predict(network, row):
	outputs = forward_propagate(network, row)
	# print outputs
	return outputs.index(max(outputs))
def dividedata(dataset, ftrain):
	division = int(math.floor(len(dataset) * ftrain))
	print len(dataset), division
	train = []
	test = []
	for i in range(len(dataset)):
		if i<division:
			train.append(dataset[i])
		else:
			test.append(dataset[i])
	return train, test





seed(1)
df = wine.sample(frac=1)
dataset = []
for column in df:
	dataset.append(df[column].as_matrix()) 
dataset = np.transpose(dataset)
train, test = dividedata(dataset, 0.8)


n_inputs = len(train[0]) - 1
n_outputs = len(set([row[-1] for row in train]))
network = initialize_network(n_inputs, 5, n_outputs)
train_network(network, train, 0.3, 500, n_outputs)
for row in test:
	prediction = predict(network, row)
	print('Expected=%d, Got=%d' % (row[-1], prediction))
