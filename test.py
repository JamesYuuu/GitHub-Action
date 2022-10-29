import pandas as pd
import pytrends
from pytrends.request import TrendReq
import googletrans
from googletrans import Translator
import os
from time import sleep

os.mkdir("homework")

df_dic = pd.read_excel('HIV-4.xlsx')

#select the words with markers “Econ@” or “ECON”    
df_dic.dropna(how="all",subset=['POLIT','Polit@'],inplace=True) 

#select the words labeled with the “positive” or “negative” tag
df_dic.dropna(how="all",subset=['Positiv','Negativ'],inplace=True)

df_dic = df_dic[['Entry','Positiv',"Negativ"]]
df_words = df_dic['Entry'].str.split('#',expand=True)   
df_dic['Entry'] = df_words.iloc[:,0]                    
df_dic = df_dic.drop_duplicates(subset=["Entry"])      #Delete the words with more than one meaning

df_dic['term'] = 'Chinese '
df_dic['term'] = df_dic['term'].str.cat(df_dic['Entry'])
#df_dic

pytrend = TrendReq()
lst = list(df_dic['term'])
dt = pd.date_range(start="20180107", end="20220930", freq="7D")
py_res = pd.DataFrame(index=dt)
for i in range(len(lst)):
    while True:
        try:
            pytrend.build_payload(kw_list=[lst[i],], timeframe='2018-01-01 2022-09-30', geo = 'US', gprop='') 
            py_current = pytrend.interest_over_time()
            break
        except Exception as e:
            pass
    if not py_current.empty:
        py_res[lst[i]] = py_current[lst[i]]
py_res.to_excel('homework/q1.xlsx')

# df_dic = pd.read_excel('HIV-4.xlsx')

# #select the words with markers “Econ@” or “ECON”    
# df_dic.dropna(how="all",subset=['ECON','Econ@'],inplace=True) 

# #select the words labeled with the “positive” or “negative” tag
# df_dic.dropna(how="all",subset=['Positiv','Negativ'],inplace=True)

# df_dic = df_dic[['Entry','Positiv',"Negativ"]]
# df_words = df_dic['Entry'].str.split('#',expand=True)   
# df_dic['Entry'] = df_words.iloc[:,0]                    
# df_dic = df_dic.drop_duplicates(subset=["Entry"])      #Delete the words with more than one meaning
# #df_dic

# translator = Translator()
# #tranlated = translator.translate('hello.', dest='zh-CN')
# df_dic['Chinese'] = df_dic['Entry'].apply(translator.translate, src='en', dest='zh-cn').apply(getattr, args=('text',))
# #df_dic

# lst = list(df_dic['Chinese'])
# pytrend = TrendReq()
# dt = pd.date_range(start="20180107", end="20200930", freq="7D")
# py_res = pd.DataFrame(index=dt)
# for i in range(len(lst)):
#     while True:
#         try:
#             pytrend.build_payload(kw_list=[lst[i],], timeframe='2018-01-01 2022-09-30', geo = 'US', gprop='') 
#             py_current = pytrend.interest_over_time()
#             break
#         except Exception as e:
#             pass
#     if not py_current.empty:
#         py_res[lst[i]] = py_current[lst[i]]
# py_res.to_excel('homework/q2.xlsx')



