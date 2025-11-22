import pandas as pd 
df=pd.read_csv('AI_Moves_Chatbot/Database/urls_merged.csv')
print(df.columns)
print(type(df['url'].iloc[0]))
#Index(['url', 'description'], dtype='object')
# <class 'str'>