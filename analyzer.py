import pandas as pd

#csv読み込み関数
def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df

#DataFrameの基本情報をまとめて表示する関数
def show_summary(df):
    rows, columns = df.shape
    print(f"行数:{rows}")
    print(f"列数:{columns}")
    print(f"列名：{df.columns}")
    print(f"データ型：\n{df.dtypes}")

#DataFrameの欠損値を確認する関数
def show_missing_values(df):
    print(df.isna().sum())

#DataFrameの集計値を確認する
def show_numeric_summary(df):
    print(f"price合計値：{df['price'].sum()}")
    print(f"price平均値：{df['price'].mean()}")
    print(f"price最大値：{df['price'].max()}")
    print(f"price最小値：{df['price'].min()}")

#ステータスごとの件数を確認する
def show_status_counts(df):
    print(df["status"].value_counts())

#カテゴリごとのprice合計を確認する
def show_category_summary(df):
    print(df.groupby("category")["total"].sum())

#トータル金額の計算を実施する
def add_total_column(df):
    df["total"] = df["price"] * df["quantity"]
    return df