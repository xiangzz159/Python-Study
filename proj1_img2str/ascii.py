# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'图片转文字图像'

from PIL import Image


IMG = 'ascii_dora.png'

ascii_char = ' `01'
count = len(ascii_char)


def get_char(r, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.7278 * r + 0.1722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]

def open_img(image_path):
    im = Image.open(image_path).convert('L')   # 打开图像并转灰度
    if im.size[0]>1000 or im.size[1]>1000:
        im = im.resize((int(im.size[0] * 0.1), int(im.size[1] * 0.05)), Image.NEAREST)
    return im

if __name__ == '__main__':
    im = open_img(IMG)
    # im.save("./resource/img2gray.jpg")
    print(u"Width:"+str(im.size[0])+' Height:'+str(im.size[1]))
    txt = ""
    for i in range(im.size[1]):
        for j in range(im.size[0]):
            gray = im.getpixel((j, i))
            txt += ascii_char[int(((count-1)*gray)/256)]
        txt += '\n'

    print(txt)
    f = open("output.txt", 'w')
    f.write(txt)
    f.close()
