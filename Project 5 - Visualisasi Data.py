#!/usr/bin/env python
# coding: utf-8

# Deskripsi: 
#     Visualisasi Data
# Materi yang digunakan :
# 1. Import Module : Pandas
# 2. Import Module : Numpy
# 3. Import Module : Matplotlib
# 4. Import Module : Seaborn

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


Kelompok_5 = pd.read_csv("2017-07_bme280sof.csv")
Kelompok_5.head()


# In[3]:


Kelompok5 = pd.DataFrame(Kelompok_5[Kelompok_5.location.isin([1675, 1931, 2325, 2343])])
Kelompok5.head()


# In[4]:


plt.plot(Kelompok5["temperature"], Kelompok5["humidity"])


# In[5]:


sns.catplot(x="temperature", y="humidity", hue="sensor_id", data=Kelompok5)
plt.show()


# In[6]:


sns.boxplot(x="sensor_id", y="humidity", data=Kelompok5)
plt.show()


# In[ ]:




