# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 11:47:16 2019

@author: Seba
"""

import pandas as pd
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.width', None)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('USA_Housing.csv')

print(df.columns)
