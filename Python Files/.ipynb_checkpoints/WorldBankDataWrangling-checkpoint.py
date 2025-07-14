# By: Ryan Gallagher 
# World Happiness and Economic Indicators Explorer
# World Bank Indicators Data Wrangling

# Library importing and management. 
import pandas as pd 
from functools import reduce

# Load World Bank Indicator datasets. 
wb_indicators = [
    pd.read_csv(r'C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/World Bank Data/IT.NET.USER.ZS/IT.NET.USER.ZS.csv', encoding='utf-8-sig', skiprows=4),
    pd.read_csv(r'C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/World Bank Data/NY.GDP.PCAP.CD/NY.GDP.PCAP.CD.csv', encoding='utf-8-sig', skiprows=4),
    pd.read_csv(r'C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/World Bank Data/SE.XPD.TOTL.GD.ZS/SE.XPD.TOTL.GD.ZS.csv', encoding='utf-8-sig', skiprows=4),
    pd.read_csv(r'C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/World Bank Data/SH.XPD.CHEX.GD.ZS/SH.XPD.CHEX.GD.ZS.csv', encoding='utf-8-sig', skiprows=4),
    pd.read_csv(r'C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/World Bank Data/SL.UEM.TOTL.ZS/SL.UEM.TOTL.ZS.csv', encoding='utf-8-sig', skiprows=4),
    pd.read_csv(r'C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/World Bank Data/SP.DYN.LE00.IN/SP.DYN.LE00.IN.csv', encoding = 'utf-8-sig', skiprows = 4), 
    pd.read_csv(r'C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/World Bank Data/SP.URB.TOTL.IN.ZS/SP.URB.TOTL.IN.ZS.csv', encoding = 'utf-8-sig', skiprows = 4)   
]

# Rename World Bank Indicator datasets from their indicator code to a more descriptive title. 
wb_indicators[0].rename(columns = {'IT.NET.USER.ZS' : 'Internet Users (% of Population)'}, inplace = True)
wb_indicators[1].rename(columns = {'NY.GDP.PCAP.CD' : 'GDP Per Capita'}, inplace = True)
wb_indicators[2].rename(columns = {'SE.XPD.TOTL.GD.ZS' : 'Education Expenditure (% of GDP)'}, inplace = True)
wb_indicators[3].rename(columns = {'SH.XPD.CHEX.GD.ZS' : 'Healthcare Expenditure (% of GDP'}, inplace = True)
wb_indicators[4].rename(columns = {'SL.UEM.TOTL.ZS' : 'Unemployment Rate'}, inplace = True)
wb_indicators[5].rename(columns = {'SP.DYN.L00.IN' : 'Life Expectancy'}, inplace = True)
wb_indicators[6].rename(columns = {'SP.URB.TOTL.IN.ZS' : 'Population in Urban Areas (% of Population)'}, inplace = True)

# Missing values handling in wb_indicators datasets. Here, missing values are merely replaced with "0," as done in the World Happiness datasets
for df in wb_indicators:
    df.fillna(0, inplace = True)  

# Declare a set of concise indicator names to avoid suffix conflicts when merging. 
wb_indicator_names = ['Internet Users', 'GDP', 'Education Expenditure', 'Healthcare Expenditure', 'Unemployment Rate', 'Life Expectancy', 'Population in Urban Areas'] 

# Concatenate indicator names before years to avoid suffix errors when merging files. Use an underscore to keep formatting consistent with World Happiness dataset.
for df, name in zip(wb_indicators, wb_indicator_names):
    year_cols = df.columns[-4:] 
    new_year_cols = [f'{name}_{year}' for year in year_cols]  
    df.rename(columns = dict(zip(year_cols, new_year_cols)), inplace = True)

# Drops irrelevant columns before merging to further avoid suffix errors when merging files.
for i in range(len(wb_indicators)):
    df = wb_indicators[i]
    year_cols = df.columns[-4:]  
    wb_indicators[i] = df[['Country Name'] + list(year_cols)]

# Merge the World Happiness data and save the merged dataset as a CSV file. 
wb_merged_data = reduce(lambda left, right: pd.merge(left, right, on='Country Name', how = 'outer'), wb_indicators)
wb_merged_data.to_csv('merged_wb_data.csv', index = False)
