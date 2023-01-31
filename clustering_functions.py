import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


def plot_cluster_inertia_k(train, col1, col2):

#initialize variable to be reference later, taking in arguments for features/columns

    X = train[[col1, col2]]

#scaling
    scaler = MinMaxScaler()
    X= scaler.fit_transform(X)

#fit KMeans algo
    kmeans = KMeans(n_clusters = 3)
    kmeans.fit(X)

#assign predictions to original dataframe
    train['clustering'] = kmeans.predict(X)

#plot cluster predictions, take in argument for column of predictions
    sns.scatterplot(x = train[col1], y = train[col2], hue = train['clustering'])

#plot inertia over k increasing, take in argument for column of predictions
    with plt.style.context('seaborn-whitegrid'):
        plt.figure(figsize=(9, 6))
        pd.Series({k: KMeans(k).fit(X).inertia_ for k in range(2, 12)}).plot(marker='x')
        plt.xticks(range(2, 12))
        plt.xlabel('k')
        plt.ylabel('inertia')
        plt.title('Change in inertia as k increases')
    


#function that creates a new dataframe describing the amount and percentage of missing values for each feature in the given dataframe
def check_missing_values(df):

    cols = ['name', 'num_rows_missing', 'percent_rows_missing']
    df_1 = pd.DataFrame(columns=cols)
    
    for col in list(df.columns):
        num_rows_missing = df[col].isna().sum()
        percent_rows_missing = num_rows_missing / df.shape[0]
        df_2 = pd.DataFrame([{'name': col, 'num_rows_missing': num_rows_missing,
                               'percent_rows_missing': percent_rows_missing}])
        df_1 = pd.concat([df_1, df_2], axis=0)
    
    df_1.set_index('name', inplace=True)    
    return df_1