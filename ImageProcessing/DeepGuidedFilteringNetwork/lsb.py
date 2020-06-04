# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:23:14 2020

@author: Steven
"""

from PIL import Image
import numpy as np
import random
import math
import matplotlib.pyplot as plt
'''
產生秘訊
    參數:
        -max_m : 範圍為2^k-1的隨機數(參考老師講義)
        -secret_msg_length : 長度secret_msg_length的總長度
    回傳值:
        -secret_msg_list : 一串長度為secret_msg_length的秘訊
'''
def generateSecretMessage(max_m, secret_msg_length):
    #設定隨機種子，使每一次產生的秘訊皆一致
    random.seed(10)
    secret_msg_list = [random.randint(0, max_m - 1) for p in range(0, secret_msg_length)] #產生長度為secret_msg_length的秘訊
    
    #顯示前10筆秘訊
    print("\nembedded message like ...:")
    print(secret_msg_list[:10])

    return secret_msg_list
'''
嵌入秘訊
    參數:
        -pixel : 欲嵌入的pixel值
        -k : 嵌入的bit位數
        -m : 欲嵌入的秘訊
    回傳值:
        -pixel_comma : 嵌完秘訊的pixel值
'''
def embedSecretMessage(pixel, k, m):
    
    pixel_c = int(pixel - (pixel % math.pow(2,k))) #清空後面的位元
    pixel_comma = pixel_c + m #嵌入秘訊
    
    return pixel_comma
'''
提取秘訊
    參數:
        -pixel_comma : 嵌完秘訊的pixel值
        -k : 嵌入的bit位數
    回傳值:
        -recover_pixel : 提取完秘訊的pixel值
        -secret_msg : 提取出來的秘訊
'''
def extractSecretMessage(pixel_comma, k):
    secret_msg = int(pixel_comma % math.pow(2, k)) #根據k值算出秘訊
    recover_pixel = pixel_comma - secret_msg #刪去秘訊後的像素值
    
    return recover_pixel, secret_msg
'''
LSB-k 嵌入演算法
    參數:
        -img : 欲嵌入的影像
        -k : 嵌入的bit位數
        -msg : 欲嵌入的秘訊
        -secret_msg_length : 欲嵌入的秘訊總長度
    回傳值:
        -stegoImg : 嵌入完的stego影像
'''
def embed_LSB_Alg(img, k, msg, secret_msg_length):
    #建立空白stego影像
    stegoImg = np.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype = np.uint8)

    index = 0 #計算秘訊嵌入了多少個
    for channel in range(img.shape[2]):
        for height in range(img.shape[0]):
            for width in range(img.shape[1]):
                if (secret_msg_length - 1 >= index): #秘訊仍可被嵌入
                    pixel_comma = embedSecretMessage(img[height, width, channel], k, msg[index])
                    index += 1
                    stegoImg[height, width, channel] = pixel_comma
                else: #秘訊已嵌入完成，填補原像素值
                    stegoImg[height, width, channel] = img[height, width, channel]
                
    #plt.imshow(stegoImg)
    return stegoImg
'''
LSB-k 提取演算法
    參數:
        -stegoImg : stego影像
        -k : 嵌入的bit位數
        -secret_msg_length : 已嵌入的秘訊總長度
    回傳值:
        -recoverImg : 提取完的stego影像(沒有用途)
        -secret_msg_list : 提取出來的秘訊
'''
def extract_LSB_Alg(stegoImg, k, secret_msg_length):
    #建立空白提取完成的影像
    recoverImg = np.zeros((stegoImg.shape[0], stegoImg.shape[1], stegoImg.shape[2]), dtype = np.uint8)
    #提取出來的秘訊
    secret_msg_list = []
    
    for channel in range(stegoImg.shape[2]):
        for height in range(stegoImg.shape[0]):
            for width in range(stegoImg.shape[1]):
                if (len(secret_msg_list) < secret_msg_length): #秘訊尚未提取完成
                    recover_pixel, secret_msg = extractSecretMessage(stegoImg[height, width, channel], k) #提取秘訊
                
                    recoverImg[height, width, channel] = recover_pixel #填補提取完秘訊的像素
                    secret_msg_list.append(secret_msg) #將提取出來的秘訊儲存
                else: #秘訊已提取完成
                    recoverImg[height, width, channel] = stegoImg[height, width, channel]

    #plt.imshow(recoverImg)
    return recoverImg, secret_msg_list

if __name__ == "__main__":
    #embed
    '''
    k : 要借幾個bit位數來嵌入
    '''
    k = 1
    img = np.asarray(Image.open("../../images/auto_ps.jpg").convert('RGB'))
    total_pixel = img.shape[0]*img.shape[1]*img.shape[2]
    '''
    embedding_rate : 嵌入量，數值可為0~1之間的實數
    secret_msg_length : 欲嵌入的秘訊數量(嵌入該張圖片的秘訊百分比)
    '''
    embedding_rate = 0.5
    secret_msg_length = math.floor(total_pixel * embedding_rate)
    
    msg = generateSecretMessage(math.pow(2, k), secret_msg_length) #產生秘訊
    stegoImg = embed_LSB_Alg(img, k, msg, secret_msg_length) #嵌入秘訊
    Image.fromarray(stegoImg).save('stego.png') #DO NOT SAVE .jpg, IT WILL COMPRESS IMAGE RGB VALUE
    
    #recover
    stegoImg = np.asarray(Image.open("stego.png").convert('RGB')) #讀入stego影像
    recoverImg, secret_msg_list = extract_LSB_Alg(stegoImg, k, secret_msg_length) #提取stego影像的秘訊

    #顯示提取出來的前10筆秘訊
    print("extracted message like ...:")
    print(secret_msg_list[:10])
    