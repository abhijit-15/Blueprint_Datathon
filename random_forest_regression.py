#Random Forest Regression

import pandas as pd
import numpy as np
from pprint import pprint
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def coerce_df_columns_to_numeric(df, column_list):
    #pprint(df.columns.values)
    #pprint(dict(zip(column_list , df[column_list].apply(np.max))))

    df.dropna(axis = 1 , thresh = 2000 , inplace = True)
    df = df.dropna(axis = 0 , thresh = 100)
    #pprint(df.columns.values)
    cols = df.columns.values
    df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')



#Read and preprocess data
data = pd.read_csv('/home/abhijeet/datathon/CHR/final_dataset2.csv',low_memory=False)
#cols = data.columns.values
#print(data.columns.values)
coerce_df_columns_to_numeric(data , data.columns.values)
print(data.dtypes)


#Make inputs, outputs and train, test sets
y = data['drug overdose deaths value']
del data['drug overdose deaths value']
X = data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1) #Make training and testing split

print('Training the model.......')
#Training evaluation
model = RandomForestRegressor(n_estimators=100, oob_score=True, random_state=1)
model.fit(X_train , y_train)
print("AUC - ROC train: ", roc_auc_score(y_train,model.oob_prediction_))

print('Testing the model.......')
#Testing evaluation
y_hat = model.predict(X_test)
print("AUC - ROC test: ", roc_auc_score(y_test,y_hat))
