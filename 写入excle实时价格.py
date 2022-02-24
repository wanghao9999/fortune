#!usr/bin/env python
# -*- coding utf-8 -*-
#author : whaty_how

import xlwings as  xw
import time 

#写入excle实时价格

##建立工作表连接
wb =xw.Book("E:\Automic_future\实时价格_20220224.xlsx")

##实例化工作表
sheet = wb.sheets["sheet1"]

now_price = [1,2,'c']
sheet.range('A1').value = now_price