"""
author: jiahui
date: 26-09-2022
desc: all functions used in data prep
"""

import pandas as pd
import numpy as np


def check_store_location_and_holiday(dataframes):
    stores = dataframes['stores']
    hol_event = dataframes['holidays_events']

    return


def check_transferred_holiday():
    return


def merge_df(dataframes):
    # leftmost table = train.csv/test.csv
    table = ['train','test']
    main_table = list(set(dataframes.keys()).intersection(set(table)))
    print("All files: ", dataframes.keys())
    print("Type: ", main_table[0])

    # main df
    df = dataframes[main_table[0]]
    # store.csv
    df = df.merge(dataframes['stores'],how='left', on='store_nbr')
    # transactions.csv
    df = df.merge(dataframes['transactions'],how='left', on=['store_nbr','date'])
    # oil.csv
    df = df.merge(dataframes['oil'],how='left', on=['date'])
    # holiday_events.csv
    df = df.merge(dataframes['holidays_events'],how='left', on=['date'])

    df.rename(columns={"type_x": "store_type", "type_y": "holiday_type"}, inplace=True)
    return df


def clean_data(df):


    return