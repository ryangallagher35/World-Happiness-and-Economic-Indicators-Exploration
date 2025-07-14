# World Happiness and Economic Indicators Explorer of the Post-COVID Pandemic Era
_By: Ryan Gallagher_

## Python Component 

### Overview
This project investigates the relationship between world happiness scores and an array of economic and social indicators from 2020 to 2023, the timeframe following the outbreak of the COVID-19 pandmenic. It employs data from the World Happiness Report and the World Bank’s World Development Indicators archive to analyze how indicators such as logged GDP per capita, healthcare expenditure, education expenditure, and internet usage influence national well-being. Such analysis is conducted in Python using a variety of machine learning and statistical techniques. Furthermore, results from such machine learning and statistical measures are stored in corresponding PDF files in the "Python Graphical Output" file of the repository. Moreover, the interactive Tableau story provides an interactive overview of the relationship between world happiness scores and such indicators and the performances of various machine learning models implemented in the study. 

### Data Wrangling
In the data wrangling phase of this study, raw CSV files from the World Happiness Report and the World Bank are read into Pandas dataframes and a consistent structure is applied across all datasets. For the World Bank indicators, column names are standardized and reshaped to avoid naming conflicts during merging. Missing values are replaced with zeros for simplicity. The World Happiness data is similarly cleaned and merged by country name across all four years. Finally, the World Happiness and World Bank Indicator data are merged into a single master dataset to explore using various statistical and machine learning techniques in Pythob. Furthermore. a long-format version of the data is created to employ for Tableau usage. 

### Artificial Neural Networks 
#### Methodology
Artificial Neural Networks are employed to predict the happiness score for each year using the available economic and social indicators. The input features include Logged GDP per capita, social support, life expectancy, freedom of choice, generosity, perception of corruption, internet usage, education and healthcare expenditure, unemployment rate, and urban population percentage (in agglomerations of over 1 million people). The data is standardized before training a Multi-Layer Perceptron with two hidden layers. After training the network, predictions are made and compared against actual happiness scores. The mean absolute error is calculated for each year and the performance trends are visualized in a bar chart to evaluate the model’s effectiveness. Such results can be found in "ANN_Error_Graph.pdf" in the Python Graphical Output file of the repository. 

### Correlation Heatmap
#### Methodology
To explore the strength and direction of relationships between the happiness score and its respective social and economic indicators, a correlation matrix is computed for each year and visualized as a heatmap using  the Seaborn data visualization library. These heatmaps provide a quick glance of the strength of correlation between each indicator and happiness, revealing potential patterns or redundancies in the dataset. These correlation heatmaps can be found in "Correlation Heatmaps.pdf" of the "Python Graphical Input" file of the repository.

### KMeans Clustering and PCA
#### Methodology 
Foremost, the optimal number of clusters is determined for each year using the elbow method, which plots the inertia values (within-cluster sum of squares) across a range of possible cluster counts. Following analysis of the elbow charts, Four clusters are selected as the optimal solution across all years. These elbow charts can be found in "KMeans PCA Elbow Charts.pdf" in the "Python Graphical Input" file of the repository. 

Once clustering is complete, Principal Component Analysis is applied to reduce the dimensionality of the dataset to two principal components, allowing for clear visualizations of the cluster structures. These PCA cluster charts can be found in "KMeans PCA Clusters.pdf" in the "Python Graphical Input" file of the repository. 

### Linear Regression
#### Methodology
Linear regression models are built for each year to quantify the linear impact of each indicator on happiness scores. After standardizing the input data, a model is trained and its coefficients are extracted. Evaluation metrics such as the R-squared value and mean squared error are computed to assess model performance. Furthermore, the predictive capability of these is visualized using scatter plots that compare actual versus predicted happiness scores, thus assessing model accuracy. These scatter plots can be found in "Linear Regression Graphs.pdf" of the "Python Graphical Input" file of the repository. 

### Random Forests
#### Methodology
To capture non-linear relationships and interaction effects among variables, Random Forest regression models are trained for each year. This ensemble learning method aggregates predictions from multiple decision trees and outputs a ranked list of feature importances based on their contribution to reducing error in the model. Furthermore, the importance scores are visualized in horizontal bar plots. These plots can be found in "Random Forest Importances.pdf" in the Python Graphical Output file. 
