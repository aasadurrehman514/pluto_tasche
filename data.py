import pandas as pd


def calculate_default_ratio(event):

    dr_df = pd.read_csv(event['ratings'])

    dr_df['default_ratio'] = dr_df['Defaults'] / dr_df['Obligators']
    print(dr_df)