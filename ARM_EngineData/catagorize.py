import pandas as pd
import csv
import numpy as np
def loadfile(csv_file):
	thedata = np.genfromtxt(csv_file, delimiter=',',dtype='float32',filling_values=0)
	# print("\n Printing the data from the csv file.\n")
	# for row in thedata: print(row)
	return thedata

def nameVar(value, classs):
	if classs is 0 : string = "RUL"
	if classs is 1 : string = "setting1"
	if classs is 2 : string = "setting2"
	if classs is 3 : string = "setting3"
	if classs is 4 : string = "s1"
	if classs is 5 : string = "s2"
	if classs is 6 : string = "s3"
	if classs is 7 : string = "s4"
	if classs is 8 : string = "s5"
	if classs is 9 : string = "s6"
	if classs is 10 : string = "s7"
	if classs is 11 : string = "s8"
	if classs is 12 : string = "s9"
	if classs is 13 : string = "s10"
	if classs is 14 : string = "s11"
	if classs is 15 : string = "s12"
	if classs is 16 : string = "s13"
	if classs is 17 : string = "s14"
	if classs is 18 : string = "s15"
	if classs is 19 : string = "s16"
	if classs is 20 : string = "s17"
	if classs is 21 : string = "s18"
	if classs is 22 : string = "s19"
	if classs is 23 : string = "s20"
	if classs is 24 : string = "s21"

	name = str(int(value))+string
	return name

def numToCat(X,p):
	Y = X[:,p]
	newY = np.zeros((1))
	noOfCategories = 8
	step = (float(np.max(Y)) - float(np.min(Y)))/noOfCategories
	steparr = {}
	for i in range(0, noOfCategories+1):
		steparr[i+1] = np.min(Y)+i*step
	# print steparr
	for i in Y:
		for key, value in steparr.items():
			if key < noOfCategories+1:
				if i>= steparr[key] and i<=steparr[key+1]:
					# print steparr[key], i, key, steparr[key+1]
					newY = np.vstack([newY, nameVar(key, p)])
					break
				else:
					dummy = 1
	newY = np.delete(newY,0,0)
	return newY

def deleteColumns(sourceFile, targetFile):
	# there are many classes whose value does not change with cycle, 
	#I am deleting those 

	f=pd.read_csv(sourceFile)
	keep_col = [0,1,2,5,6,7,10,11,12,14,15,16,17,18,20,23,24]
	new_f = f[keep_col]
	new_f.to_csv(targetFile, index=False)


X = loadfile('scrapedData.csv')

num_rows, num_cols = X.shape
catagoryArray = np.zeros((num_rows, 1))

for i in range(0,num_cols):
	Z = numToCat(X,i)
	# print np.size(Z)
	catagoryArray = np.hstack([catagoryArray, numToCat(X,i)])
catagoryArray = np.delete(catagoryArray,0,1)

with open('catagorizedData.csv', 'wb') as f:
    csv.writer(f).writerows(catagoryArray)

deleteColumns('catagorizedData.csv', 'ARMData.csv')





# def numToCat(X,p):
# 	Y = X[:,p]
# 	newY = np.zeros((1))
# 	noOfCategories = 6
# 	step = (float(np.max(Y)) - float(np.min(Y)))/noOfCategories
# 	steparr = {}
# 	for i in range(0, noOfCategories+1):
# 		steparr[i+1] = np.min(Y)+i*step
# 	# print steparr
# 	for i in Y:
# 		for key, value in steparr.items():
# 			if i> value:
# 				continue
# 			else:
# 				newY = np.vstack([newY, nameVar(key-1, p)])
# 				# print i, value, key-1
# 				break
# 		continue
# 	newY = np.delete(newY,0,0)
# 	return newY