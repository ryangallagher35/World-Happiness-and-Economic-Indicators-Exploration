# By: Ryan Gallagher 
# World Happiness and Economic Indicators Explorer
# World Happiness Data Wrangling

# Library importing and management. 
import pandas as pd 
from functools import reduce

# Load World Happiness datasets and rename the "Country" column to enable merging with World Data CSV files. 
happiness_2023 = pd.read_csv(r'C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/World Happiness Data/World Happiness Data 2023.csv')
happiness_2023.rename(columns = {'Country name' : 'Country Name'}, inplace = True) 
happiness_2022 = pd.read_csv(r'C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/World Happiness Data/World Happiness Data 2022.csv')
happiness_2022.rename(columns = {'Country' : 'Country Name'}, inplace = True) 
happiness_2021 = pd.read_csv(r'C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/World Happiness Data/World Happiness Data 2021.csv')
happiness_2021.rename(columns = {'Country name' : 'Country Name'}, inplace = True) 
happiness_2020 = pd.read_csv(r'C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/World Happiness Data/World Happiness Data 2020.csv')
happiness_2020.rename(columns = {'Country name' : 'Country Name'}, inplace = True) 
happiness_datasets = [happiness_2020, happiness_2021, happiness_2022, happiness_2023]

# Merge the World Happiness data and save the merged dataset as a CSV file. 
happiness_merged_data = reduce(lambda left, right: pd.merge(left, right, on ='Country Name', how='outer'), happiness_datasets)
happiness_merged_data.to_csv('merged_happiness_data.csv', index = False)
