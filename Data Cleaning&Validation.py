
# coding: utf-8

# In[122]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
# import seaborn
import seaborn as sns
from sklearn import preprocessing
df = pd.read_csv ('WELLCOME_APCspend2013_forThinkful.csv', encoding='ISO-8859–1')


# In[123]:


df.dtypes


# In[124]:


#replace column name
df.rename(columns={'COST (£) charged to Wellcome (inc VAT when charged)':'cost'}, inplace=True)


# In[125]:


df.head(10)


# In[131]:


df.groupby('Journal title').size().sort_values(ascending=False).head(10)


# In[127]:


# this will replace "PLoS ONE" with "PLoS One" 
# overwriting column with replaced value of column 
df["Journal title"]= df["Journal title"].str.replace("plos one", "PLos One", case = False)
df["Journal title"]= df["Journal title"].str.replace("pnas", "Proceedings of the National Academy of Sciences ", case = False)
display (df.groupby("Journal title").size().sort_values(ascending=False))


# In[105]:


df['cost'] = df.cost.apply(lambda x: x.strip('$'))
df['cost'] = df.cost.apply(lambda x: x.strip('£')).astype(float)


# In[106]:


df.dtypes


# In[130]:


# Create a groupby variable that groups cost per article by Journal title
# overwriting column with replaced value of column 
df["Journal title"]= df["Journal title"].str.replace("acs nano", "ACS Nano", case = False)
df["Journal title"]= df["Journal title"].str.replace(r'(^.*Chemotherapy.*$)', "Antimicrobial Agents and Chemotherapy", case = False)
df["Journal title"]= df["Journal title"].str.replace("pnas", "Acta Crystallographica Section D, Biological Crystallography ", case = False)
df["Journal title"]= df["Journal title"].str.replace("\.", " ", case = False)
df["Journal title"]= df["Journal title"].str.replace("\,", " ", case = False)
df["Journal title"]= df["Journal title"].str.replace("\:", " ", case = False)
df['cost'].groupby(df['Journal title']).describe()

