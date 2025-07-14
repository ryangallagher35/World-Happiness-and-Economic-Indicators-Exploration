# Ryan Gallagher 
# World Happiness and Economic Indicators Explorer
# Prepare Linear Regression data for Tableau

# Library importing and management. 
import pandas as pd

# Prepare the linear regression data so that it is in a format suitable for Tableau. 
data = [
    {
        "Year": 2020,
        "Intercept": 5.68873853,
        "MSE": 0.229717309,
        "R2": 0.803253987,
        "Logged GDP per capita": 0.295789799,
        "Social support": 0.311612238,
        "Healthy life expectancy": 0.195266093,
        "Freedom to make life choices": 0.134076492,
        "Generosity": 0.011352568,
        "Perceptions of corruption": -0.136539527,
        "Internet Users": -0.021340047,
        "Education Expenditure": 0.121082174,
        "Healthcare Expenditure": 0.077607825,
        "Unemployment Rate": -0.12006121,
        "Population in Urban Areas": 0.003912762
    },
    {
        "Year": 2021,
        "Intercept": 5.716146789,
        "MSE": 0.188264159,
        "R2": 0.831006907,
        "Logged GDP per capita": 0.333210516,
        "Social support": 0.274898836,
        "Healthy life expectancy": 0.148025318,
        "Freedom to make life choices": 0.138176002,
        "Generosity": 0.019081469,
        "Perceptions of corruption": -0.125670511,
        "Internet Users": 0.04545733,
        "Education Expenditure": 0.11555866,
        "Healthcare Expenditure": 0.044853867,
        "Unemployment Rate": -0.120469347,
        "Population in Urban Areas": -0.014359835
    },
    {
        "Year": 2022,
        "Intercept": 5.691449541,
        "MSE": 0.189881283,
        "R2": 0.843809768,
        "Logged GDP per capita": 0.450746756,
        "Social support": 0.371500573,
        "Healthy life expectancy": 0.052597799,
        "Freedom to make life choices": 0.218768656,
        "Generosity": -0.017497711,
        "Perceptions of corruption": 0.105375239,
        "Internet Users": -0.046169849,
        "Education Expenditure": 0.065235272,
        "Healthcare Expenditure": 0.10230176,
        "Unemployment Rate": -0.103382848,
        "Population in Urban Areas": -0.045457448
    },
    {
        "Year": 2023,
        "Intercept": 5.656917431,
        "MSE": 0.177238804,
        "R2": 0.862765484,
        "Logged GDP per capita": 0.361636685,
        "Social support": 0.521409139,
        "Healthy life expectancy": -0.043118007,
        "Freedom to make life choices": 0.198936698,
        "Generosity": -0.061968624,
        "Perceptions of corruption": -0.149897541,
        "Internet Users": 0.033338738,
        "Education Expenditure": -0.03304266,
        "Healthcare Expenditure": 0.046629035,
        "Unemployment Rate": -0.091076675,
        "Population in Urban Areas": -0.009636047
    }
]

df = pd.DataFrame(data)
id_vars = ['Year', 'Intercept', 'MSE', 'R2']
df_long = df.melt(id_vars = id_vars, var_name = 'Variable', value_name = 'Coefficient')
output_file = "C:/Users/rgall/Downloads/World Happiness and Economic Indicators Explorer/Python Generated Data/Linear_Regression_Results_Tableau.csv"
df_long.to_csv(output_file, index = False)