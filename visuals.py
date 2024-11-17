import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


def create_line_charts(df):
    
    default_ratio = df['Defaults'].sum() / df['Obligators'].sum()

    for value,shocked_pd,rating in zip(df['Commulative_Obligators'],df['Beta_Inv'],df['Ratings']):

        plot_df = pd.DataFrame(columns=['trials', 'PD', 'beta_PD'])
        rows = []

        for numbers in range(0,value):
                
                from_default_rate = stats.binom.pmf(numbers, value, default_ratio)
                from_beta_dist = stats.binom.pmf(numbers, value, shocked_pd)
                rows.append([numbers, from_default_rate , from_beta_dist ])


        df = pd.concat([plot_df, pd.DataFrame(rows, columns=['trials', 'PD', 'beta_PD'])], ignore_index=True)

        first_24 = df.iloc[:60]
        remaining_df = df.iloc[60:]
        filtered_remaining_df = remaining_df[remaining_df['PD'] > 0.0000001]

        df = pd.concat([first_24, filtered_remaining_df])
        
        plt.figure(figsize=(10, 6))
        plt.plot(df['trials'], df['PD'], label='PD', color='blue', marker='o')
        plt.plot(df['trials'], df['beta_PD'], label='beta_PD', color='red', marker='x')

        plt.title(f"{rating} - Binomail Distribution")
        plt.xlabel('Trials')
        plt.ylabel('Values')
        plt.legend()
        plt.grid(True)
        plt.savefig('results/{}'.format(f"{rating} - Binomail Distribution"))
        plt.close()
    print("plots saved in result folder")

    return True






