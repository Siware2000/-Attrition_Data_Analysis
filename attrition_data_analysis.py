# -*- coding: utf-8 -*-
"""Attrition_Data_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-LQ9wTWwxjbP8sHlPfDQXjvrAcmEZ-b6
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

df = pd.read_csv("Attrition_data.csv")
df.head()

df.columns

df.info()

df.shape

df.describe()

df.isna().sum()

df = df.dropna()

# count of Attrition

attrition = pd.DataFrame(df["Attrition"].value_counts())
attrition

plt.pie(attrition["Attrition"],labels = ["No","Yes"], explode = [0.2,0],autopct = "%1.1f%%")
plt.show()

df["Gender"].value_counts().plot(kind = "pie",autopct = "%1.1f%%",labels = None, figsize = (10,6))
plt.legend(labels = ["Male","Female"],loc = "upper right")

df.columns

df["Department"].value_counts().plot(kind = "pie",figsize =(20,6),autopct = "%1.1f%%",startangle = 90,shadow = True,labels = None)
plt.legend(labels = df["Department"].unique(), loc = "lower right")

rating_features = ["JobSatisfaction","EnvironmentSatisfaction","JobInvolvement","PerformanceRating"]
wk_exp = ["YearsAtCompany","YearsSinceLastPromotion","YearsWithCurrManager","TotalWorkingYears"]

c=0
fig = plt.figure(figsize=(15,8))
label = "low","medium","high","very_high"

for i in rating_features:
    ax = plt.subplot(2, 2, c + 1)
    df[i].astype(str).value_counts().plot(kind = "pie",autopct ="%1.1f%%",labels = None)
    ax.set_title("Rating given to"+" "+i+"\n"+"by employees")
    fig.legend(labels = label,loc = "center")
    c= c+1
#     # code here
# plt.show()

js = df.groupby("JobSatisfaction")["Attrition"].value_counts(normalize = True).unstack()
js.plot(kind = "bar", stacked = "False")

bus_trv = df.groupby("BusinessTravel")["Attrition"].value_counts(normalize = True).unstack()
bus_trv.plot(kind = "bar", stacked = "False")

we =df[wk_exp]
we.head()

yac = df.groupby("YearsAtCompany")["Attrition"].value_counts(normalize = False).unstack()
yac.plot(kind = "bar", stacked = "False", figsize = (10,6))

yslp = df.groupby("YearsSinceLastPromotion")["Attrition"].value_counts(normalize = False).unstack()
yslp.plot(kind = "bar", stacked = "False", figsize = (10,6))

ywcm = df.groupby("YearsWithCurrManager")["Attrition"].value_counts(normalize = False).unstack()
ywcm.plot(kind = "bar", stacked = "False", figsize = (10,6))

df["Department"].value_counts()



plt.figure(figsize = (12,5))
sns.countplot(x = "Age", hue= "Attrition", data = df)

plt.figure(figsize = (10,8))
sns.heatmap(df.corr(),annot = True)