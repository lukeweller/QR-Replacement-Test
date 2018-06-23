#! /usr/local/bin/python3
from PIL import Image

beeLogo = Image.open('./images/GiveBee_BuzzyPhoto.png')
readBee = Image.open('test0.png')

beeLogoWidth, beeLogoHeight = beeLogo.size
readBeeWidth, readBeeHeight = readBee.size

# print(readBeeWidth)
# print(readBeeHeight)
# print(readBeeWidth- beeLogoWidth)
# print(readBeeHeight- beeLogoHeight)

readBee = readBee.crop((readBeeWidth - beeLogoWidth, readBeeHeight - beeLogoHeight, readBeeWidth, readBeeHeight))

# readBee.save('test1.png')

binary_string = ''
with open('log.txt','r') as r:
	for line in r:
		y,x = line.split(',')
		p = readBee.getpixel((int(y),int(x[:-1])))
		if p[0] != 255:
			binary_string += "1"
		else:
			binary_string += "0"

print(hex(int(binary_string)))
