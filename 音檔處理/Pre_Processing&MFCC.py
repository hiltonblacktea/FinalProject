import os
import glob
from info import i, printb, printr, printp, print
from CustomUtils import load_audioFiles_saves_segments, write_sample_ids_perHive, get_samples_id_perSet, get_features_from_samples,getmusicposition

def main():
    
   #----------------------------------- parameters to change-----------------------------------#
    block_size=60 # 設定60為1個block
    path_audioFiles=getmusicposition() + '原始音檔' + os.sep  # 音頻位置
    path_save_audio_labels=os.getcwd()+'/預處理音檔' + os.sep #此檔位置 + /輸出位置
    #-------------------------------------------------------------------------------------------#
    
    if not os.path.exists(path_save_audio_labels): #確認資料夾是否存在
        os.makedirs(path_save_audio_labels)  #若無，建立資料夾
    
    audiofilenames_list = [os.path.basename(x) for x in glob.glob(path_audioFiles+'*'+'.wav')] #偵測path_audioFiles中所有 .wav的檔案
    # 原始音檔切割成60sec一個segment
    load_audioFiles_saves_segments(audiofilenames_list,path_audioFiles, path_save_audio_labels, block_size, save_audioSegments='yes')
    
    sample_ids=[os.path.basename(x) for x in glob.glob(path_save_audio_labels+'*'+'.wav')] #偵測path_save_audio_labels中所有 .wav的檔案
    # 將處理完成的音檔名稱存進.json檔案
    write_sample_ids_perHive(sample_ids , path_save_audio_labels)  
    
    #----------------------------------- parameters to change-----------------------------------#
    path_workingFolder=path_save_audio_labels  
   #-------------------------------------------------------------------------------------------#
    sample_ID = get_samples_id_perSet(path_workingFolder+'sampleID_perHive.json') 
    # MFCC 處理
    get_features_from_samples(path_workingFolder,sample_ID,'MFCCs20','NO',1)
    
    
if __name__ == "__main__":
    main()