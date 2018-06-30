#! /usr/local/bin/python3
from PIL import Image, ImageDraw
from random import randint
import sys

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
		sys.exit("INCORRECT BEE SIZE")

instaPhoto = Image.open('./images/insta0.jpg')
save_image_filename = 'test.png'

beeLogoHeight, beeLogoWidth = beeLogo.size
instaPhotoHeight, instaPhotoWidth = instaPhoto.size

giveBee_black = '#443822'

def draw3x():
	beeLogoDraw = ImageDraw.Draw(beeLogo)
	baseB = 66
	baseD = 74
	for i in range(6):
		baseB += 16
		baseD += 16
		for a in range(12,100,16):
			if randint(0,10) < 7:
				beeLogoDraw.ellipse((a, baseB, a+8, baseD), fill=giveBee_black)
	beeLogo.save(save_image_filename)

def draw2x():
	beeLogoDraw = ImageDraw.Draw(beeLogo)
	baseB = 46
	baseD = 51
	for i in range(6):
		baseB += 10
		baseD += 10
		for a in range(10,61,10):
			if randint(0,10) < 7:
				beeLogoDraw.ellipse((a, baseB, a+5, baseD), fill=giveBee_black)
	beeLogo.save(save_image_filename)

def draw1x():
	beeLogoDraw = ImageDraw.Draw(beeLogo)
	baseB = 23
	baseD = 26
	for i in range(6):
		baseB += 5
		baseD += 5
		for a in range(5,33,5):
			if randint(0,10) < 7:
				beeLogoDraw.ellipse((a, baseB, a+3, baseD), fill=giveBee_black)
	beeLogo.save(save_image_filename)

def overlay_logo():
	instaPhoto.paste(beeLogo, (instaPhotoHeight - beeLogoHeight, instaPhotoWidth - beeLogoWidth), beeLogo)
	instaPhoto.save('test0.png')

def main():

	if len(sys.argv) < 2:
		beeLogo = Image.open('./images/bee3x.png')
	else:
		if sys.argv[1] == '1':
			draw1x()
		elif sys.argv[1] == '2':
			draw2x()
		elif sys.argv[1] == '3':
			draw3x()
		else:
			sys.exit("INCORRECT BEE SIZE")
	
	overlay_logo()

main()