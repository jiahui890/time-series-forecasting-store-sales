"""
author: jiahui
date: 26-09-2022
desc: EDA, reporting, visualizations
"""


import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import logging
import pandas as pd
import numpy as np
from src.visualization.EDA_functions import sales_performance


@click.command()
@click.argument('input_filepath', nargs=1, type=click.Path(exists=True))
@click.argument('output_filepath', nargs=1, type=click.Path())
def main(input_filepath, output_filepath):

    df = pd.read_csv(input_filepath)
    # print(df.info())

    # EDA plots
    sales_performance(df, output_filepath)

    logger = logging.getLogger(__name__)
    logger.info('Plotting figures')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    project_dir = Path(__file__).resolve().parents[2]
    load_dotenv(find_dotenv())

    main()