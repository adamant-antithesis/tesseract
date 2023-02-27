import pytesseract
from PIL import Image

img = Image.open('number.jpg')                                                        #name of your file
pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract\tesseract.exe"   #path to Tesseract

# custom_config = r'--oem 3'                                                          #custom config, read - https://help.ubuntu.ru/wiki/tesseract

text = pytesseract.image_to_string(img)                                               #add config=custom_config as second argument
print(text)

with open("phone_number.txt", 'w') as text_file:                                      #writing the result to a file
    text_file.write(text)
