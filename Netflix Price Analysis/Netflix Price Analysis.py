#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


# In[6]:


df=pd.read_csv('Netflix Subscription Fee.csv')


# In[48]:


df.shape


# In[7]:


df.head()


# In[8]:


df.tail()


# In[9]:


df.describe()


# In[10]:


df.columns


# In[49]:


df.drop(columns=['Country_code'],inplace=True)


# In[50]:


df.isnull().sum()


# In[274]:


cor=df.corr()
sns.heatmap(cor, xticklabels=cor.columns, yticklabels=cor.columns,annot=True,cmap="BuPu")


# In[52]:


sns.pairplot(df)


# In[53]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[64]:


most_shows=df.sort_values(by='No. of TV Shows',ascending=False)[:15]
most_shows.reset_index(drop=True,inplace=True)
most_shows 


# In[169]:


ax1 = most_shows.plot(x="Country", y="No. of TV Shows", kind="bar", ylabel='No. of TV shows',figsize=(12,8), title='Countries with the most TV Shows', color='red', alpha=0.95 ,edgecolor='black',ylim=(0,6000))
ax1.set_facecolor('#F5F5F5')
ax1.set(xlabel=None)


# In[65]:


least_shows=df.sort_values(by='No. of TV Shows',ascending=True)[:15]
least_shows.reset_index(drop=True,inplace=True)
least_shows


# In[170]:


ax2 = least_shows.plot(x="Country", y="No. of TV Shows", kind="bar", ylabel='No. of TV shows',figsize=(12,8), title='Countries with the least TV Shows', color='red', alpha=0.95 ,edgecolor='black',ylim=(0,6000))
ax2.set_facecolor('#F5F5F5')
ax2.set(xlabel=None)


# In[66]:


most_movies=df.sort_values(by='No. of Movies',ascending=False)[:15]
most_movies.reset_index(drop=True,inplace=True)
most_movies


# In[171]:


ax3 = most_movies.plot(x="Country", y="No. of Movies", kind="bar", ylabel='No. of Movies',figsize=(12,8), title='Countries with the most Movies', color='red', alpha=0.95 ,edgecolor='black',ylim=(0,2600))
ax3.set_facecolor('#F5F5F5')
ax3.set(xlabel=None)


# In[67]:


least_movies=df.sort_values(by='No. of Movies',ascending=True)[:15]
least_movies.reset_index(drop=True,inplace=True)
least_movies


# In[173]:


ax4 = least_movies.plot(x="Country", y="No. of Movies", kind="bar", ylabel='No. of Movies',figsize=(12,8), title='Countries with the least Movies', color='red', alpha=0.95 ,edgecolor='black',ylim=(0,2600))
ax4.set_facecolor('#F5F5F5')
ax4.set(xlabel=None)


# In[174]:


least_content=df.sort_values(by='Total Library Size',ascending=True)[:10]
least_content.reset_index(drop=True,inplace=True)
least_content


# In[175]:


most_content=df.sort_values(by='Total Library Size',ascending=False)[:10]
most_content.reset_index(drop=True,inplace=True)
most_content


# In[ ]:


sns.pairplot(
    data=df,
    y_vars=["Total Library Size"],
    x_vars=["Cost Per Month - Basic ($)", "Cost Per Month - Standard ($)", "Cost Per Month - Premium ($)"],
)


# In[75]:


df


# In[ ]:


most_exp=df.sort_values(by=['Cost Per Month - Basic ($)',
       'Cost Per Month - Standard ($)', 'Cost Per Month - Premium ($)'],ascending=False)

pd.set_option('display.max_rows', most_exp.shape[0]+1)
print(most_exp)


# In[266]:


countries=['United Kingdom','India','Singapore','United States','Turkey','Japan','South Korea','France','Switzerland','Norway']
# c=most_exp.set_index('Country')
# cost_graph=c.loc[['United Kingdom','India','Singapore','United States','Turkey','Japan','South Korea']]
# c.loc[countries]
# cost_graph=c.loc[countries]

# cost_graph.reset_index()
# cost_graph.index
cost_graph=most_exp.iloc[[17, 50, 49, 59, 23,2,3,4,43]]
cost_graph


# In[56]:


#Calculating the average cost for each subscription


# In[57]:


basic_mean=df['Cost Per Month - Basic ($)'].mean()
basic_mean


# In[58]:


standard_mean=df['Cost Per Month - Standard ($)'].mean()
standard_mean


# In[116]:


premium_mean=df['Cost Per Month - Premium ($)'].mean()
premium_mean


# In[273]:



ax5 = cost_graph.plot(x='Country', y=['Cost Per Month - Basic ($)',
       'Cost Per Month - Standard ($)', 'Cost Per Month - Premium ($)'], kind="bar", ylabel='Cost in $',figsize=(15,10), title='Subscription Price Comparison', color=['#800016','#407ba7','#ff002b'], alpha=0.95 ,width=0.75,edgecolor='black')
ax5.axhline(y=basic_mean, color="#FF9F1C" ,linestyle='dashed', label="Basic Mean in $", linewidth=2.5)
ax5.axhline(y=standard_mean, color="#000000" ,linestyle='solid', label="Standard Mean in $", linewidth=2)
ax5.axhline(y=premium_mean, color="#582F0E" ,linestyle=':', label="Premium Mean in $", linewidth=3)
ax5.legend(loc = 'lower right')

ax5.set_facecolor('#F5F5F5')
ax5.set(xlabel=None)

