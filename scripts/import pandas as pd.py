import pandas as pd
import numpy as np

def load_dataset(filepath):
    return pd.read_csv(filepath)

def fill_missing_values(df):
    df['children'].fillna(0, inplace=True)
    df['agent'].fillna(0, inplace=True)
    df['company'].fillna(0, inplace=True)
    df['country'].fillna("Unknown", inplace=True)
    return df

def remove_duplicates(df):
    return df.drop_duplicates()

def treat_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[column] = np.where(df[column] < lower, lower,
                          np.where(df[column] > upper, upper, df[column]))
    return df

def remove_zero_guests(df):
    return df[~((df['adults'] == 0) & (df['children'] == 0) & (df['babies'] == 0))]
