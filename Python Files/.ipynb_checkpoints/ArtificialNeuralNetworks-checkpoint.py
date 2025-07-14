# Ryan Gallagher 
# World Happiness and Economic Indicators Explorer 
# Artificial Neural Networks 

# Library importing and management.
from sklearn.neural_network import MLPRegressor 
from sklearn.metrics import mean_absolute_error 
from sklearn.preprocessing import StandardScaler 
import pandas as pd
import matplotlib.pyplot as plt

# Import master dataset.
data = pd.read_csv("C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/Merged CSV Datasets/master_data.csv")

### Build an artificial neural network for each year to predict the Happiness Score using Happiness and World Bank Economic Indicator features . Then compare the predictions with the actual values to determine the accuracy of the models. 
years = [2020, 2021, 2022, 2023] 
results = {} 
all_predictions = []

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

    data_subset = data[['Country Name'] + features + [target]].dropna() 
    X = data_subset[features] 
    y = data_subset[target] 

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Build and train the artificial neural network. 
    ann = MLPRegressor(hidden_layer_sizes = (64, 32), max_iter = 1000, random_state = 42) 
    ann.fit(X_scaled, y) 

    # Use the artificial neural network to make predictions regarding the accuracy score and evaluate the model by comparing the predicted and actual values. 
    predictions = ann.predict(X_scaled)
    mae = mean_absolute_error(y, predictions) 
    results[year] = mae 

    # Construct dataframe to be appended and stored as a CSV. 
    prediction_data = pd.DataFrame({
        'Country Name' : data_subset['Country Name'].values,
        'Year' : year, 
        'Actual' : y.values, 
        'Predicted' : predictions, 
        'Absolute Error' : abs(y.values - predictions) 
    })

    prediction_data['MAE'] = mae 
    all_predictions.append(prediction_data)

# Combine and export predictions and metrics to a CSV. 
all_data = pd.concat(all_predictions, ignore_index = True) 
all_data.to_csv("C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/Python Generated Data/ANN_Predictions.csv")

# Graph the mean absolute errors each year to measure the effectiveness of the artificial neural network models. 
plt.figure(figsize = (8, 5)) 
plt.bar(results.keys(), results.values(), color = 'skyblue') 
plt.xticks(ticks = years, labels = [str(year) for year in years])
plt.xlabel('Year') 
plt.ylabel('Mean Absolute Error') 
plt.title('ANN Prediction Error by Year') 
plt.grid(axis = 'y') 
plt.tight_layout()
plt.savefig("C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/Python Graphical Output/ANN_Error_Graph.pdf")
plt.show() 
    

