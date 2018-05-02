from PIL import Image
#from pytesseract import image_to_string
import pytesseract
# import argparse
import cv2

import matplotlib.pyplot as plt

colored_img = cv2.imread('contoured.jpg')
img_copy = colored_img.copy()
gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

gray1 = cv2.threshold(gray , 0 , 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#gray = cv2.medianBlur(gray, 3)

#gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

gray2 = cv2.adaptiveThreshold(gray ,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,25,13)

blur = cv2.GaussianBlur(img_copy, (5,5), 0)
res3, gray3 = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imwrite('test1.png', gray1)
cv2.imwrite('test2.png', gray2)

plt.imshow(gray2)

#print "thresold reating: ", res3
cv2.imwrite('test3.png',gray3)

#img = Image.open('contoured.jpg')
#img = img.convert('RGBA')
#pix = img.load()
#
#for y in range(img.size[1]):
#    for x in range(img.size[0]):
#        if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
#            pix[x, y] = (0, 0, 0, 255)
#        else:
#            pix[x, y] = (255, 255, 255, 255)
#
#img.save('temp.png')

text = pytesseract.image_to_string(Image.open('test2.png'))
#print "----->", text

import re
text = re.sub('\n\n', '', text)
print text

#text = ''.join([i for i in text if i.isalpha()])

print text

#text = text.replace('\n', '')
#print text

new_file = open('new_fl6.txt','w')
new_file.write(text)



#lines = new_file.readlines()
#for i in lines:
#    print i


#text = image_to_string(Image.open('sample_img.jpg'))
# print image_to_string(Image.open('test-english.jpg'), lang='eng')
#print text

#print image_to_string(Image.open('samp_num.jpg'))


