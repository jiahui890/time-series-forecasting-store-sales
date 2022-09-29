# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from src.data.data_functions import merge_df
import pandas as pd
import re


@click.command()
@click.argument('input_filepath', nargs=5, type=click.Path(exists=True))
@click.argument('output_filepath', nargs=1, type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """

    # fixme
    # current working dir: C:\Users\FT-LT74\Desktop\notes\github\time-series-forecasting-store-sales\data\raw
    # parameters: raw\train.csv raw\stores.csv raw\transactions.csv raw\oil.csv raw\holidays_events.csv interim\merged_df.csv
    # TODO: change train.csv to test.csv when generating test dataset

    # import all files and store as dictionary
    dataframes = {}
    for path in input_filepath:
        filename = re.findall(r'[^\\]+(?=\.)', path)
        df = pd.read_csv(path)
        dataframes[filename[0]] = df


    # since test data has same features as train data, we need not encode supplementary info files (but it would be good prac to do so)
    # merge df and save interim
    merged_df = merge_df(dataframes)
    print(merged_df)
    merged_df.to_csv(output_filepath, index=False)


    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
