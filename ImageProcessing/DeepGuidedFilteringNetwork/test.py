# -*- coding: utf-8 -*-
"""
Created on Tue May 19 20:33:31 2020

@author: hsueh
"""
from PIL import Image
import numpy as np
import random
import math
from matplotlib.pyplot import imshow

total_message = 5

secret_msg_list = [random.randint(0, 2 - 1) for p in range(0, total_message)]

print(secret_msg_list)

print(len(secret_msg_list))