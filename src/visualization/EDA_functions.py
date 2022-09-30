"""
author: jiahui
date: 29-09-2022
desc: functions for visualization
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


def sales_performance(df, output_filepath):
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    print(df.info())

    # total sales over time
    plt.figure(figsize=(12, 8))
    totalsales_over_time = df.groupby(by=['date'])['sales'].sum().to_frame().reset_index()
    plt.plot(totalsales_over_time['date'], totalsales_over_time['sales'])
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.title('Total Sales in Ecuador over Time')
    plt.savefig(output_filepath + 'totalsales_over_time.jpg')  # note: savefig needs to be before plt.show
    plt.show()


    # total sales by store
    totalsales_by_store = df.groupby(by=['store_nbr'])['sales'].sum().to_frame().reset_index()
    plt.figure(figsize=(12, 8))
    plt.bar(totalsales_by_store['store_nbr'], totalsales_by_store['sales'], color='maroon', width=0.4)
    plt.xlabel("Store No.")
    plt.ylabel("Sales")
    plt.title("Total Sales per Store")
    plt.savefig(output_filepath + 'totalsales_by_store.jpg')
    plt.show()

    return