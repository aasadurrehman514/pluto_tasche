import pandas as pd
import os
import argparse
import json
from datetime import datetime


from data import calculate_default_ratio,calculate_commulative_obligators,calculate_commulative_defaults,calculate_probability_of_defaults,calculate_beta_distribution
from visuals import create_line_charts
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--ratings', type=str, default = 'test_data.csv')
    parser.add_argument('--confidence_interval', type=float, default = 0.75 )

    args = parser.parse_args()
    event = vars(args)

    start_time = datetime.now()

    df = pd.read_csv(event['ratings'])

    df = calculate_default_ratio(df)
    df = calculate_commulative_obligators(df)
    df = calculate_commulative_defaults(df)
    df = calculate_probability_of_defaults(df)
    df = calculate_beta_distribution(df,event)

    create_line_charts(df)

    end_time = datetime.now()
    print("\n** Total Elapsed Runtime:",str(end_time - start_time) )


if __name__ == "__main__":
    main()