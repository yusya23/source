# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

def should_re_exam(weight):
    """ 再検査対象の人はTrue """
    if weight > 90:
        return True
    else:
        return False
for row in df.itertuples():
    print(should_re_exam(row.weight), row.y)
    
    
    
%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("./input/data3.csv")

plt.hist(df[df["y"] == 0]["x"],
         bins=24, range=(0, 6), color="blue")
plt.hist(df[df["y"] == 1]["x"],
         bins=24, range=(0, 6), color="red");
         
def is_one(num):
    if num > 3:
        return True
    else:
        return False
    
answers = []
for row in df.itertuples():
    answer = is_one(row.x)
    answers.append(answer)
    
(answers == df['y']).sum() / len(answers)


import pandas as pd
df = pd.read_csv('./input/jh_heights_weights.csv')
df.head()
def is_man(height,weight):
    if height > 163 and weight < 60:
        return True
    else:
        return False
    
answers = []

for row in df.itertuples():
    y = is_man(row.height,row.weight)
    answers.append(y)

num_correct = (df['y'] == answers).sum()
num_correct

num_correct / len(df)



%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./input/jh_heights_weights.csv')

men = df[df['y'] == 1]
women = df[df['y'] == 0]

plt.scatter(men['height'],men['weight'],color='green')
plt.scatter(women['height'],men['weight'],color='blue')

a = 60/190

def is_man(height,weight):
    if weight < a * height:
        return True
    else:
        return False
 answers = []
for row in df.itertuples():
    answers.append(is_man(row.height,row.weight))   
num_corrents = (df['y'] == answers).sum()
num_corrents

num_corrents / len(df)

men = df[df['y'] == 1]
women = df[df['y'] == 0]

plt.scatter(men['height'],men['weight'],color='green')
plt.scatter(women['height'],men['weight'],color='blue')

plt.plot((0,190),(0,60),color='red')
plt.xlim(df['height'].min(),df['height'].max())
plt.ylim(df['weight'].min(),df['weight'].max());

##########################欠損値の除去###############################
# 欠損値(NaN) を含む"行"を削除
df1 = df.dropna()
# 欠損値(NaN) を含む"列"を削除
df2 = df.dropna(axis=1)
# 欠損値(NaN)ではない値が4つ未満の"行"を削除
df3 = df.dropna(thresh=4)
# 特定の列(身長)に欠損値(NaN)を含む"行"を削除
df4 = df.dropna(subset=["身長(cm)"])

#####################欠損値の補完#####################################
import pandas as pd
df = pd.read_csv('./input/data1.csv')

# 全データの表示
df
from sklearn.preprocessing import Imputer

#  欠損値(NaN) に対して 平均値(mean) を割り当てるImputerオブジェクトを生成
imp = Imputer(missing_values="NaN", strategy="mean")

# データセットの学習
imp.fit(df[["身長(cm)"]])

# strategy="mean"に基づいて欠損値(NaN)を平均値に置き換える
values = imp.transform(df[["身長(cm)"]])

# DataFrameに変換したデータを代入する
df[["身長(cm)"]] = values
df

#  欠損値(NaN) に対して 中央値(median) を割り当てるImputerオブジェクトを生成
imp = Imputer(missing_values="NaN", strategy="median")

# データセットの学習 + strategy="median"に基づいて欠損値(NaN)を中央値に置き換える
values = imp.fit_transform(df[["体重(kg)"]])

# DataFrameに変換したデータを代入する
df[["体重(kg)"]] = values
df

#  欠損値(NaN) に対して 最頻値(most_frequent) を割り当てるImputerオブジェクトを生成
imp = Imputer(missing_values="NaN", strategy="most_frequent")

# データセットの学習 + strategy="most_frequent"に基づいて欠損値(NaN)を最頻値に置き換える
values = imp.fit_transform(df[["視力"]])

# DataFrameに変換したデータを代入する
df[["視力"]] = values
df



####################クラスラベルのエンドーディング#######################

import pandas as pd
df = pd.read_csv('./input/data2.csv')

# 全データの表示
df

# クラスラベルのユニークな集合を抽出
classlabels = list(set(df["classlabel"]))
classlabels

# クラスラベルの集合からマッピング辞書を生成する
class_mapping = {}
for number, label in enumerate(sorted(classlabels)):
    # クラスラベルをキーに、numberを値としてセットする
    class_mapping[label] = number
    
#l = ['Alice', 'Bob', 'Charlie']
#for i, name in enumerate(l):
#    print(i, name)
# 0 Alice
# 1 Bob
# 2 Charlie


#org_list = [3, 1, 4, 5, 2]
#
#new_list = sorted(org_list)
#print(org_list)
#print(new_list)
# [3, 1, 4, 5, 2]
# [1, 2, 3, 4, 5]
    
class_mapping

# マッピングする
classlabels_data = df['classlabel'].map(class_mapping)
df['classlabel'] = classlabels_data
df

# クラスラベルを戻すために、class_mappingのキーと値を逆にした辞書を作る
reverse_class_mapping = {value: key for key, value in class_mapping.items()}
reverse_class_mapping

# 再びクラスラベルを文字列に変換する
df['classlabel'] = df['classlabel'].map(reverse_class_mapping)
df

####################クラスラベルのエンドーディング2#######################
import pandas as pd
df = pd.read_csv('./input/data2.csv')

# 全データの表示
df
from sklearn.preprocessing import LabelEncoder

# LabelEncoderオブジェクトを生成
encoder = LabelEncoder()

 # fit_transformメソッドで、クラスラベルを整数値にエンコーディング
classlabels_data = encoder.fit_transform(df['classlabel'])
df['classlabel'] = classlabels_data
df
df['classlabel'] = encoder.classes_[classlabels_data]
df


######################one-hotエンコーディング#####################################
import pandas as pd
df = pd.read_csv('./input/data2.csv')

# 全データの表示
df
from sklearn.preprocessing import LabelEncoder

# LabelEncoderオブジェクトを生成
encoder = LabelEncoder()

 # fit_transformメソッドで、color列を整数値にエンコーディング
values = encoder.fit_transform(df['color'])
values
# 1次元配列を2次元配列に変換
values.reshape(-1, 1)
from sklearn.preprocessing import OneHotEncoder

# OneHotEncoder　で  それぞれの色が列になり、該当の色に1がセットされる
encoder = OneHotEncoder()
result = encoder.fit_transform(values.reshape(-1, 1))

# one-hotエンコーディングされたデータをDataFrameに変換
colors_df = pd.DataFrame(result.toarray(), columns=sorted(list(set(df['color']))))
colors_df


######################one-hotエンコーディング2#####################################
import pandas as pd
df = pd.read_csv('./input/data2.csv')

# 全データの表示
df
# one-hotエンコーディングされたDataFrameを取得
colors_df = pd.get_dummies(df['color'])

# 元のDataFrameと、変換されたDataFrameを結合
df = pd.merge(df, colors_df, left_index=True, right_index=True, how='outer')
df