# -*- coding: utf-8 -*-
"""
Created on Fri May 29 15:10:21 2020

@author: Steven
"""
import lsb
import math
from skimage import io
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    '''
    imageFullName : cover影像檔名
    '''
    imageFullName = "cover images.bmp"
    
    imageName = imageFullName.strip(".bmp")
    coverImage = np.asarray(io.imread(imageFullName)) #read in RGB
    print(coverImage.shape)
    
    '''
    embed
    '''
    k = 1 #要借幾個bit位數來嵌入
    total_pixel = coverImage.shape[0]*coverImage.shape[1]*coverImage.shape[2] #最多可以嵌幾個secret message
    '''
    embedding_rate : 嵌入量，數值可為0~1之間的實數
    secret_msg_length : 欲嵌入的秘訊數量(嵌入該張圖片的秘訊百分比)
    '''
    embedding_rate = 1
    secret_msg_length = math.floor(total_pixel * embedding_rate)
    
    msg = lsb.generateSecretMessage(total_pixel, math.pow(2, k), secret_msg_length) #產生秘訊
    stegoImg = lsb.embed_LSB_Alg(coverImage, k, msg, secret_msg_length) #嵌入秘訊
    print("concealed secret message image:")
    plt.figure()
    plt.imshow(stegoImg)
    plt.show() #to enable instantly show image to console
    io.imsave(imageName + "_stego.bmp", stegoImg) #儲存stego影像
    '''
    recover
    '''
    recoverImg, secret_msg_list = lsb.extract_LSB_Alg(stegoImg, k, secret_msg_length) #提取stego影像的秘訊
    print("extracted message like ...:")
    print(secret_msg_list[:10])
    