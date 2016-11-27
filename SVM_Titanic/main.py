import numpy as np
import pandas as pd
import csv
from sklearn.svm import SVC

def loadData(trainfile='train.csv',testfile='test.csv'):
    tr=pd.read_csv(trainfile)
    test=pd.read_csv(testfile)
    return (tr,test)

def writeout(pred,testid,y_test,filename,header=["ID","predicted", "actual"]):
    # save out to .csv
    f = open(filename,'w')
    csvf=csv.writer(f)
    csvf.writerow(header)
    csvf.writerows(zip(testid,pred,y_test))
    f.close()
    
def mungeData(DF):
    # make binary male (1) and female (0)
    DF['Sex']=(DF.Sex=='male')
    DF.Pclass=(DF.Pclass-1)/2 #
    DF=DF.drop(['Name','Fare','Cabin','Ticket',
        'PassengerId','Age','Embarked'],axis=1)
    return DF

trdata,testdata= loadData()
testid = np.array(testdata.PassengerId)
trdata=mungeData(trdata)
testdata=mungeData(testdata)
testc = [0.05, 0.1, 0.3, 0.6, 1, 3, 5, 10 ]
testg = [0, 0.01, 0.05, 0.1, 0.5, 1, 1.5]
k=1
g=0.25
while k<=1:
    nvals = len(trdata)
    splitind=np.floor(nvals*0.5)
    nparams = len(testc)*len(testg)
    scores = np.zeros(nparams) #array([ 0.,  0.,  0.,  0.,  0.])
    counter=0
    paramholder=np.zeros([nparams,2]) #array([[ 0.],[ 0.]])
    # randomize trainingset and split to train and CV set
    rp = np.random.permutation(nvals)
    survt=np.array(trdata.iloc[rp[0:splitind],0])
    survcv=np.array(trdata.iloc[rp[splitind:nvals],0])
        
    tset = trdata.iloc[rp[0:splitind],1:]
    cvset = trdata.iloc[rp[splitind:nvals],1:]
    bestscore=-1
    for c in testc:
        for g in testg:
            #SVC(C=1.0, kernel='rbf', degree=3, gamma='auto', coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=-1, decision_function_shape=None, random_state=None)
            model=SVC(C=c,gamma=g,kernel='poly')
            model=model.fit(tset,survt)
            try:
                scorei=model.score(cvset,survcv)
            except:
                scorei=0 # something went wrong...
            scores[counter]=scorei
            paramholder[counter,0]=c
            paramholder[counter,1]=g
            if scorei>bestscore:
                bestscore=scorei
                bestmodel=model
            counter+=1
            print('Score = %f with c: %f, g: %f' %(scorei,c,g))
    bestc=paramholder[scores.argmax(),0]
    bestg=paramholder[scores.argmax(),1]
    print('Best score of %f with c: %f, g: %f' %(bestscore,bestc,bestg))
    k+=1
    g=g+0.25
model = bestmodel
preds = model.predict(testdata)
preds=(preds>0)*1 # predictions are -1 and 1, so make 0 and 1

##########################################################################


test_data = pd.read_csv("svmmodel_test.csv")
gender_model = pd.read_csv("gendermodel.csv")
predicted = np.array(test_data.predicted)
from sklearn.metrics import precision_recall_fscore_support as score
y_test = np.array(gender_model.Survived)
writeout(preds,testid,y_test,'svmmodel_test.csv')
precision, recall, fscore, support = score(y_test, predicted, average='binary')
print('precision: {}'.format(precision))
print('recall: {}'.format(recall))
print('fscore: {}'.format(fscore))
print('support: {}'.format(support))
#########################################################################
from sklearn import metrics
import matplotlib.pyplot as plt
fpr, tpr, _ = metrics.roc_curve(y_test, predicted)
x = fpr
y = tpr
plt.plot(x,y)
plt.show() 
auc = np.trapz(y,x)
print(auc)
