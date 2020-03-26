#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


train_vals = pd.read_csv('train_vals.csv')
train_labels = pd.read_csv('train_labels.csv')
test_vals = pd.read_csv('test_vals.csv')


# In[3]:


train_labels['status_group']=train_labels['status_group'].map({'functional': 1,'non functional': 0,'functional needs repair': 2})


# In[4]:


train_labels.dropna()


# In[5]:


train_vals['target']= train_labels['status_group']


# In[6]:


train_vals


# In[7]:


train_vals = train_vals.drop(['funder','installer','wpt_name'],1)


# In[8]:


train_vals.dropna()


# In[9]:


sns.countplot(train_vals['basin'])
plt.xticks(rotation=90)


train_vals['basin'] = train_vals['basin'].map({'Lake Nyasa': 0,
                                     'Lake Victoria': 1,
                                     'Pangani': 2,
                                     'Ruvuma / Southern Coast': 3,
                                     'Internal': 4,
                                     'Lake Tanganyika': 5,
                                     'Wami / Ruvu': 6,
                                     'Rufiji': 7,
                                     'Lake Rukwa': 8})


# In[10]:


train_vals['date_recorded'] = pd.to_datetime(train_vals['date_recorded'])


# In[11]:


train_vals['year'] = train_vals['date_recorded'].dt.year
train_vals['month'] = train_vals['date_recorded'].dt.month
train_vals['day'] = train_vals['date_recorded'].dt.day


# In[12]:


train_vals = train_vals.drop(['date_recorded'],1)


# In[13]:


train_vals


# In[14]:


sns.countplot(train_vals.region)
plt.xticks(rotation=90)


# In[15]:


sns.lineplot(train_vals['amount_tsh'],train_vals['target'])


# In[16]:


df_soft = train_vals.sort_values(by="target", ascending=False)


# In[17]:


df_soft.head(3)


# In[18]:


sns.countplot(df_soft[:5]['quantity_group'])


# In[19]:


sns.countplot(df_soft[:5]['source'])
plt.xticks(rotation=90)


# In[20]:


sns.countplot(df_soft[:5]['region'])
plt.xticks(rotation=90)


# In[21]:


train_vals = train_vals.drop(['subvillage','region'],1)


# In[22]:


train_vals = train_vals.drop(['lga'],1)


# In[23]:


train_vals = train_vals.drop(['ward'],1)


# In[24]:


sns.countplot(train_vals['quantity_group'])
train_vals['quantity_group'] = train_vals['quantity_group'].map({'enough':0,
                                                                'insufficient':1,
                                                                'dry':2,
                                                                'seasonal':3,
                                                                'unknown':4})


# In[25]:


train_vals['source'] = train_vals['source'].map({'spring':0,
                                                'rainwater harvesting':1,
                                                'dam':2,
                                                'machine dbh':3,
                                                'other':4,
                                                'shallow well':5,
                                                'river':6,
                                                'hand dtw':7,
                                                'lake':8,
                                                'unknown':9})


# In[26]:


sns.countplot(train_vals['source_type'])
plt.xticks(rotation=90)
train_vals['source_type'] = train_vals['source_type'].map({'spring':0,
                                                'rainwater harvesting':1,
                                                'dam':2,
                                                'borehole':3,
                                                'other':4,
                                                'shallow well':5,
                                                'river/lake':6})


# In[27]:


sns.countplot(train_vals['source_class'])
train_vals['source_class'] = train_vals['source_class'].map({'groundwater':0,
                                                'surface':1,
                                                'unknown':2})


# In[28]:


sns.countplot(train_vals['waterpoint_type'])

plt.xticks(rotation=90)


# In[29]:


train_vals['waterpoint_type'] = train_vals['waterpoint_type'].map({'communal standpipe':0,
                                                'communal standpipe multiple': 1,
                                                'hand pump':2,
                                                'other':3,
                                                'improved sping':4,
                                                'cattle trough': 5,
                                                'dam':6})


