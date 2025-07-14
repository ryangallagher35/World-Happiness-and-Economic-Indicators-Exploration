# Ryan Gallagher
# World Happiness and Economic Indicators Explorer
# Correlation Heatmap

# Library importing and management/
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

# Import master dataset.
data = pd.read_csv("C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/Merged CSV Datasets/master_data.csv")

### Construct correlation heatmaps for each year to further quantify relationships between features and World Happiness Score. 
years = [2020, 2021, 2022, 2023] 

output_path = "C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/Python Graphical Output/Correlation Heatmaps.pdf" 
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
            f'Population in Urban Areas_{year}',
            f'Happiness score_{year}'
        ]
        
        data_subset = data[features].dropna()
        
        # Compute correlation matrix
        corr_matrix = data_subset.corr()
        
        # Plot heatmap
        plt.figure(figsize = (12, 10))
        sns.heatmap(corr_matrix, annot = True, cmap = 'coolwarm', center = 0, fmt = ".2f", square = True, linewidths = 0.5)
        plt.title(f'Correlation Heatmap ({year})', fontsize = 16)
        plt.xticks(rotation = 70, fontsize = 9)
        plt.yticks(rotation = 0)
        plt.tight_layout()
        pdf.savefig() 
        plt.close()
