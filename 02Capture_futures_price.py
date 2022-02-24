#!usr/bin/env python
# -*- coding utf-8 -*-
#goal:获取期货成交明细
#author : whaty_how

from PIL import Image
import pyautogui 
import time
import pytesseract
import xlwings as xw


#记录程序开始运行时间
start_time = time.time()

#第一步：截取价格图片
pyautogui.hotkey('alt','tab')
pyautogui.screenshot(r'E:\Automic_future\实时价格.png',region=(31,192,270,313))

#第二步：ocr实时价格
now_price = pytesseract.image_to_string(Image.open(r'E:\Automic_future\实时价格.png'))
print(now_price)
print(type(now_price))

#第三步：写入excle实时价格
##建立工作表连接
wb =xw.Book("E:\Automic_future\实时价格_20220224.xlsx")
##实例化工作表
sheet = wb.sheets["sheet1"]
#写入
sheet.range('A1').value = now_price


#记录程序结束运行时间
end_time = time.time()  

duartion = round(end_time - start_time,3)
pyautogui.alert(title='',text='运行时长',button= duartion)