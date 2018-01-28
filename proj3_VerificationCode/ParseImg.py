#！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2018/1/28 14:58

@desc:

'''

from PIL import Image
import hashlib
import time
im = Image.open("captcha.gif")
#(将图片转换为8位像素模式)
im.convert("P")
#打印颜色直方图
# print(im.histogram())

#对直方图排序，得到有用的颜色
# his = im.histogram()
# values = {}
#
# for i in range(256):
#     values[i] = his[i]
#
# for j,k in sorted(values.items(),key=lambda x:x[1],reverse = True)[:10]:
#     print(j,k)

#生成黑白二值图片
im = Image.open("captcha.gif")
im.convert("P")
im2 = Image.new("P",im.size,255)


for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        if pix == 220 or pix == 227: # these are the numbers to get
            im2.putpixel((y,x),0)

# im2.show()

#提取单个字符图片
inletter = False
foundletter=False
start = 0
end = 0

letters = []

for y in range(im2.size[0]):
    for x in range(im2.size[1]):
        pix = im2.getpixel((y,x))
        if pix != 255:
            inletter = True
    if foundletter == False and inletter == True:
        foundletter = True
        start = y

    if foundletter == True and inletter == False:
        foundletter = False
        end = y
        letters.append((start,end))

    inletter=False
#输出每个字符的开始和结束的序列号
print(letters)

#切割并保存
count = 0
for letter in letters:
    m = hashlib.md5()
    im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
    s = str("%s%s"%(time.time(),count))
    m.update(s.encode("utf8"))
    im3.save("./%s.gif"%(m.hexdigest()))
    count += 1
