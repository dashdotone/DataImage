import sys
import os
from PIL import Image

def Punchcard_read(img,columns=80,rows=12,left=120,right=120,top=20,bottom=90):
	alpha = {'010010000000': 'k', '010100000000': 'j', '001000000001': 'z', '100000000100': 'g', '001000001010': '>', '010010000010': '!', '001000000010': 'y', '000001000010': '#', '000000000001': '9', '100000000110': '|', '100000000010': 'h', '001000000000': '0', '100000010010': '(', '010000000010': 'q', '100000000000': '&', '010000000000': '-', '000010000010':':', '001000000110': '?', '010000100000': 'm', '010000000100': 'p', '010000010010': ')', '001100000000': '/', '001000100010': '%', '000000001010': '=', '000000000110': '"', '100001000010': '.', '100100000000': 'a', '000000000010': '8', '000000000100': '7', '010001000010': '$', '100010000010': 'c', '001001000000': 't', '000000010010': "'", '000001000000': '3', '000000100010': '@', '100001000000': 'c', '010000000001': 'r', '000000010000': '5', '010001000000': 'l', '100000000001': 'i', '000000100000': '4', '100000100010': '<', '100000100000': 'd', '001000001000': 'w', '001000010000': 'v', '001000100000': 'u', '000100000000': '1', '100000001000': 'f', '000010000000': '2', '100000010000': 'e', '001000010010': '_', '010000001000': 'o', '010000100010': '*', '001010000000': 's', '001000000100': 'x', '001001000010': ',', '010000010000': 'n', '010000001010': ';', '100010000000': 'b', '000000001000': '6', '100000001010': '+','000000000000':' '}
	im = Image.open(img)
	width, height = im.size
	cell_width = int(round((width-(left+right))/(columns)))
	cell_height = int(round((height-(top+bottom))/(rows)))
	
	data = []
	
	x_i = 0
	for x in range(left,width-right):
		if x % cell_width == 0:
			data.append([])
			for y in range(top,height-bottom):
				pix = im.getpixel((x,y))
				if y % cell_height == 0:
					if pix == (0,0,0):
						data[x_i].append(1)
					else:
						data[x_i].append(0)
			x_i+=1
	
	for i in range(0,len(data)):
		for i2 in range(0,len(data[i])):
			data[i][i2] = str(data[i][i2])
		binary = ''.join(data[i])
		try:
			data[i] = binary.replace(binary,alpha[binary])
		except KeyError as e:
			print('{} at {}'.format(e,i))
	
	return ''.join(data)

def Grandpa():
	print(Punchcard_read(sys.argv[2]))

def Grandpa_again():
	cards = []
	for arg in sys.argv[2:]:
		cards.append(Punchcard_read(arg))
	
	for i in range(1,7):
		for card in cards:
			if int(card[-2:]) == i*10:
				print(card[:-8])
	print('Run this program at https://www.codechef.com/ide/')

def main():	
	if len(sys.argv) > 1:
		if sys.argv[1] == '-g':
			Grandpa()
		elif sys.argv[1] == '-ga':
			Grandpa_again()

if __name__ == '__main__':
	main()
	
