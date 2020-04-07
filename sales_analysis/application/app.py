from flask import Flask
from datetime import datetime
import os
import pandas as pd

from sales_analysis.data_pipeline._pipeline import SalesPipeline
from sales_analysis.data_pipeline import BASEPATH

# --------------------------------------------------------------------------
# Load and check valid data

FILEPATH = os.path.join(BASEPATH, "data")
DATA_FILES = [
    'commissions.csv', 
    'orders.csv', 
    'order_lines.csv', 
    'products.csv', 
    'product_promotions.csv', 
    'promotions.csv'
]

try: 
    DATA = {f : pd.read_csv(os.path.join(FILEPATH, f)) for f in DATA_FILES}
except FileNotFoundError as inst:
    print(type(inst))
    print(inst.args)

# --------------------------------------------------------------------------
# Web application

app = Flask(__name__)

@app.route('/<selected_date>', methods=['GET'])
def my_view(selected_date, daily_data):
    selected_date = datetime.strptime(selected_date, "%Y-%m-%d").date()

    sales = SalesPipeline(**DATA)
    sales_summary = sales.summary()

    try:
        daily_data = sales_summary.loc[selected_date]
        return daily_data.to_dict()
    except (KeyError):
        return f"""No data for {selected_date}. Please try 
        another date, such as 2019-08-01"""

if __name__ == '__main__':
    app.run(debug=True)
