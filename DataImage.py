
import sys
from PIL import Image

def Read_image(width=4424,height=1940,columns=80,rows=12,left=120,right=120,top=120,bottom=30):
	data = []
	
	cw = int(round((width-(left+right))/columns,0))
	ch = int(round((height-(top+bottom))/rows,0))

	im = Image.open(sys.argv[1])
	pixels = im.getdata()
	plen = len(pixels)
	for cx in range(left+int(round(cw/2,0)),width-right-1,cw):
		for cy in range(top+int(round(ch/2,0)),height-bottom-1,ch):
			try:
				data.append(pixels[width*cx+cy])
			except IndexError as e:
				print('{} at {},{} or {}/{}'.format(e,cx,cy,width*cx+cy,plen))

	with open('output.txt','w') as f:
		f.write(repr(data))
Read_image()
