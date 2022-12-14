"""
author: jiahui
date: 26-09-2022
desc: building features, cleaning data, transforming data
"""

import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import logging
import pandas as pd
import numpy as np
from src.features.features_functions import extract_dates, check_taken_holiday,check_payday, fill_in_nulls, \
    label_encoding, check_external_stimuli, moving_average


@click.command()
@click.argument('input_filepath', nargs=1, type=click.Path(exists=True))
@click.argument('output_filepath', nargs=1, type=click.Path())
def main(input_filepath, output_filepath):

    df = pd.read_csv(input_filepath)

    # feature engineering
    df = extract_dates(df)
    df = check_taken_holiday(df)
    df = check_payday(df)
    df = check_external_stimuli(df)
    df = fill_in_nulls(df)
    df = moving_average(df)
    df = label_encoding(df)
    print(df)

    # save to file
    df.to_csv(output_filepath, index=False)

    # statistical tests for traditional time-series modeling: ARIMA etc




    logger = logging.getLogger(__name__)
    logger.info('data manipulation for features')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    project_dir = Path(__file__).resolve().parents[2]
    load_dotenv(find_dotenv())

    main()