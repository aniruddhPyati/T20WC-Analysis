#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')


# In[2]:


import pandas as pd
import json


# In[3]:


with open('t20_dataset/t20_wc_match_results.json')as f:
    data=json.load(f)
match_df=pd.DataFrame(data[0]['matchSummary'])
match_df.head()


# In[4]:


match_df.shape


# In[5]:


match_df.rename({'scorecard':'matchID'},axis=1)


# In[6]:


with open('t20_dataset/t20_wc_batting_summary.json')as f:
    data=json.load(f)
data[0]['battingSummary']


# In[7]:


all_records=[]
for i in data:
    all_records.extend(i['battingSummary'])

batting_df=pd.DataFrame(all_records)
batting_df


# In[8]:


batting_df


# In[9]:


batting_df["out/not_out"]=batting_df.dismissal.apply(lambda x: "out" if len(x)>0 else "not out")


# In[10]:


batting_df


# In[11]:


batting_df.drop(columns=["dismissal"],inplace=True)
batting_df


# In[12]:


batting_df.head(11)


# In[13]:


batting_df['batsmanName']=batting_df['batsmanName'].apply(lambda x: x.replace('â€',''))


# In[14]:


batting_df.head(11)


# In[15]:


match_df.head(11)


# In[16]:


match_id_dict={}
for index,row in match_df.iterrows():
    key1= row['team1']+ ' Vs '+ row['team2']
    key2=row['team2']+ ' Vs '+ row['team1']
    match_id_dict[key1] = row["scorecard"]
    match_id_dict[key2] = row["scorecard"]
match_id_dict


# In[17]:


batting_df["match_id"]=batting_df["match"].map(match_id_dict)
batting_df.head(10)


# In[18]:


match_df


# In[37]:


batting_df.to_csv('t20_dataset/batting2_df.csv',index=False)


# In[20]:


with open('t20_dataset/t20_wc_bowling_summary.json')as f:
    data=json.load(f)
data


# In[21]:


data[0]['bowlingSummary']


# In[22]:


all_records=[]
for i in data:
    all_records.extend(i['bowlingSummary'])
all_records


# In[23]:


bowling_df=pd.DataFrame(all_records)


# In[24]:


bowling_df.head(11)


# In[25]:


bowling_df["match_id"]=bowling_df["match"].map(match_id_dict)
bowling_df.head(10)


# In[38]:


bowling_df.to_csv('t20_dataset/bowling2_df.csv',index=False)


# In[27]:


with open('t20_dataset/t20_wc_player_info.json')as f:
    data=json.load(f)
data


# In[28]:


player_df=pd.DataFrame(data)
player_df.head(10)


# In[29]:


player_df['name']=player_df['name'].apply(lambda x: x.replace('â€',''))


# In[30]:


player_df.head(11)


# In[31]:


player_df[player_df.team=="India"]


# In[32]:


player_df.loc[128]


# In[33]:


player_df.at[211,'playingRole']


# In[34]:


player_df


# In[35]:


player_df.to_csv('t20_dataset/player2.csv')


# In[36]:


bowling_df


# In[ ]:




