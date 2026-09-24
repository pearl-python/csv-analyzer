from analyzer import load_csv, show_summary, show_missing_values, show_numeric_summary, show_status_counts, show_category_summary, add_total_column

#csvを読み込む
df = load_csv("sample/sales.csv")
#データの中身を確認
print(df.head())
#dfの基本情報確認
show_summary(df)
#dfの欠損値を確認
show_missing_values(df)
#dfのprice集計値を確認
show_numeric_summary(df)
#dfのステータスごとの件数を確認
show_status_counts(df)
#dfのトータル金額を計算
df = add_total_column(df)
#dfのカテゴリごとのprice合計を確認
show_category_summary(df)