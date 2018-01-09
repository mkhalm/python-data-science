import pandas as pd
import morestats as m

df=pd.read_csv('supplies.csv')

#add a new column called total=units*unit price
df['TotalPrice']= df['Units']* df['Unit Price']

#show the mean and the sum for each rep per region
 sales=df.groupby(['Region', 'Rep'])['TotalPrice'].agg(['mean', 'sum'])

 #total sales per Region
 regions=df.groupby(['Region'])['TotalPrice'].agg(['sum']).reset_index()
 reps=df.groupby(['Region'])['Rep'].unique().to_frame().reset_index()
 merged = reps.merge(regions, on='Region').set_index('Region')
 merged['count'] = merged.apply(lambda row: len(row['Rep']), axis=1)
 merged['normalized']=merged['sum']/merged['count']
