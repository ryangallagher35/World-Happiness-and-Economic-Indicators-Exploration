# Ryan Gallagher
# World Happiness and Economic Indicators Explorer 
# Random Forests

import os
os.environ["OMP_NUM_THREADS"] = "1"

# Library importing and management.
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
import textwrap

# Import master dataset.
data = pd.read_csv("C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/Merged CSV Datasets/master_data.csv")

### Use Random Forests to determine the importance of each feature's influence on World Happiness Score each year. 
years = [2020, 2021, 2022, 2023]

output_path = "C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/Python Graphical Output/Random Forest Importances.pdf" 
with PdfPages(output_path) as pdf:  
    for year in years: 
    
        # Declare feature and target data. 
        features = [
            f'Logged GDP per capita_{year}', 
            f'Social support_{year}', 
            f'Healthy life expectancy_{year}', 
            f'Freedom to make life choices_{year}', 
            f'Generosity_{year}',
            f'Perceptions of corruption_{year}', 
            f'Internet Users_{year}', 
            f'Education Expenditure_{year}', 
            f'Healthcare Expenditure_{year}', 
            f'Unemployment Rate_{year}', 
            f'Population in Urban Areas_{year}'
        ] 
    
        target = f'Happiness score_{year}'
    
        data_subset = data[features + [target]].dropna() 
        X = data_subset[features] 
        y = data_subset[target] 
    
        # Train the Random Forest for 2023. 
        rf = RandomForestRegressor(n_estimators = 100, random_state = 42) 
        rf.fit(X, y)
    
        # Gather and sort the obtained importances.
        importances = pd.Series(rf.feature_importances_, index = features) 
        importances_sorted = importances.sort_values(ascending = True) 
    
        # Plot the results.
        plt.figure(figsize = (10, 6)) 
        wrapped_labels = [textwrap.fill(label, width = 25) for label in importances_sorted.index]
        importances_sorted.plot(kind = 'barh', title = f'Feature Importance for Happiness Score: {year}')
        plt.yticks(ticks = range(len(wrapped_labels)), labels = wrapped_labels, fontsize = 6)     
        plt.xlabel('Importance')
        plt.tight_layout
        pdf.savefig() 
        plt.close()
