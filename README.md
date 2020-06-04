----
## 關於本專案

This repository uses LSB-k method to embedded messages to an image, based on DeepGuidedFilter accepted by CVPR.

NO commercial used, just lecture needed.

see [paper](http://wuhuikai.me/DeepGuidedFilterProject/deep_guided_filter.pdf)

see [DeepGuidedFilter](https://github.com/wuhuikai/DeepGuidedFilter)

>這個Repository根據DeepGuidedFilter這篇論文的結果，加上資訊隱藏中的LSB-k方式進行秘密訊息的嵌入。
動機為系上多媒體系統課程之期末個人專題，為自我練習的部分，僅記錄實作結果，沒有任何商業使用。


----
## 使用方式
**以下分別介紹如何使用Cover Modification 與 Cover Synthesis的方式來使用程式**

>註 : 原始論文的程式安裝方式請參考[DeepGuidedFilter](https://github.com/wuhuikai/DeepGuidedFilter)


<h3>使用Cover Modification</h3>

  1. 下載本專案 `git clone https://github.com/stevenlin1015/LSB_k_based_on_DeepGuidedFilter.git`

  2. 使用Spyder開啟 `LSB_k_based_on_DeepGuidedFilter/ImageProcessing/DeepGuidedFilteringNetwork/`內的 **predict_cover_modification_ratio.py**、**cover_modification.py** 兩支程式

  3. 在 **predict_cover_modification_ratio.py** 按 **Ctrl + F6** 快捷鍵，要來配置執行參數
  * General settings內設定Command line options為 `--task auto_ps --img_path ../../images/auto_ps.jpg --save_folder . --model deep_guided_filter_advanced --low_size 64`，按下OK


  4.執行 **predict_cover_modification_ratio.py**，會在`LSB_k_based_on_DeepGuidedFilter/ImageProcessing/DeepGuidedFilteringNetwork/`下產生一張名為 **cover images.bmp** 的BMP影像，這張影像是我們的cover image。

  5.接著進入 **cover_modification.py** ，找到 **embedding_rate** 變數，這個是嵌入秘訊的嵌入率，可以設定為0~1之間的實數(e.g. 若只想嵌入10%的秘訊到影像中，則embedding_rate = 0.1)

  6.設定完 **embedding_rate** 後，執行 **cover_modification.py** 。

  7.會在 `LSB_k_based_on_DeepGuidedFilter/ImageProcessing/DeepGuidedFilteringNetwork/` 內，找到檔名後綴為 **xxx_stego.bmp** 的BMP影像，這個就是所產生的stego image。

<h3>使用Cover Synthesis</h3>

  1. 下載本專案 `git clone https://github.com/stevenlin1015/LSB_k_based_on_DeepGuidedFilter.git`

  2. 使用Spyder開啟 `LSB_k_based_on_DeepGuidedFilter/ImageProcessing/DeepGuidedFilteringNetwork/`內的 **predict_lsb_ratio.py** 程式

  3. 在 **predict_lsb_ratio.py** 按 **Ctrl + F6** 快捷鍵，要來配置執行參數
  * General settings內設定Command line options為 `--task auto_ps --img_path ../../images/auto_ps.jpg --save_folder . --model deep_guided_filter_advanced --low_size 64`，按下OK

  4.接著進入 **predict_lsb_ratio.py** ，找到 **embedding_rate** 變數，這個是嵌入秘訊的嵌入率，可以設定為0~1之間的實數(e.g. 若只想嵌入10%的秘訊到影像中，則embedding_rate = 0.1)

  5.執行 **predict_lsb_ratio.py**，會在`LSB_k_based_on_DeepGuidedFilter/ImageProcessing/DeepGuidedFilteringNetwork/`下產生一張名為 **auto_ps.bmp** 的BMP影像，這張影像就是我們的stego image。(auto_ps這個檔名會隨著你的輸入影像檔名改變而變動)
