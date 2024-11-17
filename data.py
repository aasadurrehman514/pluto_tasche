import pandas as pd
import scipy.stats as stats
import os


def create_portfolio_summary(df,mapping_file):
    summary = df.groupby("Ratings").agg(
        Obligators=("Defaults", "count"),
        Defaults=("Defaults", "sum")
                        ).reset_index()

    
    result_df = pd.merge(summary, mapping_file, on="Ratings", how="left")
    result_df.sort_values(by='mapped', ascending=True, inplace=True)

    summary_file_path = "test_data.csv"

    result_df.drop(columns=['mapped'], inplace=True)
    result_df.to_csv(summary_file_path, index=False)
    print("Summary saved")

    return result_df


def calculate_default_ratio(dr_df):

    dr_df['default_percentage'] = dr_df['Defaults'] / dr_df['Obligators']
    return dr_df

def calculate_commulative_obligators(dr_df):
    
    dr_df['Commulative_Obligators'] = dr_df['Obligators'][::-1].cumsum()[::-1]
    return dr_df

def calculate_commulative_defaults(dr_df):
    
    dr_df['Commulative_Defaults'] = dr_df['Defaults'][::-1].cumsum()[::-1]
    return dr_df

def calculate_probability_of_defaults(dr_df):
    
    dr_df['probability_of_defaults'] = dr_df['Commulative_Defaults'] / dr_df['Commulative_Obligators']
    return dr_df

def calculate_beta_distribution(dr_df,event):
    dr_df['confidence_interval'] =event['confidence_interval']
    dr_df['Beta_Inv'] = dr_df.apply(beta_inv, axis=1)

    return dr_df

def beta_inv(row):
    probability = row['confidence_interval'] 
    alpha = row['Commulative_Defaults'] + 1   
    beta = row['Commulative_Obligators'] - row['Commulative_Defaults']
    
    return stats.beta.ppf(probability, alpha, beta)
