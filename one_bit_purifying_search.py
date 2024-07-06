#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def one_bit_purifying_search(X_train, X_test, y_train, y_test, S, optimal_sol):
    
    from fitness_calculation import calculate_error_rate as error
    from dominance_check import dominance_check_between_two_points as dc
    
    import random
    N=len(S)
    random.seed(30)
    ref = random.sample(range (0, N), 1)
    ref=ref[0]
    print(ref)
    
    
    X_ref = S[ref]
    
    
    n = len(X_ref)
    
    
    
    for i in range(n):
        random.seed(30)
        u1 = random.sample(range(0, n), 1)
        u1 = u1[0]
        if X_ref [u1]==1:
            break
        else:
            continue
        print (u1)

    for i in range(n):
        random.seed(30)
        u2 = random.sample(range(0, n), 1)
        u2 = u2[0]
        if X_ref[u2] ==0:
            break
        else:
            continue
        print(u2)

    #Step 3: Judge the relative importance between the two feature bits u 1 and u 2;
    X_ref_by_making_u1_equals_0 = X_ref.copy()
    X_ref_by_making_u1_equals_0[u1] = 0
    if(sum(X_ref_by_making_u1_equals_0)==0):
        X_ref_by_making_u1_equals_0 = X_ref.copy()
    print(X_ref_by_making_u1_equals_0)
    
    X_ref_by_making_u1_0_and_u2_equals_1 = X_ref_by_making_u1_equals_0.copy()
    X_ref_by_making_u1_0_and_u2_equals_1[u2]=1 
    print(X_ref_by_making_u1_0_and_u2_equals_1)
    
    
    X_ref, num_feature_ref, err_ref = error(dataset_train=X_train, target_train =  y_train, dataset_test = X_test, target_test = y_test, X_rn = X_ref)
    X_u1, num_feature_u1, err_u1 = error(dataset_train =X_train, target_train = y_train, dataset_test = X_test, target_test = y_test, X_rn = X_ref_by_making_u1_equals_0) 
    X_u2, num_feature_u2, err_u2 = error(dataset_train =X_train, target_train = y_train, dataset_test = X_test, target_test = y_test, X_rn = X_ref_by_making_u1_0_and_u2_equals_1)
    
    temp1 = err_u1 - err_ref
    temp2 = err_u1 - err_u2
    print(temp1)
    print (temp2)
    print(temp1 - temp2)
    
    X_h = optimal_sol
    X_h_hat = X_h.copy()
    
    if(abs(err_u1 - err_ref) > abs(err_u1 - err_u2)):
        X_ref1 = X_ref.copy()
        #This is within if condition, as this will execute only when u1 is ing than u2
        #Step 4: For an optimal solution, thest, do
        if(X_h[u1] == 1 and X_h[u2]==1):
            X_hat[u2] = 0
        elif(X_h[u1] == 0 and X_h[u2] == 0):
            X_h_hat[u1]=1
        elif(X_h[u1] == 1 and X_h[u2] == 0 ):
            X_h_hat[u1]=0
        else:
            X_h_hat[u1] = 1
            X_h_hat[u2] = 0
            
    X_h, num_feature_h, err_h = error(dataset_train = X_train, target_train = y_train, dataset_test = X_test, target_test = y_test, X_rn = X_h)
    X_h_hat, num_feature_h_hat, err_h_hat  = error(dataset_train = X_train, target_train = y_train, dataset_test= X_test, target_test = y_test, X_rn = X_h_hat)
    
    hhat_dominates_h, h_dominates_hhat, h_and_hhat_are_nondominating = dc(point1=[num_feature_h, err_h], point2=[num_feature_h_hat, err_h_hat]) 
    #print(err_h)
    #print(err_h_hat)
    #print(hhat_dominates_h, h_dominates_hhat, h_and_hhat_are_nondominating)
    
    if(hhat_dominates_h): #focusses on both objective
        #if(err_h_hat < err_h): #Instead of 2 objective, here we focusses just on error nate
        print("population Pt saves Xhhat to replace Xh") 
        to_go_to_next_gen = [X_h_hat] + [num_feature_h_hat, err_h_hat]
        
    elif (h_dominates_hhat): #Focusses on both objective
        #elif(err_h < err_h_hat): #Instead of 2 objective, here we focusses just on error rate
        print("population keeps X h unchanged")
        to_go_to_next_gen = [X_h] + [num_feature_h, err_h]
    else:
        print("it saves both Xh and Xhhat into Pt")
        to_go_to_next_gen = [[X_h] + [num_feature_h, err_h], [X_h_hat]+[num_feature_h_hat, err_h_hat]]
    print("to_go_to_next_gen to_go_to_next_gen")
    print(to_go_to_next_gen)
    return to_go_to_next_gen
#Step 5: If the size of Pt is Longer than N, remove | Pt-Nindividuals with high ranks, and reduce the crowfing distances frot using the method in Section 5.3 
#Step 6 Output population F

