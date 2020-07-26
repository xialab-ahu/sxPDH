# -*- coding: utf-8 -*-
"""
Created on 20190726

"""

import GetData
import My_SVM


if __name__ == "__main__":
    trainData = GetData.trainData
    testData = GetData.testData

    trainSvcScoress1 = []
    featss1 = []
    clfs1 = []
    feasImp=["SPIDER2_hsb_CN","PSSM_T","Eigenvector centrality","PSSM_R","min DPXBound","boundAll polarRE","DISOPRED_Score","dNon-polarABS","SPIDER2_spd_Psi","energy_9","dAll polarABS","s-ch s_avg DPXUnBound","min DPXUnBound","energy_17","PSSM_H","PSSM_E","DSSPTCO","PSSM_A","energy_15","boundTotal-SideABS","PSSM_N","DisEMBLCOILS","PSSM_D","SPIDER2_hsb_HSEu","PSSM_P","energy_12","PSSM_Y","dTotal-SideREL","SPIDER2_spd_Tau(i-2=>i+1)","max DPXUnBound","PSSM_W","PSSM_L","energy_16","s-ch s_avg CXBound","PSSM_C","PSSM_S","boundMain-ChainABS","DSSPALPHA","dAll polarRE","boundAll polarABS","PSSM_G","energy_1","s-ch s_avg CXUnBound","SPIDER2_hsa_CN","s-ch avg DPXUnBound","PSSM_F","PSSM_I","PSSM_M","PSSM_Q","s-ch avg DPXBound","energy_18","dMain-ChainABS","Betweenness","PSSM_V","PSSM_cons","s-ch s_avg DPXBound","PSSM_K","energy_7","energy_10","boundTotal-SideREL","s_avg CXUnBound","energy_0","SPIDER2_hsa_HSEd","Closeness","dMain-ChainREL","min CXUnBound","DSSPKAPPA","boundMain-ChainREL","energy_3","Cluster_Coeff","SPIDER2_hsa_HSEu","max CXBound","energy_19","average DPXBound","DSSPPHI","dTotal-SideABS","HydrophobicityUnBound","max CXUnBound","energy_5","min CXBound","DSSPPSI","DisEMBLHOTLOOPS","energy_14","average CXUnBound","Eccentricity","boundNon-polarABS","SPIDER2_hsb_HSEd","s_avg CXBound","s-ch avg CXBound","dNon-polarREL","energy_11","SPIDER2_spd_Theta(i-1=>i+1)","max DPXBound","DisEMBLREM465","energy_13","NetSurfP_RSA","s-ch avg CXUnBound","energy_8","dAll-atomsABS","boundNon-polarREL","energy_2","energy_6","Degree","s_avg DPXBound","boundAll-atomsREL","Average neighbor degree","energy_4","dAll-atomsREL","s_avg DPXUnBound","average CXBound","boundAll-atomsABS","NetSurfP_ASA","average DPXUnBound","DSSPACC"]
    feats = feasImp[:20]
    train, test = GetData.sc(trainData, testData,feats)
    print ('降维后结构:')
    print (train.shape)
    My_SVM.my_svm(train,test)
