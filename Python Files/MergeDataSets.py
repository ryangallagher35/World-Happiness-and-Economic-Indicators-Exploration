# By: Ryan Gallagher 
# World Happiness and Economic Indicators Explorer
# Merge Data Sets

# Library importing and management. 
import pandas as pd 

# Load merged World Happiness data and World Bank Data 
happiness_data = pd.read_csv(r'C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/merged_happiness_data.csv')
world_bank_indicator_data = pd.read_csv('C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/merged_wb_data.csv')

# Merge the two datasets into a final CSV.
master_data = pd.merge(happiness_data, world_bank_indicator_data,on = "Country Name", how = "inner") 
master_data.to_csv('master_data.csv', index = False)
