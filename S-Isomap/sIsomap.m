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
% Dtrain_data = train_data * Y.coords{1, 1}';
% Dtest_data  = test_data  * Y.coords{1, 1}';
% %% ʶ��
% [bestacc,bestc,bestg] = SVMcg(train_label,Dtrain_data,-4,4,-4,4,3,0.5,0.5,0.9);
% 
% cmd = ['-t 0''-c ',num2str(bestc), ' -g ', num2str(bestg) ];
% model = libsvmtrain( train_label, Dtrain_data, cmd );
% 
% [predict_label, accuracy, dec_values] = libsvmpredict(test_label, Dtest_data, model);
% 
% %% ����
% TP = 0; % ��Ԥ�����
% FN = 0; % ��Ԥ��ɸ�
% TN = 0; % ��Ԥ��ɸ�
% FP = 0;  % ��Ԥ�����
% for i =1 : 64
%     if test_label(i) == 1 && predict_label(i) == test_label(i)
%         TP = TP + 1;
%     elseif test_label(i) == 1 && predict_label(i) ~= test_label(i)
%         FN = FN + 1;
%     elseif test_label(i) == 0 && predict_label(i) == test_label(i)
%         TN = TN + 1;
%     elseif test_label(i) == 0 && predict_label(i) ~= test_label(i)
%         FP = FP + 1;
%     end
% end
% sen = TP/(TP+FN);
% pre = TP/(TP+FP);
% auc_data=AUC(test_label,predict_label) ;
% fprintf('Sens: %.6f% \n', TP/(TP+FN));   %ֱ���������Ļ��������C���Ե������ʽ  
% fprintf(' Spec: %.6f% \n', TN/(TN+FP) );
% fprintf(' Pre: %.6f% \n', TP/(TP+FP));
% fprintf(' F1: %.6f% \n', 2*sen*pre/(sen+pre) );
% fprintf(' ACC: %.6f% \n', accuracy(1)/100 ); 
% fprintf(' MCC: %.6f% \n', (TP*TN-FP*FN)/(((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))^0.5));
% fprintf(' AUC: %.6f% \n', auc_data );