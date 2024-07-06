#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fast_non_dominated_sort(data):
    #create a List to hold the fronts
    fronts = []
    fronts_= []
    #create a list to hold the domination counts for each data point
    domination_counts = [0] * len(data)
    #create a List to hold the domination Lists for each data point
    domination_lists =[[] for _ in range(len(data))] 
    #create a list to hold the ranks of each data point
    ranks = [0]*len(data)
    #Loop over each data point
    for i in range(len(data)):
        #Loop over each data point after i
        for j in range(i+1, len(data)):
            #compare the two data points
            if data[i][0] <= data[j][0] and data[i][1] <= data[j][1]: 
                domination_counts[j] += 1
                domination_lists[i].append(j)
            elif data[i][0] >= data[j][0] and data[i][1]>= data[j][1]:
                domination_counts[i] += 1 
                domination_lists[j].append(i)
    #create a List of points with domination count 0
    S =[i for i in range(len(data)) if domination_counts[i]==0]
    S_= [data[i] for i in range(len(data)) if domination_counts[i] == 0]
    #create the first front 
    fronts.append(S)
    #print(data)
    #print(s)
    fronts_.append(S_)
    #Loop until the s List is empty
    while S:
        Q =[]
        Q_=[]
        #Loop over each data point in s
        for i in S:
            # set the rank of the data point
            ranks[i] = len(fronts)
            #Loop over each dominated data point
            for j in domination_lists[i]:
                domination_counts[j] -= 1
                if domination_counts[j]==0:
                    Q.append(j)
                    Q_.append(data[j])
        #add the next front to the fronts List
        fronts.append(Q) 
        fronts_.append(Q_)
        #sets to the next front 
        S = Q
    #return the fronts
    return fronts, fronts_


# In[]:


#NON DOMINATED SORTING STARTS
def dominance_check_between_two_points (point1, point2):
    
    import numpy as np
    import math
    import collections
    import bisect
    
    CP=point1
    FP=point2
    #print (CP)
    #print(point)
    
    CP_dominates_FP=False
    FP_dominates_CP=False
    CP_and_FP_are_nondominating = False
    
    
    for i in range(len(CP)):
        if(CP[i]<=FP[i]):
            CP_better_than_or_equal_FP =True
            continue
        else:
            CP_better_than_or_equal_FP = False
            break
    
    if (CP_better_than_or_equal_FP==True):
        for i in range(len(CP)):
            if(CP[i]==FP[i]):
                continue
            else:
                CP_dominates_FP =True
    
    #################################
    for i in range(len(CP)):
        if(FP[i]<=CP[i]):
            FP_better_than_or_equal_CP = True
            continue
        else:
            FP_better_than_or_equal_CP = False
            break
            
    if (FP_better_than_or_equal_CP == True):
        for i in range(len(CP)):
            if(FP[i] == CP[i]):
                continue
            else:
                FP_dominates_CP =True
    
    if(CP_dominates_FP == False and FP_dominates_CP == False):
        CP_and_FP_are_nondominating = True
    
    #print("CP_dominates_FP+ str(CP_dominates_FP)) 
    #print("FP dominates_CP:"+str(FP_dominates_CP)),
    #print("CP_and_FP_are_nondominating:" + str(CP_and_FP_are_nondominating))
    
    return FP_dominates_CP, CP_dominates_FP, CP_and_FP_are_nondominating

#For insert in sorted List
def insert(list, n):
    import bisect
    bisect. insort(list, n)
    return list

