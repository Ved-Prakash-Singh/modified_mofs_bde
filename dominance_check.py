#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#NON DOMINATED SORTING STARTS
def dominance_check_between_two_points (point1, point2):
    
    import numpy as np
    import math
    import collections
    import bisect

    CP = point1
    FP = point2
    #print (CP)
    #print(point)
    
    CP_dominates_FP=False
    FP_dominates_CP=False
    CP_and_FP_are_nondominating = False
    
    
    for i in range(len(CP)):
        if(CP[i]<=FP[1]):
            CP_better_than_or_equal_FP =TrUP
            continue
        else:
            CP_better_than_or_equal_FP = False
            break
            
    if (CP_better_than_or_equal_FP == True): 
        for i in range(len(CP)):
            if(CP[i]==FP[i]):
                continue
            else:
                CP_dominates_FP = True

    #####################################
    for i in range (len(CP)):
        if(FP[i]<=CP[i]):
            FP_better_than_or_equal_CP = True
            continue
        else:
            FP_better_than_or_equal_CP = False
            break

    if (FP_better_than_or_equal_CP == True):
        for i in range(len(CP)):
            if( FP[i] ==CP[i]):
                continue
            else:
                FP_dominates_CP = True
    
    if(CP_dominates_FP == False and FP_dominates_CP==False):
        CP_and_FP_are_nondominating = True

    #print( "CP_dominates_FP+ str(CP_dominates_FP))
    #print("FP_dominates_CP:" + str(FP_dominates_CP)) 
    #print("CP_and_FP_are_nondominating: str(CP_and_FP_are_nondominating))

    return FP_dominates_CP, CP_dominates_FP, CP_and_FP_are_nondominating


# #For insert in sorted List

# def insert(list, n):

# import bisect

# bisect. insort(list, n)

# return list

# def non dominated_sorting(Input_list_to_be_sorted):

# import numpy as np.

# import math

# import collections

# import bisect

# Input list Input_list_to_be_sorted Mlen(Input list[e])

# #print(1)

# Input array np.array(Input_list)

# #For first point of population P

# first point_of_population Input array[e]

# #Initialize the List "Front Reys_list" with first key Front_keys_list[1]

# #Initio Lize the Dictinory "o" for first point.

# D=(Front keys_list[@]: [list(first_point_of_population)]} #DefFront_keys_List[e]: [first_point_of population])

# Counter-e

# for point in Input_array[1:]:

# print("Current point under consideration")

# aprint(point)

# CP point.copy()

# current point_assigned_flag False

# #Largest_value in_Front_keys_list max(Front keys_list)

# #smallest value in Front keys Listein (Front Reys_list)

# Highest key dominated_by_CPmax(Front_keys_list)-1 Highest kry dominating to_CP min(Front keys list) 1

# #for key in Front_keys_list[::2]

# for key in Front_keys list[:]:

# if (key Highest_key dominated_by_CP and key Highest_key_dominating to_CP): 1-len(D[key])

# if(current_point_assigned_flag-False): for point in D[key][::-1]:

# for point in D[key][:]:

# if(current_point_assigned_flag-False):

# jlen(D[key])

# #Last Index)-1

# #len of front Len(D[key])

# print()

# while ( 1 > e and current point_assigned_flag-False):

# erighest key dominated_by_CP= min(Front_keys_(1st)-1 wHighest_key_dominating_to_CP max(Front keys_list)+1 result_of_dominance_check dominance_check_between_two_points(pointi-CP, point2-point) Counter 1

# if (result of_dominance_check[e].True)(PCF Highest key dominated by CP Highest_key dominated

# Highest key dominating to by CP max(key, Highest_key_dominating to_)

# #Bresh for Loop and jump to the next by

# JITES condition will break the while loop during next comparison

# elif (result of_dominance_check[1] True): CP dominates F

# Highest key dominated by CP min(key, Highest_key dominated by_)

# Highest key dominating to_CP Highest_key_dominating to_CP

# #great for Love and jump to the next y

# 3--1 #This condition will areak the while loop during next comparison

# elif (result_of_dominance_check(2) True): #CP_and_FP_are_nondorinating

# #check with next point from current front

# if(1-1):

# D[key].append(list (CP))

# f = f - 1

# current point assigned_flag-True

# if(current point_assigned_flag=False):

# if (Highest key dominated by CP max(Front_keys_list)):

# new key max(Front_keys_list)+1

# #Front beys_List.append(nes_key)

# Front keys-list-insert(Front_keys_list, new_key)

# D[new key] (list(CP)]

# #[new_key][P]

# current point assigned_flag-True

# #Largest value_in_Front_keys_List = max(Front_keys_List) #smallest value_in_Front_keys_List min(Front_keys_list)

# elif (Highest key dominating_to_CP < min (Front_keys_list))

# new key min (Front_keys_list)-1

# #Front keys List.append(new_key)

# Front_keys_list-insert(Front_keys_list, new_key)

# D[new_key] [list(CP)]

# #[new_key] = [CP]

# current_point_assigned_flag-True

# #Largest value_in_Front_keys_List = max(Front_keys_List)

# esmallest value_in_Front_keys_List = min(Front_keys_List)

# else:

# new key (Highest_key_dominated_by_CP Highest_key_dominating_to_CP)/2

# #Front_keys_List.append(new_key)

# Front keys_list-insert(Front_keys_list, new key)

# D[new_key] [list(CP)]

# #[new_key] = [\mathcal{F}] current point_assigned_flag-True

# #Largest_value_in_Front_keys_List max(Front_keys_List)

# #smallest value in Front Reys_List min(Front_keys_list)

# od

# collections.OrderedDict(sorted(D.items()))

# #od

# smallest key min (Front_keys_list)

# #print(0)

# #print(od)

# return od, smallest_key
