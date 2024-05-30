import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

data=pd.read_csv(r"/content/heart.csv")
data.head(20)
print(data.describe())
data.corr()
figure = plt.figure(figsize=(12, 12))
sns.heatmap(data.corr(), annot=True)
plt.show()
for column in data:
  plt.figure()
  data.boxplot([column])
num_var=['age','trtbps','chol','thalachh','oldpeak']
cat_var=['sex','cp','fbs','restecg','exng','slp','caa','thall','output']
num_axis_name=['Age of Patient', 'Resting Blood Pressure', 'Cholestrol', 'Maximum Heart Rate Achieved', 'ST Depression']
cat_axis_name=['Gender', 'Chest Pain', 'Fasting Blood Sugar', 'Resting ECG', 'Exercise Induced Angina', 'Slope of ST Segment', 'No. of Major Vessels', 'Thal', 'Target']

for i, j in list(zip(num_var, num_axis_name)):
  plt.figure()
  sns.distplot(data[i], hist_kws=dict(linewidth=1, edgecolor='red'),bins=20)
  plt.title(i)
  plt.xlabel(j)
  plt.ylabel('Density')
  plt.show()

for i, j in list(zip(cat_var, cat_axis_name)):
  fig, ax=plt.subplots(figsize=(10,8))
  obs_value=list(data[i].value_counts().index)
  total_obs_value=list(data[i].value_counts())
  ax.pie(total_obs_value, labels=obs_value, autopct='%1.1f%%', startangle=110, labeldistance=1.1)
  ax.axis('equal')
  plt.title(j)
  plt.legend()
  plt.show()
num_var.append('output')

for i, j in list(zip(num_var, num_axis_name)):
    graph = sns.FacetGrid(data[num_var], hue = 'output', height = 5, xlim = ((data[i].min() - 10), (data[i].max() + 10)))
    graph.map(sns.kdeplot, i, shade = True)
    graph.add_legend()
    plt.title(i)
    plt.xlabel(j)
    plt.ylabel("Density")
    plt.tight_layout()
    plt.show()

num_var.remove('output')
graph = sns.pairplot(data[num_var], diag_kind = "kde")
graph.map_lower(sns.kdeplot, levels = 4, color = ".2")
plt.show()
data_copy=data.copy()
x=data_copy.drop('output', axis=1)
y=data_copy[['output']]
x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2, random_state=3)
x_train.head()
y_train.head()

log_req=LogisticRegression()
log_req.fit(x_train,y_train)
y_pred=log_req.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
print('LogisticRegression Test Accuracy:', accuracy_score(y_test,y_pred))
print("Cross-Validation Accuracy Scores:", cross_val_score(log_req, x_test, y_test, cv=10).mean())

dec_tree=DecisionTreeClassifier(random_state=5)
dec_tree.fit(x_train,y_train)
y_pred=dec_tree.predict(x_test)
print('DecisionTreeClassifier Test Accuracy:', accuracy_score(y_test,y_pred))
print("Cross-Validation Accuracy Scores:", cross_val_score(dec_tree, x_test, y_test, cv=10).mean())

svc_model=SVC(random_state=5)
svc_model.fit(x_train,y_train)
y_pred=svc_model.predict(x_test)
print('SVC Test Accuracy:', accuracy_score(y_test,y_pred))
print("Cross-Validation Accuracy Scores:", cross_val_score(svc_model, x_test, y_test, cv=10).mean())

random_forest=RandomForestClassifier(random_state=5)
random_forest.fit(x_train,y_train)
y_pred=random_forest.predict(x_test)
print('RandomForestClassifier Test Accuracy:', accuracy_score(y_test,y_pred))
print("Cross-Validation Accuracy Scores:", cross_val_score(random_forest, x_test, y_test, cv=10).mean())

gauss_model=GaussianNB()
gauss_model.fit(x_train,y_train)
y_pred=gauss_model.predict(x_test)
print('GaussianNB Test Accuracy:', accuracy_score(y_test,y_pred))
print('Cross-Validation Accuracy Scores:', cross_val_score(gauss_model, x_test, y_test, cv=10).mean())


