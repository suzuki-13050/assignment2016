import sys,random,math,time
#import numpy as np
from optparse import OptionParser

def read_instance(sentences):#1レビュー分のインスタンス作成
    bow_list=[]  #素性ベクトル格納用リスト
    test_list=[]
    bunbo=0
    flg = False

    for sentence in sentences.split():
        if flg == False:#1ループ目=ラベル
            flg = True
            rabel=int(sentence)
        else:
            if ":" in sentence :#素性ベクトルがあるときのみ
                index,value=map(int,sentence.split(":")) #「：」の左側=インデックス、右側=頻度
                bunbo+=value*value
                
                test_list.append((index,value))

    #bunbo+=1
    if int(opts.regular)==0:#正規化モード=オフ
        bunbo=1
        
    for bow in test_list:
        bow_list.append((bow[0],bow[1]/math.sqrt(bunbo)))#タプルで渡す

    #bow_list.append((0,1/math.sqrt(bunbo)))
    bow_list.append((0,int(opts.bias)))#バイアス項

    return (rabel,bow_list)#1レビュー分のインスタンス

def read_data(file_name):#レビューデータ全体のインスタンス作成
    max_index = 0
    all_data=[]#レビュー毎の情報(インスタンス)が集合となったリスト(全レビュー分のデータ)
    
    for sentences in open(file_name,"r").read().split("\n"):#1行毎読み込み
        if sentences != "":#値が入っている行のみ
            all_data.append(read_instance(sentences))#各レビューのデータをリストに追加

    for j in range(len(all_data)):
        #各レビューにおける最大インデックスと現在の最大インデックスを比較
        max_index=max(max(all_data[j][1],key=lambda x: x[0])[0],max_index)
        
    return (all_data,max_index)#(入出力データ,インデックスの最大値)のタプル

def add_fv(one_review_fv):#重みベクトルに素性ベクトルを足す
    for instance in one_review_fv:#instance=1単語分のラベルと頻度
        weight[instance[0]]+=instance[1]

def sub_fv(one_review_fv):#重みベクトルから素性ベクトルを引く
    for instance in one_review_fv:
        weight[instance[0]]-=instance[1]#インデックスと同じところから頻度を引く

def add_tmp(one_review_fv,nupdates):
    for instance in one_review_fv:
        tmp_weight[instance[0]]+=(instance[1]*nupdates)

def sub_tmp(one_review_fv,nupdates):
    for instance in one_review_fv:
        tmp_weight[instance[0]]-=(instance[1]*nupdates)

def averaged_weight(num):
    for i in range(len(weight)):
        ave_weight[i]=weight[i]-(tmp_weight[i]/num)

def mult_fv(we_vec,one_review,length):#重みベクトルと素性ベクトルの内積計算
    answer=0

    for index,fv in one_review:#レビュー内の全インデックス分計算
        if length > index:#重みベクトルの長さ以内のインデックスである場合
            answer+=we_vec[index]*fv
            
    return answer

def update_weight(label,one_review_fv,length,nupdates):#重みベクトルの更新
    #素性ベクトルを渡して内積計算
    naiseki=mult_fv(weight,one_review_fv,length)
    if ((naiseki*label) <= 0)or(math.fabs(naiseki)<0.1):#内積値とラベルが異符号の時のみ重みベクトルの更新を行う
        if label > 0:#ラベルが正
            add_fv(one_review_fv)
            add_tmp(one_review_fv,nupdates)
        else:
            sub_fv(one_review_fv)
            sub_tmp(one_review_fv,nupdates)
        """
        for i in range(len(weight)):
            test[i]+=weight[i]
        """
        nupdates+=1

    return nupdates#戻り値は更新回数+1
      
def evaluate(learned_vec,review_data,length):#正解率の算出
    correct=0
    for one_review in review_data:
        naiseki=mult_fv(learned_vec,one_review[1],length)#素性ベクトルを渡して内積計算
        if (naiseki*one_review[0]) > 0:#内積値とラベルが同符号=正解
            correct+=1
    return correct,len(review_data),(correct/len(review_data)) #Accuracy rate=正解率=正解数÷インスタンス数

if __name__ == "__main__":
    parser=OptionParser()
    parser.add_option('-t','--train',dest="train_file",help="train_data_name.")
    parser.add_option('-e','--test',dest="test_file",help="test_data_name.")
    parser.add_option('-n','--upnum',dest="update_num",help="number_of_updates.")
    parser.add_option('-b','--bias',dest="bias",default=1,help="value_of_bias.")
    parser.add_option('-r','--regular',dest="regular",default=True,help="normalization.")
    parser.add_option('-m','--margin',dest="margin",default=True,help="margin.")
    parser.add_option('-a','--average',dest="average",default=True,help="averaged_perceptron.")
    opts, args = parser.parse_args()

    print("教師データ:"+opts.train_file)
    print("テストデータ:"+opts.test_file)
    print("学習回数:"+opts.update_num,"バイアス値:"+opts.bias,end=" ")
    print("正規化:"+opts.regular,"マージン:"+str(opts.margin),"平均化:"+str(opts.average),end="\n\n")

    #訓練データの読み込み及び並べ替え
    train_data,max_index=read_data(opts.train_file)
    random.seed(0)
    random.shuffle(train_data)

    #print(max_index,max_index_test)#教師データとテストデータの最大インデックス
    
    weight=[0]*(max_index+1)#重みベクトルの宣言(長さ=レビュー数+1(バイアス項))
    tmp_weight=[0]*(max_index+1)
    weight[0]=1
    nupdates=1#weightベクトルの更新回数+1

    #test=[0]*(max_index+1)
    
    for learned_count in range(int(opts.update_num)):
        for instances in train_data:
            nupdates=update_weight(instances[0],instances[1],max_index,nupdates)

    ave_weight=[0]*(max_index+1)
    averaged_weight(nupdates)
    #テストデータの読み込み及び並べ替え
    test_data,max_index_test=read_data(opts.test_file)

    if int(opts.margin)==1:
        correct_n,instance_n,accuracy_rate=evaluate(ave_weight,test_data,max_index)
    else:
        correct_n,instance_n,accuracy_rate=evaluate(weight,test_data,max_index)

    #print(weight[1000:1100])

    """
    for i in range(len(test)):
        test[i]=test[i]/(nupdates)
        test[i]=test[i]-ave_weight[i]
    """
    #print(ave_weight[0:100])
    #print(test[0:100])
    
    print("正解数:"+str(correct_n),"インスタンス数:"+str(instance_n),"正解率:"+str(accuracy_rate*100)+"%")