def non_dominated_sorting(Input_list_to_be_sorted):
    
    import numpy as np
    import math
    import collections
    import bisect
    
    Input_list = Input_list_to_be_sorted 
    M = len(Input_list[0])
    #print (M)
    Input_array = np.array(Input_list)
    
    #for first paint of population P 
    first_point_of_population = Input_array[0]
    
    #Initialize the "Front keys List" with first key 
    Front_keys_list = [1]
    
    #Initialize the Dictinory "D" for first point.
    D = {Front_keys_list[0]:[list(first_point_of_population)]}
    #D[Front_keys_list[@]:[first_point_of_population))
    
    Counter=0
    for point in Input_array[1:]:
        print("Current point under consideration")
        #print(point)
        
        CP = point.copy()
        current_point_assigned_flag=False
        
        #Largest value in Front Reys_List max(Front_keys_list) 
        #smallest value in Front keys List = min(Front beys List)
        
        Highest_key_dominated_by_CP = max(Front_keys_list)+1 
        Highest_key_dominating_to_CP= min(Front_keys_list)-1
        
        #for key in Front keys_list[::-1]: 
        for key in Front_keys_list[:]:
            if (key < Highest_key_dominated_by_CP and key > Highest_key_dominating_to_CP):
                j=len(D[key])
                if(current_point_assigned_flag==False): 
                    #for point in D[key][::-1]:
                    for point in D[key][:]:
                        if(current_point_assigned_flag==False):
                            
                            #j = len(D[key]) 
                            #Last_index=j-1
                            Len_of_front = Len(D[key])
                            print(j)
                            
                            while ( j > 0 and current_point_assigned_flag==False):
                                
                                #Highest_key_dominated_by_CP = min(Front_keys_List)-1
                                #Highest_key_dominating_to_CP= max(Front_keys_List)+1
                                result_of_dominance_check = dominance_check_between_two_points(point1=CP, point2=point)
                                Counter += 1
                                
                                if (result_of_dominance_check[0]==True): #FP_dominates_CP 
                                    Highest_key_dominated_by_CP = Highest_key_dominated_by_CP 
                                    Highest_key_dominating_to_CP= max(key, Highest_key_dominating_to_CP) 
                                    #Break for Loop and jump to the next key
                                    j = -1 #This condition will Break the while loop during next comparison
                                    
                                elif (result_of_dominance_check[1] == True): #CP_dominates_FP
                                    Highest_key_dominated_by_CP = min(key, Highest_key_dominated_by_CP) 
                                    Highest_key_dominating_to_CP= Highest_key_dominating_to_CP
                                    #Break for loop and jump to the next key
                                    j = -1 #This condition will Break the while loop during next comparison

                                elif (result_of_dominance_check[2]==True): #CP_and_FP_are_nondominating 
                                    #check with next point from current front
                                    if(j==1):
                                        D[key].append(list(CP))
                                        current_point_assigned_flag=True
                                j = j-1
                                        
        if (current_point_assigned_flag == False):
            if (Highest_key_dominated_by_CP > max(Front_keys_list)):
                new_key = max(Front_keys_list)+1
                #Front_keys_list.append(new_key)
                Front_keys_list = insert(Front_keys_list, new_key)
                D[new_key] = [list(CP)]
                #D[new_key] = [CP]
                current_point_assigned_flag = True
                
                #Largest_value_in_Front_keys_List = max(Front_keys_List) 
                #smallest_value_in_Front_keys_List= min(Front_teys List)
                
            elif (Highest_key_dominating_to_CP < min(Front_keys_list)):
                new_key = min(Front_keys_list)-1
                #Front_keys_list.append(new_key)
                Front_keys_list = insert(Front_keys_list, new_key)
                D[new_key] = [list(CP)]
                #[new_key] = [CP]
                current_point_assigned_flag=True
                
                #Largest value_in_Front_keys_List max(Front_keys_list)
                #smallest value_in_Front_keys_List min(Front_keys_List)
                
            else:
                new_key = (Highest_key_dominated_by_CP + Highest_key_dominating_to_CP) / 2
                #Front_keys_list.append(new_key) 
                Front_keys_list = insert(Front_keys_list, new_key)
                D[new_key] = [list(CP)]
                #D[new_key] = [CP]
                current_point_assigned_flag = True
                
                #Largest_value_in_Front_keys_List = max(Front_keys_List)
                #Smollest_value_in_Front_keys_list = min(Front_keys_list)

    od = collections.OrdereDict(sorted(D.items()))
    #od
    
    smallest_key = min(Front_keys_list)
    
    #print(D)
    #print(od)
    return od, smallest_key


# In[]:


def inert(list, n):
    import bisect 
    bisect.insort(list, n)
    return list


#In[]:


