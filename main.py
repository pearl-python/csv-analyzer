from analyzer import (
    load_csv,
    show_summary,
    show_missing_values,
    show_numeric_summary,
    show_status_counts,
    show_category_summary,
    add_total_column,
    filter_high_value_orders,
    sort_by_total,
    save_csv,
    show_duplicate_orders,
    remove_duplicate_orders,
    convert_date_column,
    add_date_columns,
    show_monthly_summary
)

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
#dfのカテゴリごとのtotalを確認
show_category_summary(df)
#dateを日付型に変更
df = convert_date_column(df)
#dateから年月を取得
df = add_date_columns(df)
#10000以上のtotalを確認
high_value_orders = filter_high_value_orders(df, 10000)
print(high_value_orders)
#totalの降順ソート
high_value_orders = sort_by_total(high_value_orders)
print(high_value_orders)
#csvへ保存
save_csv(high_value_orders, "sample/high_value_orders.csv")
#重複行数確認
show_duplicate_orders(df)
#重複行を最新の日付以外排除
df = remove_duplicate_orders(df)
#月別の売上高
show_monthly_summary(df)
print(df)