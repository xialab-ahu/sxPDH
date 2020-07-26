# -*- coding: utf-8 -*-
"""
Created on 20190726

"""


from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from copy import deepcopy as dp
import PATH
from scipy.io import loadmat


'''
首先定义数据类
包含：
x - 数据
y - 标签
'''
class CsvData(object):

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self._shape=0
    @property
    def shape(self):
        if self.x.shape[0]==self.y.shape[0]:
            return self.x.shape
        else:
            raise ValueError("The data shape do not match label shape!")
    
    def toCsv(self,fileName,hasLabel=True,indexx=False):
        from copy import deepcopy
        x,y=deepcopy(self.x),deepcopy(self.y)
        x=pd.DataFrame(x)
        if hasLabel==True:
            x["DDG"]=y
        x.to_csv(fileName,index=indexx,sep=",")
       
    @property
    def columns(self):
        return self.x.columns.get_values()

'''
读取CSV文件函数，将读取的CSV文件里的数据实例化成CsvData的类
'''
def readCsv(csvName,mark=[],c=True):
    data=pd.read_csv(csvName).drop(mark,axis=1)
    x=data.drop(["DDG"],axis=1)
    y=data["DDG"].get_values()
    if c:
        y[y>=1]=1
        y[y<1]=0
    else:
        pass
    outData=CsvData(x,y)
    return outData
def ReadMat(matName):
    f = loadmat(matName)
    Dtrain_data = f['Dtrain_data']
    train_label = f['train_label']
    Dtest_data = f['Dtest_data']
    test_label = f['test_label']
    trainData = CsvData(Dtrain_data,train_label)
    testData = CsvData(Dtest_data,test_label)
    return trainData,testData
'''
将数据标准化，需要同时输入CsvData类的两个实例化
'''
def sc(train,test,mark=None):
    train=dp(train) #deepcopy
    test=dp(test)
    if not mark:
        pass
    else:
        train.x=train.x[mark]
        test.x=test.x[mark]
        
    s=StandardScaler().fit(train.x)
    train.x=s.transform(train.x)
    test.x=s.transform(test.x)
#    train.x=train.x.get_values()
#    test.x=test.x.get_values()
    return train,test
'''
np.random.seed(5)

trainfile_dir = PATH.trainfile_dir
testfile_dir = PATH.testfile_dir

trainData=readCsv(trainfile_dir, c=True, mark=["PDBID","CHAIN","REF","POS","ALT"])
testData=readCsv(testfile_dir, c=True, mark=["PDBID","CHAIN","REF","POS","ALT"])
AllFs=trainData.x.columns.get_values().tolist()
'''