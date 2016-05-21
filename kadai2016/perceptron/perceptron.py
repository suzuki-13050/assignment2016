import sys,math

def read_instance(sentences):#1レビュー分のインスタンス作成
    bow_list=[]  #素性ベクトル格納用リスト
    flg = False
    
    for sentence in sentences.split(" "):
        if flg == False:#1ループ目=ラベル
            flg = True
            rabel=sentence
        else:
            if ":" in sentence :#素性ベクトルがあるときのみ
                key_value=sentence.split(":")#「：」の左側=インデックス、右側=頻度
                bow_list.append((key_value[0],key_value[1]))
                
    return (rabel,bow_list)#1レビュー分のインスタンス

def read_data(file_name):#レビューデータ全体のインスタンス作成
    max_index = 0
    all_data=[]#レビュー毎の情報(インスタンス)が集合となったリスト(全レビュー分のデータ)
    
    for sentences in open(file_name,"r").read().split("\n"):#1行毎読み込み
        if sentences != "":#値が入っている行のみ
            all_data.append(read_instance(sentences))#各レビューのデータをリストに追加

    for j in range(len(all_data)):
        #各レビューにおける最大インデックスと現在の最大インデックスを比較
        max_index=max(int(max(all_data[j][1],key=lambda x: int(x[0]))[0]),max_index)
            
    return (all_data,max_index)#(入出力データ,インデックスの最大値)のタプル

def add_fv(one_review):#重みベクトルに素性ベクトルを足す
    for i in range(len(one_review)):
        weight[int(one_review[i][0])]+=int(one_review[i][1])#インデックスと同じところに頻度を足す 

def sub_fv(one_review):#重みベクトルから素性ベクトルを引く
    for i in range(len(one_review)):
        weight[int(one_review[i][0])]-=int(one_review[i][1])#インデックスと同じところに頻度を足す
    
def mult_fv(one_review):#重みベクトルと素性ベクトルの内積計算
    answer=0
    for i in range(len(one_review)):#レビュー内の全インデックス分計算
        if len(weight) > int(one_review[i][0]):#重みベクトルの長さ以内のインデックスである場合
            answer+=weight[int(one_review[i][0])]*int(one_review[i][1])

    return answer

def update_weight(review_data):#重みベクトルの更新
    for one_review in review_data:
        naiseki=mult_fv(one_review[1])#素性ベクトルを渡して内積計算
        if (naiseki*int(one_review[0])) <= 0:#内積値とラベルが異符号の時のみ重みベクトルの更新を行う
            #print("ラベル：",one_review[0],"内積値：",naiseki)
            if int(one_review[0]) > 0:#ラベルが正
                add_fv(one_review[1])
            else:
                sub_fv(one_review[1])
            
def evaluate(review_data):#正解率の算出
    correct=0
    for one_review in review_data:
        naiseki=mult_fv(one_review[1])#素性ベクトルを渡して内積計算
        if (naiseki*int(one_review[0])) > 0:#内積値とラベルが同符号=正解
            correct+=1
    rate=correct/len(review_data)
            
    return rate #Accuracy rate=正解率
                
if __name__ == "__main__":
    train_data,max_index=read_data(sys.argv[1])
    test_data,max_index_test=read_data(sys.argv[2])
    #print(max_index,max_index_test)#教師データとテストデータの最大インデックス
    weight=[0]*(max_index+1)#重みベクトルの宣言(長さ=レビュー数+1(バイアス項))
    #sub_fv(train_data[1][1])
    
    for learned_count in range(int(sys.argv[3])):
        #print("学習回数",learned_count+1)
        update_weight(train_data)
        
    #print(weight[0:2000])
    #print(train_data)
        
    print("正解率:"+str(evaluate(test_data)*100)+"%")

