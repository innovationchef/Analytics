import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from matplotlib import*
import matplotlib.pyplot as plt
from matplotlib.cm import register_cmap
from scipy import stats
#from wpca import PCA
from sklearn.decomposition import PCA as sklearnPCA
import seaborn

"""
movie.csv [movieID, title, genre]
ratings.csv [usedID, movieID, rating, timestamp]
"""
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('	ratings.csv')
ratings.drop(['timestamp'], axis=1, inplace=True)#axis=1 means column #axis=0 means rows

############################################################
'''Replace MovieID in the rating column with the Movie names associated with it'''
'''
To select out everything for variable A we could do:

In [2]: df[df['variable'] == 'A']
Out[2]: 
  	      date     variable     value
0 	2000-01-03        A 	  	 0.469112
1 	2000-01-04        A 		-0.282863
2 	2000-01-05        A 		-1.509059
'''
def replace_name(x):
	return movies[movies['movieId']==x].title.values[0]
ratings.movieId = ratings.movieId.map(replace_name)
############################################################
'''Pivoting the Table'''
'''
		date 		variable       value
0 	2000-01-03	        A 	 	 0.469112
1 	2000-01-04       	A 		-0.282863
2 	2000-01-05       	A 		-1.509059
	
PIVOTED TABLE
variable           A         B         C         D
date                                              
2000-01-03  0.469112 -1.135632  0.119209 -2.104569
2000-01-04 -0.282863  1.212112 -1.044236 -0.494929
2000-01-05 -1.509059 -0.173215 -0.861849  1.071804
'''
M = ratings.pivot_table(index=['userId'], columns=['movieId'], values='rating').head(200)
m = M.shape
df1 = M.replace(np.nan, 0, regex=True)
X_std = StandardScaler().fit_transform(df1)
############################################################
'''
Now we have our dataset in the following format --- 
title              avtar   gravity interstellar movie 21
userID                                              
1			 	 0.469112  0.135632  0.119209  0.104569
2 				 0.282863  0.212112  0.044236  0.494929
3 				 1.509059  0.173215  0.861849  0.071804

NOW WE START DOING THE PCA
'''
#1.  Find the covariance matrix
mean_vec = np.mean(X_std, axis=0)
cov_mat = (X_std - mean_vec).T.dot((X_std - mean_vec)) / (X_std.shape[0]-1)
#2.  Perform eigendecomposition on covariance matrix
eig_vals, eig_vecs = np.linalg.eig(cov_mat)
#3.  Selecting Principal Components
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]
s# # 4.  Create a Projection Matrix
# '''
#  The construction of the projection matrix that will be used to transform the ratings data 
#  onto the new feature subspace.  It is basically just a matrix of our concatenated top k eigenvectors.
# '''
# # matrix_w = np.hstack((eig_pairs[0][1].reshape(4,1),
# #                       eig_pairs[1][1].reshape(4,1)))
# # print('Matrix W:\n', matrix_w)

# # 5. Projecting onto a new Feature Space
# # Y = X_std.dot(matrix_w)




