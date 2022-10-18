"""
author: jiahui
date: 26-09-2022
desc:
"""

import pandas as pd
import numpy as np
from datetime import datetime
import calendar
from sklearn import preprocessing


def extract_dates(df):
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    df['Year'] = df['date'].dt.year
    df['Month'] = df['date'].dt.month
    df['Day'] = df['date'].dt.day
    df['DayofWeek'] = df['date'].dt.dayofweek
    return df


def fill_in_nulls(df):
    # check for NA
    df['transactions'].fillna(0, inplace=True)
    df['dcoilwtico'].fillna(0, inplace=True)
    df['transferred'].fillna(False, inplace=True)
    df.fillna('None', inplace=True)  # fillna for the rest are strings
    return df


def check_celebrated_holiday(df):
    def check_holiday(x):
        if x['transferred'] == True or x['holiday_type'] == 'Work Day':
            return 0
        elif str(x['holiday_type']).lower()=='nan':
            return 0
        else:
            return 1

    df['Is_Holiday_Celebrated'] = df.apply(check_holiday, axis=1)
    return df


def check_payday(df):
    def payday(x):
        end_of_month = calendar.monthrange(x['Year'], x['Month'])[1]
        if (x['Day'] == 15) or (x['Day'] == end_of_month):
            return 1
        else:
            return 0

    df['Is_PayDay'] = df.apply(payday, axis=1)
    return df


def label_encoding(df):
    # getting object type columns
    cols = list(df.select_dtypes(include=[object, bool]).columns)
    le = preprocessing.LabelEncoder()
    df[cols] = df[cols].apply(le.fit_transform)
    return df


