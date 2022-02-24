# import pyautogui
# currentMouseX, currentMouseY = pyautogui.position() # 鼠标当前位置
# print(currentMouseX, currentMouseY)



from PIL import Image
import pytesseract
 
text = pytesseract.image_to_string(Image.open(r'E:\automic_future\价格.png'))
print(text)