#! /usr/local/bin/python3
from PIL import Image, ImageDraw
from random import randint
from math import sqrt
import sys

GIVEBEE_BLACK = '#443822'
PERCENT_OF_SCREEN = 0.034

def drawx36(beeLogo, instaPhoto):
	beeLogoDynamic = dynamic(beeLogo, instaPhoto)
	beeLogoHeight, beeLogoWidth = beeLogoDynamic.size
	beeLogoDraw = ImageDraw.Draw(beeLogoDynamic)
	baseB = beeLogoHeight * 0.35
	index = 0
	with open('log.txt', 'r') as l:
		for line in l:
			for i in range(6):
				baseB += int((beeLogoWidth*0.5-beeLogoWidth*0.1)/5)
				for baseA in range(int(beeLogoWidth*0.055),int(beeLogoWidth*0.5),int((beeLogoWidth*0.5-beeLogoWidth*0.1)/5)):
					if line[index] != '0':
						beeLogoDraw.ellipse((baseA, baseB, baseA+int((beeLogoWidth*0.5-beeLogoWidth*0.1)/10), baseB+int((beeLogoWidth*0.5-beeLogoWidth*0.1)/10)), fill=GIVEBEE_BLACK)
					index += 1
	beeLogoDynamic.save('test.png')
	return beeLogoDynamic

def drawx25(beeLogo, instaPhoto):
	beeLogoDynamic = dynamic(beeLogo, instaPhoto)
	beeLogoHeight, beeLogoWidth = beeLogoDynamic.size
	beeLogoDraw = ImageDraw.Draw(beeLogoDynamic)
	baseB = beeLogoHeight * 0.36
	index = 0
	with open('log.txt', 'r') as l:
		for line in l:
			for i in range(5):
				baseB += int((beeLogoWidth*0.5-beeLogoWidth*0.1)/4.5)
				for baseA in range(int(beeLogoWidth*0.08),int(beeLogoWidth*0.45),int((beeLogoWidth*0.5-beeLogoWidth*0.1)/4.5)):
					if line[index] != '0':
						beeLogoDraw.ellipse((baseA, baseB, baseA+int((beeLogoWidth*0.5-beeLogoWidth*0.1)/9), baseB+int((beeLogoWidth*0.5-beeLogoWidth*0.1)/9)), fill=GIVEBEE_BLACK)
					index += 1
	beeLogoDynamic.save('test.png')
	return beeLogoDynamic

def dynamic(beeLogo, instaPhoto):
	beeLogoHeight, beeLogoWidth = beeLogo.size
	instaPhotoHeight, instaPhotoWidth = instaPhoto.size
	resizeRatio = min((instaPhotoWidth*sqrt(PERCENT_OF_SCREEN))/beeLogoWidth, (instaPhotoHeight*sqrt(PERCENT_OF_SCREEN))/beeLogoHeight)
	beeLogoDynamic = beeLogo.resize((int(beeLogoHeight * resizeRatio), int(beeLogoWidth * resizeRatio)))
	return beeLogoDynamic

def overlay_logo(beeLogo, instaPhoto):
	beeLogoHeight, beeLogoWidth = beeLogo.size
	instaPhotoHeight, instaPhotoWidth = instaPhoto.size
	instaPhoto.paste(beeLogo, (instaPhotoHeight - beeLogoHeight, instaPhotoWidth - beeLogoWidth), beeLogo)
	instaPhoto.save('test0.png')

def write_log(user_id):
	with open('log.txt', 'w') as log:
		print(pad_user_id(str(bin(user_id))[2:]))
		log.write(pad_user_id(str(bin(user_id))[2:]))

def pad_user_id(user_id):
	while len(user_id) < 25:
		user_id = '0' + user_id
	return user_id

def main():

	user_id = int(sys.argv[3])

	write_log(user_id)

	if len(sys.argv) < 2:
		beeLogo = Image.open('./images/bee3x.png')
	else:
		if sys.argv[1] == '1':
			beeLogo = Image.open('./images/bee1x.png')
		elif sys.argv[1] == '2':
			beeLogo = Image.open('./images/bee2x.png')
		elif sys.argv[1] == '3':
			beeLogo = Image.open('./images/bee3x.png')
		else:
			sys.exit("incorrect asset size, try 1, 2, 3")

	instaPhoto = Image.open('./images/insta2.jpg')

	if len(sys.argv) < 3:
		overlay_logo(drawx25(beeLogo, instaPhoto), instaPhoto)
	else: 
		if sys.argv[2] == '25' or sys.argv[2] == '5':
			overlay_logo(drawx25(beeLogo, instaPhoto), instaPhoto)
		elif sys.argv[2] == '36' or sys.argv[2] == '6':
			overlay_logo(drawx36(beeLogo, instaPhoto), instaPhoto)
		else: 
			sys.exit("incorrect dot count, try 25, 36")

main()