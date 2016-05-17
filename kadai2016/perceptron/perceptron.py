import sys

review_data=[]#レビュー毎の情報が集合となったリスト

def read_instance(sentences):#1レビュー分のインスタンス作成
    bow_list=[]  #素性ベクトル格納用リスト
    crt_max = 0  #1レビュー内の最大インデックス
    
    flg = False
    for sentence in sentences.split(" "):
        if flg == False:#1ループ目=ラベル
            flg = True
            rabel=sentence
        else:
            if ":" in sentence :#素性ベクトルがあるときのみ
                key_value=sentence.split(":")
                bow=(key_value[0],key_value[1])
                bow_list.append(bow)

                if int(key_value[0])  > crt_max:#1レビュー内のインデックスの最大値取得
                    crt_max=int(key_value[0])
                    
    return ((rabel,bow_list),crt_max)#(1レビュー分のインスタンス,1レビュー内の最大インデックス)

def read_data():#レビューデータ全体のインスタンス作成

    max_index = 0
    for sentences in open(sys.argv[1],"r").read().split("\n"):#1行毎読み込み
        if sentences != "":#値が入っている行のみ
            instance_index=read_instance(sentences)
            review_data.append(instance_index[0])

            #レビューデータ全体でのインデックスの最大値取得
            if instance_index[1] > max_index:
                max_index=instance_index[1]
    
    return (review_data,int(max_index))#(入出力データ,インデックスの最大値)のタプル

if __name__ == "__main__":
    train_data,max_index=read_data()
    weight=[0]*(max_index+1)

    
    print(len(weight))
