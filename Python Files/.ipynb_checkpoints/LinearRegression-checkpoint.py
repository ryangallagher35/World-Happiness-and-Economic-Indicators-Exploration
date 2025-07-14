# Ryan Gallagher 
# World Happiness and Economic Indicators Explorer 
# Linear Regression 

# Library importing and management.
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Import master dataset.
data = pd.read_csv("C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/Merged CSV Datasets/master_data.csv")

### Construct a linear regression model and store respective metrics, coefficients, and variables. 
years = [2020, 2021, 2022, 2023] 
scaler = StandardScaler() 
csv_rows = [] 

output_path = "C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/Python Graphical Output/Linear Regression Graphs.pdf"
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
    
        data_subset = data[features + [target]].copy() 
        data_subset.dropna(inplace = True) 
        X = data_subset[features] 
        y = data_subset[target] 
        X_scaled = scaler.fit_transform(X) 
    
        # Build and fit the linear regression model.
        lr = LinearRegression()
        lr.fit(X_scaled, y) 
    
        # Predict the Happiness score and evaluate the linear regression model. 
        y_pred = lr.predict(X_scaled) 
        mse = mean_squared_error(y, y_pred) 
        r2 = r2_score(y, y_pred) 
    
        # Store the linear regression mode, slope and intercept coefficients, MSE, and R^2 value. 
        row = {
            "model" : lr, 
            "coefficients" : dict(zip(features, lr.coef_)), 
            "intercept coefficient" : lr.intercept_, 
            "MSE" : mse, 
            "R^2" : r2
        }
    
        for feature, coef in zip(features, lr.coef_): 
            row[feature] = coef 
        csv_rows.append(row)
    
        # Graph an actual vs. predicted scatter plot, reflecting how well the linear regression model predicts happiness score. A perfect model will align along the identity line.
        plt.scatter(y, y_pred) 
        plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--') 
        plt.xlabel("Actual Happiness Score") 
        plt.ylabel("Predicted Happiness Score") 
        plt.title(f"Actual vs. Predicted Happiness: {year}")
        plt.grid(True) 
        pdf.savefig() 
        plt.close() 

results = pd.DataFrame(csv_rows) 
results.to_csv("C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/Python Generated Data/Linear Regression Results.csv", index = False)





    
