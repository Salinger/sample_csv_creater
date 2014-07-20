・サンプル CSV 生成のためのプログラム
以下の4項目について指定行数だけランダムな値を生成する。
user_id: 1 ~ 100000 までの値
action:  100 ~ 10000 までの値
item_type: 0 ~ 4 までの値
payment: 50 ~ 20000 までの値（値の幅はitem_typeに依存）

・使用例（1000行のサンプルデータを生成）
python mk_sample.py 1000 > payment_sample.csv
