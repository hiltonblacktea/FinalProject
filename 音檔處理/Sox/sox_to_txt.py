# 自動將新加入的音檔轉換成txt(使用sox) 
# 有使用到 sox 執行上windows不支援 -> 使用 gitbash環境來解決
import os , time
import sys
def main():
    
    count = 0 #計算此次處理檔案數量
    
    fileposition = soundposition() +os.sep# 要處理的音檔位置
    fileList = os.listdir(fileposition) # 取得音檔list
    
    storeposition = os.getcwd() + os.sep + 'sound_data' + os.sep # 要存放處理完成data位置
    storeList = os.listdir(storeposition) #取得先前完成的data , 用來判斷音檔有無處理過

    for filename in fileList:
        
        if filename[0:-4] + '.txt' in storeList:
            print('this sound has been used')
            continue

        if filename.endswith(".wav"):
            count += 1
            name = filename.replace('.wav','.txt')
            Sox = 'sox '+fileposition + filename+" -n stat -freq 2>&1 | sed -n -e :a -e '1,15!{P;N;D;};N;ba' | cat > " + storeposition + name
            # sox 音檔位置(跟程式放不同地方要給絕對路徑) -n ... -> 取得頻率&能量+統計資訊 | sed ... -> 去除最後統計資訊 | cat > 要儲存txt的位置
            os.popen(Sox)
            
    print(str(count)+" files have been converted ")

def soundposition():
    # 取得此刻檔案名
    filename = os.getcwd().split(os.sep)[-1]
    getposition = os.getcwd().replace(filename,'')
    return getposition + '預處理音檔'
if __name__ == '__main__':
    main()