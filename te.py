import pytesseract
from PIL import Image

aa = Image.open('test.png')
ss = pytesseract.image_to_string(aa)
print(ss)