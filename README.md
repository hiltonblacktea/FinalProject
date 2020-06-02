# FinalProject
畢業專題 : 蜂箱數據分析

專案架構介紹:

- 使用樹梅派+溫濕度感測器+聲音傳感器收集資訊並定時上傳至雲端空間

- 使用LineNotify功能,定時從DB取出當時溫溼度,當有異狀則自動透過Line通報蜂農異狀(Line_Notify.py)

- 將載下的音檔使用兩種方式轉換成 " 頻率 : 強度 " 為後續機器學習的特徵值 
(使用音檔來源:https://www.dropbox.com/sh/us1633xi4cmtecl/AAA6hplscuDR7aS_f73oRNyha?dl=0)
    - Sox : 撰寫python腳本 
        - 腳本1(sox_to_txt.py) : 自動批次將 (預處理完成)音檔載入-> 音檔轉換成[頻率:強度] -> 匯出成txt檔案備用
        - 腳本2(txt_to_xlsx.py) : 自動批次將 txt檔案載入 -> 將同頻率之強度加總 -> 取所需頻率範圍(0~700) -> 正規化(*備註1) -> 匯出成xlsx檔案供後續機器學習使用
    - MFCC : 撰寫python腳本( MFCC功能參考自:https://www.researchgate.net/publication/328997207_To_bee_or_not_to_bee_Investigating_machine_learning_approaches_for_beehive_sound_recognition)
        - 腳本(Pre_processing&MFCC.py) : 自動批次將 原始音檔載入 -> 音檔切割成60sec一個segment並存入預處理音檔資料夾 ->  執行音檔轉換成MFCC(梅爾倒譜頻率之強度)(*備註2) -> 匯出成xlsx檔案供後續機器學習
          使用(所有MFCC轉換皆以python函式庫Librosa進行)

- 使用先前處理完成的特徵檔案,進行機器學習建模以及預測分析(使用 MLP & PCA & SVM 三種技術)(*備註3)
    - MLP : 使用 keras 進行建模、預測
        1. 匯入資料集、篩選所需欄位資料、隨機切割訓練集&測試集(80% : 20%)
        2. 將狀態(label)區分,對應數值( 正常 = 0 : 失王 = 1 )
        3. 建立MLP模型,設定輸入層(131個神經元)、隱藏層(40個神經元)、輸出層(1個神經元)
        4. 查看訓練集準確率&誤差率、模型準確率查看,並將模型儲存供下次使用
        5. 新資料匯入訓練好模型進行預測,取得預測結果
      
    - PCA&SVM : 使用 scikit-learn 進行機器學習降維、分類
        1. 匯入資料集、篩選所需欄位資料
        2. 透過PCA降維並顯示降維成果查看降維效果
        3. 隨機切割訓練集&測試集(80% : 20%)
        4. 建立SVM模型進行預測
        5. 查看預測結果


*備註1 : 
    將所有強度數值收斂在0~1之間,Sox軟體轉檔上自動調整音檔音量大小導致各檔案強度調整,故使其收斂去除誤差問題。
    
*備註2 : 
    MFCC即是梅爾頻率倒譜,透過此方法可以將難以使用的時域音訊分解、強化、傅立葉轉換成容易使用的[梅爾頻率:能量]達到後續方便利用 , 其原理: 將連續音訊切割成多個訊框 -> 預強化將原先壓抑的高音部分凸顯 -> 傅立葉轉換
將訊號時域轉換成頻域能量 -> 透過梅爾濾波器、梅爾刻度上提取對數能量 -> 離散傅立葉轉換為倒頻譜域 -> 得到MFCC即是倒頻譜域的能量。

*備註3 : 
    MLP(Multilayer perceptron) : 多層感知器 , 一種監督式學習 ，透過從資料集中的特徵值(features)跟與之對應到的標籤(labels)學習。
        過程透過自動調整特徵值與標籤間對應關係的權重進行學習。學習完成能對沒有標籤的新資料進行預測。
        主要包含三種類神經網路 層: 輸入層、隱藏層、輸出層。 
    
    PCA(Principal components analysis) : 主成分分析 , 一種統計分析、簡化數據集的方法, 主要用於減少數據集的維數，同時保留數據集當中對變異數貢獻最大的特徵。
    
    SVM(Support Vector Machine) : 支持向量機 , 基於統計理論上的一種監督式機器學習方法，常用在統計分析及迴歸分析中。
    其目的為找出一個分類函數或是分類模型，又以二分類的模型最常見，意即在數據點中找出一個超平面使數據中的不同類別可以區隔開來。
    
    