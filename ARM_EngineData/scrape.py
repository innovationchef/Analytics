import numpy as np
def loadfile(csv_file):
	thedata = np.genfromtxt(csv_file,skip_header=1, delimiter=',',dtype='float32',filling_values=0)
	# print("\n Printing the data from the csv file.\n")
	# for row in thedata: print(row)
	return thedata

def scrapdata(X):
	Y = X[:,0]
	num_rows, num_cols = X.shape
	newdata = np.zeros((num_cols))
	prevData = Y[0]
	for idx, data in enumerate(Y):	
		if (data - prevData)<=0 : 
			NewData = data
			continue
		else:
			# print X[idx-1]
			newdata = np.vstack([newdata, X[idx-1]])
			prevData = data

	newdata = np.vstack([newdata, X[num_rows-1, :]])
	newdata = np.delete(newdata,0,0)
	newdata = np.delete(newdata,0,1)
	np.savetxt("scrapedData.csv", newdata, delimiter=",")

X = loadfile('PM_train.csv')
scrapdata(X)

