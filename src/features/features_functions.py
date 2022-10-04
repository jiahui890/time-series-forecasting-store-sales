"""
author: jiahui
date: 26-09-2022
desc:
"""

import pandas as pd


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


    df['Is_Holiday_Celebrated'] = ''

    return df