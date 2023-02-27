import pytesseract
from PIL import Image

# example with number

img = Image.open('number_example.jpg')                                                #name of your file
pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract\tesseract.exe"   #path to Tesseract

# custom_config = r'--oem 3'                                                          #custom config, read - https://github.com/tesseract-ocr/tesseract/blob/main/doc/tesseract.1.asc

number = pytesseract.image_to_string(img)                                             #add config=custom_config as second argument
print(number)

with open("phone_number.txt", 'w') as text_file:                                      #writing the result to a file
    text_file.write(number)

# example with text

img = Image.open('text_example.png')

custom_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(img, config=custom_config)
print(text)

with open("text.txt", 'w') as text_file:
    text_file.write(text)

#example with dictionarys

#you need to download a dictionary - https://github.com/tesseract-ocr/tessdata and drop it to root of Tesseract
#path example - D:\Program Files\Tesseract\tessdata

img = Image.open('ukrainian_example.jpg')

custom_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(img, lang='ukr', config=custom_config)
print(text)

with open("ukrainian_example.txt", 'w') as text_file:
    text_file.write(text)