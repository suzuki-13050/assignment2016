#ログファイル作成
rm c_x.log
touch c_x.log

#x=-15～15までループ
for x in -15 -10 -5 0 5 10 15
do
    #コスト=2^x
    cost=$(echo "scale=10; 2^$x" \ | bc)
    echo "コスト=$cost"
    #モデル作成
    #rm train_cv0.txt.model &
    ./train -B 1 -c $cost train_cv0.txt
    #テストデータでの分類精度をログファイルに追記
    ./predict test_cv0.txt train_cv0.txt.model cache.txt>>c_x.log
    #rm cache.txt
done