# In[30]:


sns.countplot(train_vals['waterpoint_type_group'])
plt.xticks(rotation=90)
train_vals['waterpoint_type_group'] = train_vals['waterpoint_type_group'].map({'communal standpipe':0,
                                                'communal standpipe multiple': 1,
                                                'hand pump':2,
                                                'other':3,
                                                'improved sping':4,
                                                'cattle trough': 5,
                                                'dam':6})


# In[31]:


sns.countplot(train_vals['extraction_type'])
plt.xticks(rotation=90)

cols= list(dict(train_vals['extraction_type'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
train_vals['extraction_type'] = train_vals['extraction_type'].map(val_dict)


# In[32]:


cols= list(dict(train_vals['extraction_type_group'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
train_vals['extraction_type_group'] = train_vals['extraction_type_group'].map(val_dict)


# In[33]:


cols= list(dict(train_vals['extraction_type_class'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
train_vals['extraction_type_class'] = train_vals['extraction_type_class'].map(val_dict)


# In[34]:


cols= list(dict(train_vals['management'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
train_vals['management'] = train_vals['management'].map(val_dict)


# In[35]:



cols= list(dict(train_vals['management_group'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
train_vals['management_group'] = train_vals['management_group'].map(val_dict)


# In[36]:


cols= list(dict(train_vals['payment'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
train_vals['payment'] = train_vals['payment'].map(val_dict)


# In[37]:


cols= list(dict(train_vals['payment_type'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
train_vals['payment_type'] = train_vals['payment_type'].map(val_dict)


# In[38]:



cols= list(dict(train_vals['water_quality'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
train_vals['water_quality'] = train_vals['water_quality'].map(val_dict)


# In[39]:



cols= list(dict(train_vals['quality_group'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
train_vals['quality_group'] = train_vals['quality_group'].map(val_dict)


# In[40]:



cols= list(dict(train_vals['quantity'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
train_vals['quantity'] = train_vals['quantity'].map(val_dict)


# In[41]:



cols= list(dict(train_vals['public_meeting'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
train_vals['public_meeting'] = train_vals['public_meeting'].map(val_dict)


# In[42]:



cols= list(dict(train_vals['recorded_by'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
train_vals['recorded_by'] = train_vals['recorded_by'].map(val_dict)


# In[43]:



cols= list(dict(train_vals['scheme_management'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
train_vals['scheme_management'] = train_vals['scheme_management'].map(val_dict)


# In[44]:



cols= list(dict(train_vals['scheme_name'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
train_vals['scheme_name'] = train_vals['scheme_name'].map(val_dict)


# In[45]:



cols= list(dict(train_vals['permit'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
train_vals['permit'] = train_vals['permit'].map(val_dict)


# In[46]:


train_vals.dtypes


# In[75]:


X = train_vals.drop(['target'],1)
y= train_vals.target


# In[78]:


X.dtypes


# In[48]:


X = np.array(X)


# In[49]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)


# In[84]:


def Stacking(model,train,y,test,n_fold,params):
    folds=StratifiedKFold(n_splits=n_fold,random_state=1)
    
    test_pred=np.empty((test.shape[0],1),float)
    
    train_pred=np.empty((0,1),float)
    
    for train_indices,val_indices in folds.split(train,y):
        x_train,x_val=train.iloc[train_indices],train.iloc[val_indices]
        y_train,y_val=y.iloc[train_indices],y.iloc[val_indices]

        
        trained_model = train(np.array(x_train),np.array(y_train),params,model)
        
        
        
        pras = []
        for i in trained_model.predict(x_val):
            pras.append(np.argmax(i))
            
        pras2 = []
        for i in trained_model.predict(test):
            pras2.append(np.argmax(i))
            
        train_pred=np.append(train_pred,pras)
        test_pred=np.append(test_pred,pras2)
    return test_pred.reshape(-1,1),train_pred

def train_xgb(x,y,params,model):
    
    gbd = model.train(params,dtrain,100)
    return gbd
    


# In[85]:


from sklearn.model_selection import StratifiedKFold
import xgboost as xgb


xgb_params = {
    
    'objective': 'multi:softprob',
    'num_class': 3,
    'scaleposweight':1,
    'seed':27,
    'regalpha':0.01,
    'max_depth': 4,
    'eval_metric': 'mlogloss'

}

test_pred1 ,train_pred1=Stacking(model=xgb_model,n_fold=10, train=X,test=X_test,y=y,params=xgb_params)

train_pred1=pd.DataFrame(train_pred1)
test_pred1=pd.DataFrame(test_pred1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[51]:


preds =xgb_model.predict(dtest)


# In[52]:


pra = []
for i in preds:
    pra.append(np.argmax(i))


# In[53]:


np.mean(pra==y_test)


# In[151]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)


# In[65]:


import lightgbm as lgb
params = {
    'objective': 'multiclass',
    'num_class': 3,
    'metric': 'multi_error',
    'boosting': 'gbdt',
    'num_iterations': 1000,
    'learning_rate': 0.01,
    'num_leaves': 24,
    'max_bin': 500,
    'num_estimators': 100
    
}
lgb_model = lgb.LGBMModel(**params).fit(X_train,y_train)


# In[67]:





# In[55]:


import lightgbm as lgb
dtrain = lgb.Dataset(X_train,y_train)
dtest = lgb.Dataset(X_test,y_test)




model = lgb.train(params,dtrain,valid_sets=dtest,num_boost_round=10)


# In[56]:


from sklearn.metrics import roc_auc_score
preds = model.predict(X_test)
predictions=  []
for i in preds:
    predictions.append(np.argmax(i))


# In[80]:


predictions


# In[57]:


np.mean(y_test == predictions)


# In[58]:


final_preds = (np.array(pra) + np.array(predictions)) / 2
final_preds


# In[69]:


from sklearn.ensemble import VotingClassifier
model = VotingClassifier(estimators=[('lgb', lgb_model), ('xgb', xgb_model)], voting='hard')
model.fit(X_train,y_train)
model.score(X_test,y_test)


# In[70]:


model.predict(X_test)


# In[73]:


test_vals = test_vals.drop(['funder','installer','wpt_name'],1)
test_vals.dropna()
test_vals['basin'] = test_vals['basin'].map({'Lake Nyasa': 0,
                                     'Lake Victoria': 1,
                                     'Pangani': 2,
                                     'Ruvuma / Southern Coast': 3,
                                     'Internal': 4,
                                     'Lake Tanganyika': 5,
                                     'Wami / Ruvu': 6,
                                     'Rufiji': 7,
                                     'Lake Rukwa': 8})
test_vals['date_recorded'] = pd.to_datetime(test_vals['date_recorded'])
test_vals['year'] = test_vals['date_recorded'].dt.year
test_vals['month'] = test_vals['date_recorded'].dt.month
test_vals['day'] = test_vals['date_recorded'].dt.day
test_vals = test_vals.drop(['date_recorded'],1)
test_vals = test_vals.drop(['subvillage','region'],1)
test_vals = test_vals.drop(['lga'],1)
test_vals = test_vals.drop(['ward'],1)
test_vals['quantity_group'] = test_vals['quantity_group'].map({'enough':0,
                                                                'insufficient':1,
                                                                'dry':2,
                                                                'seasonal':3,
                                                                'unknown':4})
test_vals['source'] = test_vals['source'].map({'spring':0,
                                                'rainwater harvesting':1,
                                                'dam':2,
                                                'machine dbh':3,
                                                'other':4,
                                                'shallow well':5,
                                                'river':6,
                                                'hand dtw':7,
                                                'lake':8,
                                                'unknown':9})
test_vals['source_type'] = test_vals['source_type'].map({'spring':0,
                                                'rainwater harvesting':1,
                                                'dam':2,
                                                'borehole':3,
                                                'other':4,
                                                'shallow well':5,
                                                'river/lake':6})
test_vals['source_class'] = test_vals['source_class'].map({'groundwater':0,
                                                'surface':1,
                                                'unknown':2})
test_vals['waterpoint_type'] = test_vals['waterpoint_type'].map({'communal standpipe':0,
                                                'communal standpipe multiple': 1,
                                                'hand pump':2,
                                                'other':3,
                                                'improved sping':4,
                                                'cattle trough': 5,
                                                'dam':6})
test_vals['waterpoint_type_group'] = test_vals['waterpoint_type_group'].map({'communal standpipe':0,
                                                'communal standpipe multiple': 1,
                                                'hand pump':2,
                                                'other':3,
                                                'improved sping':4,
                                                'cattle trough': 5,
                                                'dam':6})
cols= list(dict(test_vals['extraction_type'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
test_vals['extraction_type'] = test_vals['extraction_type'].map(val_dict)
cols= list(dict(test_vals['extraction_type_group'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
test_vals['extraction_type_group'] = test_vals['extraction_type_group'].map(val_dict)
cols= list(dict(test_vals['extraction_type_class'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
test_vals['extraction_type_class'] = test_vals['extraction_type_class'].map(val_dict)
cols= list(dict(test_vals['management'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
test_vals['management'] = test_vals['management'].map(val_dict)

cols= list(dict(test_vals['management_group'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
test_vals['management_group'] = test_vals['management_group'].map(val_dict)
cols= list(dict(test_vals['payment'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
test_vals['payment'] = test_vals['payment'].map(val_dict)
cols= list(dict(test_vals['payment_type'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
test_vals['payment_type'] = test_vals['payment_type'].map(val_dict)

cols= list(dict(test_vals['water_quality'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
test_vals['water_quality'] = test_vals['water_quality'].map(val_dict)

cols= list(dict(test_vals['quality_group'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
test_vals['quality_group'] = test_vals['quality_group'].map(val_dict)

cols= list(dict(test_vals['quantity'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
test_vals['quantity'] = test_vals['quantity'].map(val_dict)

cols= list(dict(test_vals['public_meeting'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
test_vals['public_meeting'] = test_vals['public_meeting'].map(val_dict)

cols= list(dict(test_vals['recorded_by'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
test_vals['recorded_by'] = test_vals['recorded_by'].map(val_dict)

cols= list(dict(test_vals['scheme_management'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
test_vals['scheme_management'] = test_vals['scheme_management'].map(val_dict)

cols= list(dict(test_vals['scheme_name'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
test_vals['scheme_name'] = test_vals['scheme_name'].map(val_dict)

cols= list(dict(test_vals['permit'].value_counts()).keys())
vals= []
for i in range(len(cols)):
    vals.append(i)
val_dict = dict((key,val) for key,val in zip(cols,vals))
test_vals['permit'] = test_vals['permit'].map(val_dict)


# In[161]:


final_tests = xgb.DMatrix(test_vals)


# In[162]:


pri = xgb_model.predict(final_tests)
xgb_preds = []
for i in pri:
    xgb_preds.append(np.argmax(i))
    


# In[ ]:





# In[74]:


preds= model.predict(test_vals)


# In[75]:


res = []
for i in preds:
    res.append(np.argmax(i))


# In[165]:


new_xgb = []
for i in xgb_preds:
    if i == 1:
        new_xgb.append("functional")
    elif i == 2:
        new_xgb.append("functional needs repair")
    else:
        new_xgb.append("non functional")


# In[76]:


new_res = []
for i in res:
    if i == 1:
        new_res.append("functional")
    elif i == 2:
        new_res.append("functional needs repair")
    else:
        new_res.append("non functional")


# In[166]:


res_dict= pd.DataFrame({'id':test_vals['id'],'status_group':new_xgb})
res_dict.to_csv('submission.csv',index=False)


# In[ ]:




