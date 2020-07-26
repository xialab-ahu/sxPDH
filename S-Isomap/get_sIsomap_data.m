clear;
clc;
%% 导入数据
load('C:\#研究生阶段#\CEI\xgboost\20190617\dataset\trainlable.mat')
train_label = train;
load('C:\#研究生阶段#\CEI\xgboost\20190617\dataset\testlable.mat')
test_label = test;
load('C:\#研究生阶段#\CEI\xgboost\20190617\dataset\train.mat')
train_data = train;
load('C:\#研究生阶段#\CEI\xgboost\20190617\dataset\test.mat')
test_data = test;
%% 降维
alpha = 0.5;
K = 10;
% load data.mat
D=distance(train_data, train_label, alpha);
options.dims = 5;
[Y, R, E] = IsomapII(D, 'k', K, options); 
Dtrain_data = train_data * Y.coords{1, 1}';
Dtest_data  = test_data  * Y.coords{1, 1}';

save('sIsomap_Data.mat','Dtrain_data','Dtest_data','train_label','test_label');