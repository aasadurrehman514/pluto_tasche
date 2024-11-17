# README for Pluto Tasche PD Calculation

## Overview

This Python script implements the **Pluto Tasche approach** to calculate **Probability of Defaults (PDs)** for a credit portfolio. It uses statistical calculations and visualizations to estimate and represent PDs with confidence intervals, leveraging techniques such as beta distribution. The script also generates a comprehensive PDF report with detailed results and charts.

---

## Features

1. **Data Processing**:
   - Reads portfolio data and rating mappings.
   - Computes default ratios, cumulative obligors, and cumulative defaults.

2. **Probability of Default (PD) Calculation**:
   - Utilizes the beta distribution to estimate PDs.
   - Supports a customizable confidence interval.

3. **Visualization**:
   - Generates line charts for binomial distributions of credit ratings.

4. **Report Generation**:
   - Produces a PDF report summarizing results with tables and visualizations.

---

## Prerequisites

1. **Python Libraries**:
   - `pandas`
   - `argparse`
   - `jinja2`
   - `pdfkit`

2. **Other Requirements**:
   - **wkhtmltopdf**: Ensure it is installed and correctly configured. Update the `path_wkhtmltopdf` variable with the installation path.

3. **Input Files**:
   - `portfolio.json`: Contains portfolio data in JSON format.
   - `ratings_map.csv`: Maps credit ratings to corresponding criteria.
   - `report_template.html`: HTML template for generating the report.
   - `style.css`: CSS file for styling the PDF report.

---

## Installation

1. Clone the repository.
2. Install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure `wkhtmltopdf` is installed and accessible from the configured path.

---

## Usage

Run the script with the following command:

```bash
python main.py --portfolio <portfolio.json> --mapping_file <config/ratings_map.csv> --confidence_interval <confidence_value>
```

### Arguments:
- `--portfolio`: Path to the portfolio JSON file. Default: `portfolio.json`.
- `--mapping_file`: Path to the ratings mapping CSV file. Default: `config/ratings_map.csv`.
- `--confidence_interval`: Confidence interval for PD calculations (float). Default: `0.75`.

Example:
```bash
python main.py --portfolio my_portfolio.json --mapping_file my_mapping.csv --confidence_interval 0.9
```

---

## Output

1. **Charts**:
   - PNG files for each credit rating binomial distribution saved in the `results/` directory.

2. **PDF Report**:
   - A comprehensive report named `Shocking_PDs_through_Pluto_Tasche_Approach.pdf` in the `results/` directory.

---

## Folder Structure

```plaintext
├── data/
│   ├── calculate_default_ratio.py
│   ├── calculate_commulative_obligators.py
│   ├── calculate_commulative_defaults.py
│   ├── calculate_probability_of_defaults.py
│   ├── calculate_beta_distribution.py
│   ├── create_portfolio_summary.py
├── visuals/
│   ├── create_line_charts.py
├── config/
│   ├── ratings_map.csv
├── results/
│   ├── <Generated PNG Files>
│   ├── Shocking_PDs_through_Pluto_Tasche_Approach.pdf
├── templates/
│   ├── report_template.html
├── style.css
├── main.py
```

---

## Notes

- Customize the report and charts by editing `report_template.html` and `style.css`.
- For issues with PDF generation, ensure the path to `wkhtmltopdf` is correctly configured.

