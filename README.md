# YemekSepetianalyzes
This project performs analysis on customer orders from YemekSepeti. It calculates metrics such as Contact Rate, Self-Service Rate, Seamless Order Rate, NPS (Net Promoter Score), and CSAT (Customer Satisfaction) scores. Additionally, it visualizes data to provide deeper insights into customer satisfaction based on order size and payment method preferences.

## Project Structure

```bash
YemekSepetiAnalyzes/
│
├── .venv/                             # Python virtual environment
├── data/
│   └── task1-dataset-1723704917.xlsx  # Excel dataset file
├── src/
│   └── main.py                        # Main Python script for analysis
├── correlation_matrix.png             # Correlation matrix visualization
├── order_size_vs_csat.png             # Scatterplot: Order Size vs CSAT
├── csat_by_payment_method.png         # Bar chart: CSAT by Payment Method
└── README.md                          # Project documentation (this file)
```

## Dependencies

Before running the script, install the necessary dependencies:

- pandas
- matplotlib
- seaborn
- openpyxl