def non_dominated_sorting (Input_list_to_be_sorted):
    
    import numpy as np
    import math
    import collections
    import bisect
    
    Input_list = Input_list_to_be_sorted
    M = len(Input_list[0]) 
    #print(M) 
    Input_array = np.array(Input_list)
    
    #for first point of population P 
    first_point_of_population = Input_array[0]
    
    #Initialize the List "Front_keys_List" with first key 
    Front_keys_list = [1]
    
    #Initialize the Dictinery "D" for first point. 
    D = {Front_keys_list[0]:[list(first_point_of_population)]}
    #D = {Front_keys_List[0]:[first_point_of_population)}
    
    Counter = 0
    for point in Input_array[1:]:
        #print("Current point under consideration")
        #print (point)
        
        CP = point.copy()
        current_point_assigned_flag = False
        
        #Largest_value_in_Front_keys_List = max(Front_keys_List) 
        #smallest_value_in_Front_keys_List = min(Front_keys List)
        
        Highest_key_dominated_by_CP = max(Front_keys_list)+1 
        Highest_key_dominating_to_CP= min(Front_keys_list)- 1
        
        #for key in Front_keys_list[::-1]:
        for key in Front_keys_list[:]:
            if(key < Highest_key_dominated_by_CP and key > Highest_key_dominating_to_CP):
                j = len(D[key])
                if (current_point_assigned_flag == False):
                    #for point in D[key][::-1]:
                    for point in D[key][:]:
                        if(current_point_assigned_flag == False):
                            
                            #j = len(D(key))
                            #last_index=j-1
                            #len_of_front =  len(D[key])
                            #print(j)
                            
                            while(j > 0 and current_point_assigned_flag == False):
                                
                                #highest key dominated by CP min (Front Reys_list)- 1
                                #nighest key dominating_to_CPmax(Front Reys_list)
                                result_of_dominance_check = dominance_check_between_two_points(point1=CP, point2=point)
                                Counter += 1
                                
                                if (result_of_dominance_check[0] == True): #FP_dominates_CP
                                    Highest_key_dominated_by_CP = Highest_key_dominated_by_CP
                                    Highest_key_dominating_to_CP = max(key, Highest_key_dominating_to_CP)
                                    #Break for Loop and jump to the next key 
                                    j = -1 #This condition will great the while loop during next comparison
                                    
                                elif (result_of_dominance_check[1]==True): #CP_dominates_FP 
                                    Highest_key_dominated_by_CP = min(key, Highest_key_dominated_by_CP) 
                                    Highest_key_dominating_to_CP = Highest_key_dominating_to_CP
                                    #Break for Loop and jump to the next key
                                    j = -1 #This condition will Break the while loop during next compart.son
                                    
                                elif (result_of_dominance_check[2]==True): #CP_and_FP_are_nondominating
                                    #check with next point from current front 
                                    if(j==1):
                                        D[key].append(list(CP))
                                        current_point_assigned_flag=True
                                j = j-1

        if(current_point_assigned_flag==False):
            if (Highest_key_dominated_by_CP > max(Front_keys_list)):
                new_key = max(Front_keys_list)+1
                #Front_keys_list.append(new_key)
                Front_keys_list = insert(Front_keys_list, new_key)
                D[new_key] = [list(CP)]
                #D[new_key] = [CP)
                current_point_assigned_flag = True 
                
                #Longest_value_in_Front_keys_list =  max(Front keys_list)
                #smallest_value_in_Front_keys_list = min(Front_keys_list)

            elif (Highest_key_dominating_to_CP < min(Front_keys_list)):
                new_key = min (Front_keys_list)-1
                #Front_keys_List.append(new key)
                Front_keys_list = insert(Front_keys_list, new_key)
                D[new_key] = [list(CP)]
                #D[new_key] = [CP]
                current_point_assigned_flag = True
                
                #Largest_value_in_ Front_keys_list = max(Front_keys_list)
                #smallest_value_in_Front_keys_list = min(Front_keys_list)
            
            else:
                new_key = (Highest_key_dominated_by_CP + Highest_key_dominating_to_CP) / 2
                #Front_keys_list.append(new_key)
                Front_keys_list = insert(Front_keys_list, new_key)
                D[new_key] = [list(CP)]
                #D[new key] = [CP]
                current_point_assigned_flag =True
                
                #Largest_value_in_Front_heys_list = max(Front_keys_List)
                #Smallest_value_in_Front_keys_List = min(Front_keys_list)
                
    od = collections.OrderedDict(sorted(D.items()))
    #od
    
    smallest_key = min(Front_keys_list)
    
    #print(D)
    #print(od)
    return od, smallest_key

