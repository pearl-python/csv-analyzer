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

#高額注文の抽出
def filter_high_value_orders(df, min_total):
    filtered_df = df[df["total"] >= min_total]
    return filtered_df

#totalの降順ソート
def sort_by_total(df):
    sorted_df = df.sort_values("total", ascending=False)
    return sorted_df

#csvへ保存
def save_csv(df, file_path):
    df.to_csv(file_path, index=False)

#重複行の検出
def show_duplicate_orders(df):
    
    duplicate_ids = df.loc[
    df["order_id"].duplicated(keep=False),
    "order_id"
    ].unique()

    duplicate_rows = df[
        df["order_id"].duplicated(keep=False)
    ]
    print(f"order_id の重複件数：{df['order_id'].duplicated().sum()}")
    print(f"重複order_id：{duplicate_ids}")
    print(f"重複行：\n{duplicate_rows}")

#重複行の日付の最新のものを残す関数
def remove_duplicate_orders(df):
    df = df.sort_values("date")
    deduplicated_df = df.drop_duplicates(subset=["order_id"], keep="last")
    return deduplicated_df

#日付型に変換する
def convert_date_column(df):
    df["date"] = pd.to_datetime(df["date"])
    return df

#日付の年・月を取得する
def add_date_columns(df):
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    return df

#月別の売上高を集計する
def show_monthly_summary(df):
    print(f"月別売上高：\n{df.groupby(['year', 'month'])['total'].sum()}")