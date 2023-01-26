import pandas as pd

def df_described(df):
    df_transposed = pd.DataFrame(df.T.iloc[:,0])
    cols_to_drop = df.shape[:0]
    df_transposed = df_transposed.drop(columns = df_transposed[: , - cols_to_drop])
    df_transposed['0'] = df.isnull().sum(axis=0)
    return df_described
