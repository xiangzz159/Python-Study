# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'图片转文字图像'

from PIL import Image


IMG = 'ascii_dora.png'

ascii_char1 = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
ascii_char2 = ' `01'
count1 = len(ascii_char1)
count2 = len(ascii_char2)

def img2str1():
    im = Image.open(IMG).resize((153, 153), Image.NEAREST)
    txt = ""
    for i in range(im.size[1]):
        for j in range(im.size[0]):
            txt += get_char1(*im.getpixel((j, i)))
        txt += '\n'

    print(txt)
    f = open("output1.txt", 'w')
    f.write(txt)
    f.close()

def get_char1(r,b,g,alpha = 256):
	if alpha == 0:
		return ' '
	gray = int(0.2126*r+0.7152*g+0.0722*b)

	unit = (256.0+1)/count1
	return ascii_char1[int(gray/unit)]


def img2str2():
    im = open_img(IMG)
    im = im.convert("L")  # 转灰度
    # im.save("./resource/img2gray.jpg")
    print(u"Width:" + str(im.size[0]) + ' Height:' + str(im.size[1]))
    txt = ""
    for i in range(im.size[1]):
        for j in range(im.size[0]):
            gray = im.getpixel((j, i))
            txt += ascii_char2[int(((count2 - 1) * gray) / 256)]
        txt += '\n'

    print(txt)
    f = open("output2.txt", 'w')
    f.write(txt)
    f.close()

def open_img(image_path):
    im = Image.open(image_path)
    if im.size[0]>1000 or im.size[1]>1000:
        im = im.resize((int(im.size[0] * 0.1), int(im.size[1] * 0.05)), Image.NEAREST)
    return im



if __name__ == '__main__':
    img2str1()
    img2str2()
