"""
author: jiahui
date: 26-09-2022
desc: all functions used in data prep
"""

import pandas as pd
import numpy as np


def matching_store_and_holiday_location(df, holiday_events):
    # get unique holiday dates
    dates = dates = holiday_events['date'].unique().tolist()

    # initial merging with just date
    df_temp = df.merge(holiday_events,how='left', on=['date'])

    # splitting holiday location types
    local = holiday_events[holiday_events['locale']=='Local']
    regional = holiday_events[holiday_events['locale'] == 'Regional']
    national = holiday_events[holiday_events['locale'] == 'National']

    # inner join with each location
    df_local = df.merge(local, how='inner', left_on=['date','city'], right_on=['date','locale_name'])
    df_regional = df.merge(regional, how='inner', left_on=['date','state'], right_on=['date','locale_name'])
    df_national = df.merge(national, how='inner', on='date')

    # get rows from initial_merge that does not have holiday
    df_no_hols = df_temp[~df_temp['date'].isin(dates)]

    # concat by rows: all joins with holiday per location + rows with no holidays
    df_interim = pd.concat([df_no_hols, df_local, df_regional, df_national], axis=0).reset_index().drop(columns=['index'])

    # find row ids that matched holiday dates but not celebrated locations
    id_holidays = df_temp[df_temp['date'].isin(dates)]['id'].tolist()
    matched_ids = df_interim['id'].unique().tolist()
    df_rows_not_matched = df[(df['id'].isin(id_holidays)) & (~df['id'].isin(matched_ids))]
    # get holiday events columns --> use match with local
    df_not_matched = df_rows_not_matched.merge(holiday_events, how='left', left_on=['date','city'], right_on=['date','locale_name'])

    # find combine all df
    final_df = pd.concat([df_interim,df_not_matched], axis=0).reset_index().drop(columns=['index']).sort_values(by='id')

    return final_df



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
    #df = df.merge(dataframes['holidays_events'],how='left', on=['date'])
    final_df = matching_store_and_holiday_location(df, dataframes['holidays_events'])

    # manipulations
    final_df.rename(columns={"type_x": "store_type", "type_y": "holiday_type"}, inplace=True)
    final_df['date'] = pd.to_datetime(final_df['date'], format='%Y-%m-%d')

    return final_df

