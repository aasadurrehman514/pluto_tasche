import pandas as pd
import os
import argparse
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta

from data import calculate_default_ratio

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--ratings', type=str, default = 'test_data.csv')

    args = parser.parse_args()
    event = vars(args)

    start_time = datetime.now()

    calculate_default_ratio(event)

    end_time = datetime.now()
    print("\n** Total Elapsed Runtime:",str(end_time - start_time) )


if __name__ == "__main__":
    main()