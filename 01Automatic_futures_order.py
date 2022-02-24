#!usr/bin/env python
# -*- coding utf-8 -*-
#goal:根据期货实时价格，实现实时下单操作
#author : whaty_how


import pyautogui 
import time

#记录程序运行时长
start_time = time.time()



#第一部分，价格获取
#截取价格图片
pyautogui.hotkey('alt','tab')
pyautogui.screenshot(r'E:\automic_future\价格.png',region=(0,0,500,700))

end_time = time.time()  

duartion = round(end_time - start_time,3)
pyautogui.alert(title='',text='运行时长',button= duartion)
 




# 及分析
# 每隔1秒钟获取一次价格


#第二部分，自动下单操作

##点击下单


#下单坐标
# pyautogui.position()
# xy = 234

# pyautogui.click()

