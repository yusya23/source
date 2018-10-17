import pandas as pd

df = pd.read_csv('dataset/stationery.csv',encoding='utf-8')

df.head()
stationery_counts = df['Name'].value_counts()

# 大きなサイズのcsvファイルの読込み
df_log_big = pd.read_csv('dataset/product_log.csv', low_memory=False)
# 日本語などでUTF8を使用している時
df_log1_utf8 = pd.read_csv('dataset/product_log.csv', encoding='utf-8')
# 日本語などでWindowsのShift JIS（cp932）を使用している時
df_log_cp932 = pd.read_csv('dataset/product_log.csv', encoding='cp932')
#列の追加/変更
df['HeightM'] = df['Height']/100
df['Name'] = ['小麦粉A 200g', '小麦粉A 500g', '小麦粉A 1000g', '小麦粉B 300g', '小麦粉C 900g']

%matplotlib inline
import matplotlib.pyplot as plt

# 日本語フォントとサイズを指定
plt.rcParams['font.family'] = 'TakaoGothic'
plt.rcParams['font.size'] = 14
# BMIをグラフで表示
df[['BMI']].plot.bar()
plt.xticks(df.index,df.Name)
# BMIが25以上の人を表示
df_filtering = df[df['BMI'] >= 25]
# 条件付きでデータを表示
df_filtering = df[(df['BMI'] >= 25) | (df['BMI'] < 18.5)]
df_ans = df[(df['Height'] >= 165) & (df['Weight'] >= 55)]
df_ans = df.query('Height >= 165 & Weight >= 55')
#リストをデータ列に
sample_list = ['a', 'b', 'c', 'd']
series = pd.Series(sample_list)
series_1 = series[1]
#目次を変更
series.index=['i1','i2','i3','i4']
s_indexes = series.index.values
#データフレーム作成
df = pd.DataFrame([list('abcd'), list('efgh')])
df = pd.DataFrame([list('abc'),list('def'),list('ghi')],columns=['r1','r2','r3'])
df = pd.DataFrame([list('abcd'), list('efgh'), list('ijkl'), list('mnop')],
                  index=['first', 'second', 'third', 'fourth'], columns=list('ABCD'))
#データフレームの値表示
df_values = df.values
df_columns = df.columns.values
df_idx_val  = df.index.values
df_index = df.index.values
df.columns=list('ABCD')
df_r2 = df['r2']
df_r2r3 = df[['r2','r3']]
#行データをシリーズに
df_loc = df.loc[1]
df_loc = df.loc['second']
df_iloc_1 = df.iloc[1]
df_loc_rowcol = df.loc['second','C']
#特定データ抽出
df_loc_row = df.loc[['second','fourth']]
df_loc_rowcol = df.loc[['second','fourth'],['A','D']]
# 列だけ
df_loc_col = df.loc[:, ['A', 'D']]
#データの読み込み
df_tsv = pd.read_csv('dataset/health_check.tsv',sep='\t')
df_head = pd.read_csv('dataset/health_check_nohead.csv',names=['Name','Height','Weight'])
#データ書き出し
df_csv.to_csv('./pyq_out.csv',index=False)
#DataFrameをjson形式に変更
df_json = df_csv.to_json()
df_json_records = df_csv.to_json(orient='records')
# 列price_per_kgのランクを新しい列 price_rankとして追加
df['PriceRank'] = df['PricePerKg'].rank()
#文字数追加
df['CommentLen'] = df['Comment'].str.len()
#データ挿入
sliced_list = []
for row in df.itertuples():
    sliced_list.append(row.Comment[:15])

df['SlicedComment'] = sliced_list

def get_sliced_str(x):
    return x[:15]

df['SlicedComment'] = df['Comment'].apply(get_sliced_str)

#条件分岐
def get_sliced_str(x):
    SPLIT_STR_LENGTH = 12

    first_sentence = x.split('。')[0] + '。'
    if len(first_sentence) > SPLIT_STR_LENGTH:
        return x[:SPLIT_STR_LENGTH] + '...'
    else:
        return first_sentence
#文字列をカウント
df['SentenceNum'] = df['Comment'].str.count('。')
#評価
def get_3range_rate(x):
    if x >= 4:
        return '好評'
    elif x == 3:
        return '普通'
    elif x <= 2:
        return '不評'
df['Rate3range'] = df['Rate'].apply(get_3range_rate)
# 箱ひげ図の表示
df_case_log.boxplot(showmeans=True);
# ヒストグラムの確認
df_case_log.hist(bins=10, range=(0, 10));
# 散布図行列
pd.plotting.scatter_matrix(df_case_log);
# 相関行列
df_corr = df_case_log.corr()
# 2つの売上データを縦に結合
df3 = pd.concat([df1, df2])
# indexを再設定
df4 = pd.concat([df1, df2]).reset_index(drop=True)
# 2つのデータを横に結合
df6 = pd.concat([df3, df5], axis=1)
# pd.mergeに2つのDataFrameを渡すとマージできます
# このとき、両方に含まれる列ラベルがキーとなります
df_sale = pd.merge(df_log, df_master)
# キーを自分で指定する場合は、`on`オプションを使います
df_sale = pd.merge(df_log, df_master, on='Product')
# 時刻順にしたいのでマージされた表を列Dateでソートします
# reset_index(drop=True)はindex(行ラベル)を再設定するイディオムです
df_sale = df_sale.sort_values('Date').reset_index(drop=True)
#  howオプションで結合方法を指定できます
# デフォルトは inner で内部結合になります
df_sale = pd.merge(df_log, df_master, how='inner')
# Saleのグラフをみます
df_sale.Sale.plot()
# 売上金額(Sale)をPrice×Numで計算して追加します
df_sale['Sale'] = df_sale.Price * df_sale.Num
# 要素が文字列である列に、strアクセサを使うと列が文字列であるかのように扱えます
# str[5:7]とすると、'2017-01-03'などの５文字目と６文字目をとります
df_log_date_str57 = df_log.Date.str[5:7]
# astype(int)でintに変換できます
df_log_date_str57_int = df_log_date_str57.astype(int)
# 月の値を取り出し、新しい列Monthを作ります
df_log['Month'] = df_log_date_str57_int
# 製品(Product)ごと、月(Month)ごとの販売個数(Num)の合計(sum)の表を作ります
df_log_pivot = df_log.pivot_table(
    values='Num', index='Product', columns='Month', aggfunc='sum')
# aggfuncで色々なメソッドが使えます
# countで該当個数になります
df_log.pivot_table('Num', 'Product', 'Month', aggfunc='count')
# aggfuncに明示的に指定することもできます
df_log.pivot_table('Num', 'Product', 'Month', aggfunc='mean')
# グラフを描いてみよう（横軸が製品になります）
df_log_pivot.plot();
# 横軸を月にして、製品ごとのグラフを描きます
df_log_pivot.T.plot();
# 月の値を取り出し、新しい列Monthを作ります
df_log['Month'] = df_log.Date.str[5:7].astype(int)