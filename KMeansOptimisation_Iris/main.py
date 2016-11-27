
####################################### scipy.cluster.vq.kmeans #############################################
# Since vector quantization is a natural application for k-means, information theory terminology is often used. 
# The centroid index or cluster index is also referred to as a code and the table mapping codes to centroids 
# and vice versa is often referred as a code book. The result of k-means, a set of centroids, can be used to
# quantize vectors. Quantization aims to find an encoding of vectors that reduces the expected distortion.
# Since vector quantization is a natural application for k-means, information theory terminology is often used. 
# The centroid index or cluster index is also referred to as a code and the table mapping codes to centroids 
# and vice versa is often referred as a code book. The result of k-means, a set of centroids, can be used to 
# quantize vectors. Quantization aims to find an encoding of vectors that reduces the expected distortion.

# idx = kmeans(X,k) performs k-means clustering to partition the observations of the n-by-p data matrix X into
# k clusters, and returns an n-by-1 vector (idx) containing ###cluster indices### of each observation. Rows of X 
# correspond to points and columns correspond to variables.

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans

def loadfile(csv_file,p):
	thedata = np.genfromtxt(csv_file, delimiter=',',dtype='float32',filling_values=0,usecols =(p,6,7,8))
	print("\n Printing the data from the csv file.\n")
	for row in thedata: print(row)
	return thedata

def plotElbowGraph(K, avgWithinSS):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	# These are subplot grid parameters encoded as a single integer. For example, "111" means "1x1 grid, first subplot" and "234" means "2x3 grid, 4th subplot".
	ax.plot(K, avgWithinSS)
	plt.grid(True)
	plt.xlabel('Number of clusters')
	plt.ylabel('Average within-cluster sum of squares')
	plt.title('Elbow for KMeans clustering')
	plt.show()

p = int(sys.argv[1])
X = loadfile('PM_Score.csv',p)
K = range(1,10)
KM = [kmeans(X,k) for k in K]
centroids = [cent for (cent,var) in KM]   # filter the output of the above function
avgWithinSS = [var for (cent,var) in KM]  # mean within-cluster sum of squares
plotElbowGraph(K, avgWithinSS)