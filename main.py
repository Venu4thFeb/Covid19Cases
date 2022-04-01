import csv;
import pandas as pd;
import datetime ;
import time;



df=pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
nw_dt=df.sort_values(['date','location'],ascending=False).groupby('location',as_index=False).first()
dt=nw_dt[nw_dt['date']!=pd.to_datetime('today').date().strftime(format='%Y-%m-%d')].head(10)
dt.to_csv('./artifact/Top10.csv',sep='\t')

lc = pd.read_csv('./countries.txt')
#new cases, total cases, new vaccinations and total vaccinations
nw_dt=df.sort_values(['date','location'],ascending=False)
for country in lc:
    
    f_dt=nw_dt[nw_dt['location']==country].groupby('location',as_index=True).agg(
    {
         'total_cases':sum, 
         'new_cases': sum,  
         'new_vaccinations': sum,
         'total_vaccinations': sum
    })
    f_dt.to_csv('./artifact/listedCountries'+time.strftime("%Y%m%d-%H%M%S")+'.csv',sep='\t',mode='a', header=False)


