import pytesseract
from PIL import Image

img = Image.open('number.jpg')                                                        #name of your file
pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract\tesseract.exe"   #path to Tesseract

text = pytesseract.image_to_string(img)
print(text)
