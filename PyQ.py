# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 15:53:44 2018

@author: kagitani
"""

import pandas as pd
df = pd.read_csv('./input/data2.csv')

# マッピング用の辞書データを用意
size_mapping = {'XL': 4,  'L': 3, 'M': 2, 'S': 1}

# size列に対してマッピング用辞書の適用
values = df['size'].map(size_mapping)

df['size'] = values
df