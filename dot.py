#! /usr/local/bin/python3
from PIL import Image, ImageDraw
from random import randint
from math import sqrt
import sys

GIVEBEE_BLACK = '#443822'
PERCENT_OF_SCREEN = 0.034

def draw3x(beeLogo, instaPhoto):
	beeLogoDraw = ImageDraw.Draw(beeLogo)
	baseB = 66
	baseD = 74
	for i in range(6):
		baseB += 16
		baseD += 16
		for a in range(12,100,16):
			if randint(0,10) < 7:
				beeLogoDraw.ellipse((a, baseB, a+8, baseD), fill=GIVEBEE_BLACK)
	return dynamic(beeLogo, instaPhoto)

def draw2x(beeLogo, instaPhoto):
	beeLogoDraw = ImageDraw.Draw(beeLogo)
	baseB = 46
	baseD = 51
	for i in range(6):
		baseB += 10
		baseD += 10
		for a in range(10,61,10):
			if randint(0,10) < 7:
				beeLogoDraw.ellipse((a, baseB, a+5, baseD), fill=GIVEBEE_BLACK)
	return dynamic(beeLogo, instaPhoto)

def draw1x(beeLogo, instaPhoto):
	beeLogoDraw = ImageDraw.Draw(beeLogo)
	baseB = 23
	baseD = 26
	for i in range(6):
		baseB += 5
		baseD += 5
		for a in range(5,33,5):
			if randint(0,10) < 7:
				beeLogoDraw.ellipse((a, baseB, a+3, baseD), fill=GIVEBEE_BLACK)
	return dynamic(beeLogo, instaPhoto)

def dynamic(beeLogo, instaPhoto):
	beeLogoHeight, beeLogoWidth = beeLogo.size
	instaPhotoHeight, instaPhotoWidth = instaPhoto.size
	resizeRatio = min((instaPhotoWidth*sqrt(PERCENT_OF_SCREEN))/beeLogoWidth, (instaPhotoHeight*sqrt(PERCENT_OF_SCREEN))/beeLogoHeight)
	beeLogoDynamic = beeLogo.resize((int(beeLogoHeight * resizeRatio), int(beeLogoWidth * resizeRatio)))
	beeLogoDynamic.save('test.png')
	return beeLogoDynamic

def overlay_logo(beeLogo, instaPhoto):
	beeLogoHeight, beeLogoWidth = beeLogo.size
	instaPhotoHeight, instaPhotoWidth = instaPhoto.size
	instaPhoto.paste(beeLogo, (instaPhotoHeight - beeLogoHeight, instaPhotoWidth - beeLogoWidth), beeLogo)
	instaPhoto.save('test0.png')

def main():

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

	if len(sys.argv) < 2:
		beeLogoDynamic = draw3x(beeLogo, instaPhoto)
	else:
		if sys.argv[1] == '1':
			beeLogoDynamic = draw1x(beeLogo, instaPhoto)
		elif sys.argv[1] == '2':
			beeLogoDynamic = draw2x(beeLogo, instaPhoto)
		elif sys.argv[1] == '3':
			beeLogoDynamic = draw3x(beeLogo, instaPhoto)
		else:
			sys.exit("incorrect asset size, try 1, 2, 3")

	overlay_logo(beeLogoDynamic, instaPhoto)

main()