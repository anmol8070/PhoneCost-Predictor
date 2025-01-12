import pandas as pd 
import numpy as np 
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df=pd.read_csv('train.csv')
df2=df.drop(['blue','dual_sim','m_dep','mobile_wt','sc_h','sc_w','three_g','wifi','touch_screen','talk_time'],axis=1)
x=df2.drop('price_range',axis=1)
y=df2['price_range']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=123,stratify=y)
knn=KNeighborsClassifier(n_neighbors=8)

knn.fit(x_train,y_train)

y_test_pred1 = knn.predict(x_test)
y_train_pred1=knn.predict(x_train)

knn_acc=accuracy_score(y_test_pred1,y_test)

# print("Train Set Accuracy:"+str(accuracy_score(y_train_pred1,y_train)*100))
# print("Test Set Accuracy:"+str(accuracy_score(y_test_pred1,y_test)*100))
# print("\nConfusion Matrix:\n%s"%confusion_matrix(y_test_pred1,y_test))
# print("\nClassification Report:\n%s"%classification_report(y_test_pred1,y_test))

# 842	0	2.2	0	1	0	7	0.6	188	2	...	20	756	2549	9	7	19	0	0	1	
# custom_data = np.array([842,0,2.2,0,1,0,7,0.6,188,2,2,20,756,2549,9,7,19,0,0,1,1])


import pickle
with open('model.pkl','wb') as f:
    pickle.dump(knn,f)
#predictions = knn.predict_price(custom_data)

#print("f.pridiction is {predictions}")