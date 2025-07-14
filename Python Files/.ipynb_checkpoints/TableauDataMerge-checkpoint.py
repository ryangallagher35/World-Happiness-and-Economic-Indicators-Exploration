# Ryan Gallagher 
# World Happiness and Economic Indicators Explorer
# Master File for Tableau

# Library importing and management.
import pandas as pd

# Load the data and rearrange it from long format into a format more suitable for Tableau analysis
data = pd.read_csv('C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/Merged CSV Datasets/master_data.csv')  
master_data_tableau = data.melt(id_vars = ['Country Name'], var_name = 'Indicator_Year', value_name = 'Value')
master_data_tableau[['Indicator', 'Year']] = master_data_tableau['Indicator_Year'].str.rsplit('_', n = 1, expand = True)
master_data_tableau = master_data_tableau[['Country Name', 'Year', 'Indicator', 'Value']]
master_data_tableau.to_csv('C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/Merged CSV Datasets/master_data_tableau.csv', index = False)