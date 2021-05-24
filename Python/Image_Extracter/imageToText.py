import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Lenovo\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open('Met-Max.png')
text = tess.image_to_string(img)

print(text.upper())
