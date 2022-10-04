"""
author: jiahui
date: 26-09-2022
desc:
"""

import pandas as pd
import numpy as np


def extract_dates(df):
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    df['Year'] = df['date'].dt.year
    df['Month'] = df['date'].dt.month
    df['Day'] = df['date'].dt.day
    df['DayofWeek'] = df['date'].dt.dayofweek
    return df


def clean_data():
    # check for NA
    # check for outliers

    return


def check_celebrated_holiday(df):
    def check_holiday(x):
        if x['transferred'] == True or x['holiday_type'] == 'Work Day':
            return 0
        elif x['holiday_type'] == np.nan:
            return 0
        else:
            return 1

    df['Is_Holiday_Celebrated'] = df.apply(check_holiday, axis=1)
    return df


def check_payday():
    return