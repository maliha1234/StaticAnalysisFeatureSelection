clc;
clear all;
close all;

% dim = 300;
% w_star = randi([-10,10],dim-1,1);
% X = randn(1000,dim-1).*randi(12,1000,dim-1);
% Y = X*w_star + 0*randn(1000,1) ;
% X(:,end+1) = -Y;

matrixTable = readtable('CSV_FILE_DIRECTORY + programName + Two_way.csv');
mat = matrixTable(:,11:end);
X= zscore(table2array(mat));

Y = zscore(table2array(matrixTable(:,3)));
X(:,end+1) = -Y;

dim = size(X,2);

L = [0.1 0.1 0.5 0.5 0.7 0.7 1 1 1.2 1.2];%Hyper
Tries = 1;%Hyper
Runs = 5;%Hyper
Dnum = [1.01];%Hyper
Iterations = [1000];%Hyper
best_ws = randn(dim,length(L));

res_L = zeros(length(Dnum),length(L));
res_end = zeros(dim,length(L),length(Dnum));
res_max = zeros(length(Dnum),length(L));

for dn = 1:length(Dnum)
    denum = Dnum(dn);
    for re_run = 1:Runs
        for j = 1:length(L)
            mat_W = zeros(dim,Tries);
            for trys = 1:Tries
                etta = ones(dim,1)./(re_run^1.4);%Hyper
                W = best_ws(:,j);
                W(end) = 1;
                for iter = 1:Iterations(dn)
                    deriv = zeros(dim,1);
                    x_star = find(abs(X*W) == max(abs(X*W)));
                    for i =1:length(x_star)
                        if X(x_star(i),:)*W < 0
                            deriv = deriv - X(x_star(i),:)' ./ length(x_star);
                        elseif X(x_star(i),:)*W >= 0
                            deriv = deriv + X(x_star(i),:)' ./ length(x_star);
                        end
                    end
                    deriv = deriv + L(j)*sign(W);
                    W = W - etta.*deriv;
                    W(end) = 1;
                    etta = etta./(denum);%Hyper
                end
                mat_W(:,trys) = W;
            end
            [~,b_res] = min(max(abs(X*mat_W)));
            best_ws(:,j) = mat_W(:,b_res);
        end
        
    end
    
    res_L(dn,:) = L;
    res_end(:,:,dn) = round(best_ws,3);
    res_max(dn,:) = max(abs(X*best_ws));
end


res_end(:,end+1) = zeros(size(res_end,1),1);
for i = 1:size(res_end,1)-1
    if i<= 5
        res_end(i,end) = i/10;
    elseif i <= 5+57
        res_end(i,end) = i-5;
    else
        res_end(i,end) = floor((i-5-57-1)/5) + 1 + (rem(i-5-57,5)*(rem(i-5-57,5)~=0) +5*(rem(i-5-57,5)==0)) /10;
    end
end

disp('------------------------------num12------------------------------')
res_end(5+57+11*5+1:5+57+11*5+5,:)%n12

disp('------------------------------cat5------------------------------')
res_end(67:5:end,:)%c5 1st

% disp('------------------------------cat1------------------------------')
% res_end(63:5:end,:)%c1 3rd
% disp('------------------------------cat2------------------------------')
% res_end(64:5:end,:)%c2 2nd
% disp('------------------------------cat3------------------------------')
% res_end(65:5:end,:)%c3 4th
% disp('------------------------------cat4------------------------------')
% res_end(66:5:end,:)%c4 5th

%n7
%n12c2
%n12c3