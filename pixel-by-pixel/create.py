#! /usr/local/bin/python3
from PIL import Image
from random import randint

username = 'luke'
beeLogo = Image.open('./images/bee1x.png')
instaPhoto = Image.open('./images/insta0.jpg')

write_new_log_bool = True
log_filename = 'log.txt'
save_image_filename = 'test.png'
key_filename = 'key.txt'

beeLogoHeight, beeLogoWidth = beeLogo.size
instaPhotoHeight, instaPhotoWidth = instaPhoto.size

def username_to_binary(username):
	for i in range(16-len(username)):
		username += " "
	print(bin(int.from_bytes(username.encode(), 'big')))
	print(len(bin(int.from_bytes(username.encode(), 'big'))))

def rand_pix(x,y):
	r = randint(0,1)
	if r < 1:
		beeLogo.putpixel((x,y) , (255,255,255,255))
		return "0"
	else:
		beeLogo.putpixel((x,y) , (68,56,51,255))
		return "1"

def write_new_log(log_filename):
	pix_change_counter = 0
	with open(log_filename, 'w') as l:
		for x in range(0, int(beeLogoWidth*0.6)):
			for y in range(int(beeLogoHeight*0.25), int(beeLogoHeight*0.75)):
				p = beeLogo.getpixel((y,x))
				if p[0] > 180 and p[1] > 180 and p[2] > 180 and p[3] > 0:
					l.write('{},{}\n'.format(y,x))
					pix_change_counter += 1
	print('Pixel change cnt: {}'.format(pix_change_counter))

def create_new_image(log_filename, image_filename):
	binary_string= ""
	with open(log_filename,'r') as r:
		for line in r:
			y,x = line.split(',')
			binary_string += rand_pix(int(y),int(x[:-1]))
	beeLogo.save(image_filename)
	print(len(binary_string))
	return hex(int(binary_string))

def overlay_logo():
	instaPhoto.paste(beeLogo, (instaPhotoHeight - beeLogoHeight, instaPhotoWidth - beeLogoWidth), beeLogo)
	instaPhoto.save('test0.png')


def main():

	username_to_binary(username)

	if write_new_log_bool:
		write_new_log(log_filename)

	with open(key_filename, 'w') as k:
		k.write(create_new_image(log_filename, save_image_filename))

	overlay_logo()


main()
