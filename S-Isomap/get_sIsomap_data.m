clear;
clc;
%% ��������
load('C:\#�о����׶�#\CEI\xgboost\20190617\dataset\trainlable.mat')
train_label = train;
load('C:\#�о����׶�#\CEI\xgboost\20190617\dataset\testlable.mat')
test_label = test;
load('C:\#�о����׶�#\CEI\xgboost\20190617\dataset\train.mat')
train_data = train;
load('C:\#�о����׶�#\CEI\xgboost\20190617\dataset\test.mat')
test_data = test;
%% ��ά
alpha = 0.5;
K = 10;
% load data.mat
D=distance(train_data, train_label, alpha);
options.dims = 5;
[Y, R, E] = IsomapII(D, 'k', K, options); 
Dtrain_data = train_data * Y.coords{1, 1}';
Dtest_data  = test_data  * Y.coords{1, 1}';

save('sIsomap_Data.mat','Dtrain_data','Dtest_data','train_label','test_label');