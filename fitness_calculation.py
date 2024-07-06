#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def calculate_error_rate(dataset_train, target_train, dataset_test, target_test, X_rn):
    from sklearn.model_selection import train_test_split #train test split
    from sklearn.metrics import precision_score, recall_score, confusion_matrix, classification_report, accuracy_score, f1_score, roc_auc_score
    from sklearn.metrics import precision_recall_curve
    from sklearn.metrics import precision_recall_curve
    #import scikit-plot
    ##from scikitolet.metrics import plot_precision_recall as plot_precision_recall_curve
    
    from sklearn.tree import DecisionTreeClassifier


    
    
    
    X_r = X_rn
    data_tr = dataset_train
    
    feature_set = []
    for i in range(len(X_r)):
        #print(i)
        if X_r[i] == 1:
            feature_set.append(data_tr.columns[i])
    #print(feature_set)
    if(len(feature_set)==0):
        num_feature = 0
        f1_score = 0
        error_rate=0
    else:
        X_ = dataset_train[feature_set]
        
        
        
        
        from xgboost import XGBClassifier
        model = XGBClassifier(use_label_encoder = False, eval_metric='mlogloss', random_state=42)
        
        
        X_train = dataset_train[feature_set]
        X_test = dataset_test[feature_set]
        y_train = target_train
        y_test = target_test
        
        
        
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        
        num_feature = len(feature_set)
        f1_score =  f1_score(y_test, y_pred) * -1 #this is to make it einirization problen
        
        
        print("f1 score is" +str(f1_score)) 
        score = accuracy_score(y_test, y_pred)
        accuracy_score = score
        print("accuracy is" +str(score))
        print("error rate is" +str(1-score))
        error_rate = 1-score
        print("roc suc score is" +str(roc_auc_score(y_test, y_pred)))
        print("gini is" +str((2*roc_auc_score(y_test, y_pred)) - 1))
        print(confusion_matrix(y_test, y_pred))
        print(classification_report(y_test, y_pred))

    #print(num_feature)
    #print (f1_score)
    
    #return X_r, num_feature, f1_score
    return X_r, num_feature, error_rate


#In[ ]:


def calculate_f1_score(dataset_train, target_train, dataset_test, target_test, X_rn):
    from sklearn.model_selection import train_test_split #train test split
    from sklearn.metrics import precision_score, recall_score, confusion_matrix, classification_report, accuracy_score, f1_score, roc_auc_score
    from sklearn.metrics import precision_recall_curve
    from sklearn.metrics import precision_recall_curve
    #import scikit-plot
    ##from scikitolet.metrics import plot_precision_recall as plot_precision_recall_curve
    
    from sklearn.tree import DecisionTreeClassifier


    
    
    
    X_r = X_rn
    data_tr = dataset_train
    
    feature_set = []
    for i in range(len(X_r)):
        #print(i)
        if X_r[i] == 1:
            feature_set.append(data_tr.columns[i])
    #print(feature_set)
    if(len(feature_set)==0):
        num_feature = 0
        f1_score = 0
    else:
        X_ = dataset_train[feature_set]
        
        
        
        
        from xgboost import XGBClassifier
        model = XGBClassifier(use_label_encoder = False, eval_metric='mlogloss', random_state=42)
        
        
        X_train = dataset_train[feature_set]
        X_test = dataset_test[feature_set]
        t_rain = target_train
        y_test = target_test
        
        
        
        
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        
        num_feature = len(feature_set)
        f1_score =  f1_score(y_test, y_pred) * -1 #this is to make it einirization problen
        
        
        print("f1 score is" +str(f1_score)) 
        score = accuracy_score(y_test, y_pred)
        accuracy_score = score
        print("accuracy is" +str(score))
        print("error rate is" +str(1-score))
        error_rate = 1-score
        print("roc suc score is" +str(roc_auc_score(y_test, y_pred)))
        print("gini is" +str((2*roc_auc_score(y_test, y_pred)) - 1))
        print(confusion_matrix(y_test, y_pred))
        print(classification_report(y_test, y_pred))

    #print(num_feature)
    #print (f1_score)
    
    return X_r, num_feature, f1_score
    #return X_r, num_feature, error_rate
