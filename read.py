#! /usr/local/bin/python3
from PIL import Image
import config

GIVEBEE_BLACK = config.GIVEBEE_BLACK
PERCENT_OF_SCREEN = config.PERCENT_OF_SCREEN

def crop_to_bee(readPhoto, beeLogo):
	readPhotoHeight, readPhotoWidth = readPhoto.size
	beeLogoHeight, beeLogoWidth = beeLogo.size
	croppedBee = readPhoto.crop((readPhotoHeight - beeLogoHeight, readPhotoWidth - beeLogoWidth, readPhotoHeight, readPhotoWidth))
	return croppedBee.crop((beeLogoHeight*0.04,beeLogoWidth*0.37,beeLogoHeight*0.55, beeLogoWidth*0.83))

def more_jpeg(croppedBee):
	return croppedBee.resize((6,6))

def read_pixel_by_pixel(croppedBee):
	binstring = ''
	croppedBeeWidth, croppedBeeHeight = croppedBee.size
	for x in range(croppedBeeWidth):
		for y in range(croppedBeeHeight):
			r,g,b = croppedBee.getpixel((y,x))
			if rgb2hex(r,g,b) == config.GIVEBEE_BLACK:
				binstring += '1'
			else:
				binstring += '0'
	return binstring

def write_readlog(binstring):
	with open('readlog.txt', 'w') as readlog:
		readlog.write(binstring)
	with open('readlog_id.txt', 'w') as readlog_id:
		readlog_id.write(str(int(binstring, 2)))

def rgb2hex(r,g,b):
    return '#{:02x}{:02x}{:02x}'.format(r,g,b)

def main():
	readPhoto = Image.open('test0.png')
	beeLogo = Image.open('test.png')
	croppedBee = more_jpeg(crop_to_bee(readPhoto, beeLogo))
	croppedBee.save('test1.png')
	write_readlog(read_pixel_by_pixel(croppedBee))

main()


