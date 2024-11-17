import pandas as pd
import argparse
import json
import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import pdfkit
import sys
import time

from data import calculate_default_ratio,calculate_commulative_obligators,calculate_commulative_defaults,calculate_probability_of_defaults,calculate_beta_distribution,create_portfolio_summary
from visuals import create_line_charts


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--portfolio', type=str, default = 'portfolio.json')
    parser.add_argument('--mapping_file', type=str, default = 'config/ratings_map.csv')
    parser.add_argument('--confidence_interval', type=float, default = 0.75 )

    args = parser.parse_args()
    event = vars(args)

    start_time = datetime.now()
    portfolio = pd.read_json(event['portfolio'])
    mapping_file = pd.read_csv(event['mapping_file'])
    df = create_portfolio_summary(portfolio,mapping_file)
 
    df = (df
        .pipe(calculate_default_ratio)
        .pipe(calculate_commulative_obligators)
        .pipe(calculate_commulative_defaults)
        .pipe(calculate_probability_of_defaults)
        .pipe(calculate_beta_distribution, event))

    create_line_charts(df)
    generate_pdf_report(event,df)

    end_time = datetime.now()
    print("\n** Total Elapsed Runtime:",str(end_time - start_time) )

def generate_pdf_report(event,df):

    print(f'\rGenerating PDF report')

    current_directory = os.getcwd()
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    template_vars = { 'title' : "Shocking PDs through Pluto Tasche Approach",
                    'representation_table' : df,
                    "A1": os.path.join(current_directory,"results", "A1 - Binomial Distribution.png"),
                    "A2": os.path.join(current_directory,"results", "A2 - Binomial Distribution.png"),
                    "A3": os.path.join(current_directory,"results", "A3 - Binomial Distribution.png"),
                    "AA1": os.path.join(current_directory,"results", "AA1 - Binomial Distribution.png"),
                    "AA2": os.path.join(current_directory,"results", "AA2 - Binomial Distribution.png"),
                    "AA3": os.path.join(current_directory,"results", "AA3 - Binomial Distribution.png"),
                    "AAA": os.path.join(current_directory,"results", "AAA - Binomial Distribution.png"),
                    "B1": os.path.join(current_directory,"results", "B1 - Binomial Distribution.png"),
                    "B2": os.path.join(current_directory,"results", "B2 - Binomial Distribution.png"),
                    "B3": os.path.join(current_directory,"results", "B3 - Binomial Distribution.png"),
                    "BA1": os.path.join(current_directory,"results", "BA1 - Binomial Distribution.png"),
                    "BA2": os.path.join(current_directory,"results", "BA2 - Binomial Distribution.png"),
                    "BB3": os.path.join(current_directory,"results", "BB3 - Binomial Distribution.png"),
                    "BBB1": os.path.join(current_directory,"results", "BBB1 - Binomial Distribution.png"),
                    "BBB2": os.path.join(current_directory,"results", "BBB2 - Binomial Distribution.png"),
                    "BBB3": os.path.join(current_directory,"results", "BBB3 - Binomial Distribution.png"),
                    "C": os.path.join(current_directory,"results", "C - Binomial Distribution.png"),
                    "CA": os.path.join(current_directory,"results", "CA - Binomial Distribution.png"),
                    "CAA1": os.path.join(current_directory,"results", "CAA1 - Binomial Distribution.png"),
                    "CAA2": os.path.join(current_directory,"results", "CAA2 - Binomial Distribution.png"),
                    "CAA3": os.path.join(current_directory,"results", "CAA3 - Binomial Distribution.png"),
                    }
                

    env = Environment(loader=FileSystemLoader('.'))
    internal_template = env.get_template("report_template.html")
    options = {'enable-local-file-access': True, 'quiet': ''}
    
    html_out = internal_template.render(template_vars)
    pdfkit.from_string(html_out,"results/Shocking_PDs_through_Pluto_Tasche_Approach.pdf", css=["style.css"],options=options,configuration=config)




if __name__ == "__main__":
    main()