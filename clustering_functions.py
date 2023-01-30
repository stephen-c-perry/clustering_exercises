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
    
