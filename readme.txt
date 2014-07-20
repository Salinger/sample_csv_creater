# mk_sample.py
サンプル CSV 生成のためのプログラム
以下の4項目について指定行数だけランダムな値を生成する。
user_id: 1 ~ 100000 までの値
action:  100 ~ 10000 までの値
item_type: 0 ~ 4 までの値
payment: 50 ~ 20000 までの値（値の幅はitem_typeに依存）

※ 使用例（1000行のサンプルデータを生成）
python mk_sample.py 1000 > payment_sample.csv



# sample.R
Rによる user_id 毎の payment 合計額を集計するプログラム。
実行に要した時間を出力する。



# sample.sh
MCMDによる user_id 毎の payment 合計額を集計するプログラム。

$ time bash sample.sh
とすると実行に要した時間を出力できる。
