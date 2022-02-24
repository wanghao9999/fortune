from PIL import Image
import pytesseract

#ocr实时价格
text = pytesseract.image_to_string(Image.open(r'E:\Automic_future\实时价格.png'))
print(text)
print(type(text))
