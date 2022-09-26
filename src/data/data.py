"""
author: jiahui
date: 26-09-2022
desc: importing data from kaggle through API
"""

import kaggle
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

path = 'data/raw'
api.competition_download_files('store-sales-time-series-forecasting', path=path)

with zipfile.ZipFile(path+'/store-sales-time-series-forecasting.zip', 'r') as zipref:
    zipref.extractall(path)


