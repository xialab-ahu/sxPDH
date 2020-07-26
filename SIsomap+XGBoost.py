# -*- coding: utf-8 -*-
"""
Created on 20190726

"""
import GetData
import MY_XGBoost
import PATH


if __name__ == "__main__":
    trainData, testData = GetData.ReadMat(PATH.SISOMAP_dir)
    # trainData,testData = GetData.sc(trainData,testData) # 标准化
    MY_XGBoost.my_xgboost(trainData, testData) #xgboost