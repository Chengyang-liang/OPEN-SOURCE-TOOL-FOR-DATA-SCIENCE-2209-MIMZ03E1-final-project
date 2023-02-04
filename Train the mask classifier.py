#图片格式转换成jpg
import os
import string
#dirName = "C:\\Users\\Lenovo\\Desktop\\P_N_samples\\mask\\have_mask\\"
dirName = "C:\\Users\\Lenovo\\Desktop\\P_N_samples\\mask\\no_mask\\"
#dirName = "jpeg\\"      #最后要加双斜杠，不然会报错
#dirName = "png\\"      #最后要加双斜杠，不然会报错
li=os.listdir(dirName)
for filename in li:
    newname = filename
    newname = newname.split(".")
    if newname[-1]=="jpeg":
        newname[-1]="jpg"
        newname = str.join(".",newname)  #这里要用str.join
        filename = dirName+filename
        newname = dirName+newname
        os.rename(filename,newname)
        print(newname,"updated successfully")
    if newname[-1]=="JPEG":
        newname[-1]="jpg"
        newname = str.join(".",newname)  #这里要用str.join
        filename = dirName+filename
        newname = dirName+newname
        os.rename(filename,newname)
        print(newname,"updated successfully")
    if newname[-1]=="png":
        newname[-1]="jpg"
        newname = str.join(".",newname)  #这里要用str.join
        filename = dirName+filename
        newname = dirName+newname
        os.rename(filename,newname)
        print(newname,"updated successfully")

# 对正样本数据集重命名
# coding:utf-8
import os

path = "C:\\Users\\Lenovo\\Desktop\\P_N_samples\\mask\\have_mask"  # 你的路径
filelist = os.listdir(path)
count = 1000  # 开始文件名1000.jpg
for file in filelist:
    Olddir = os.path.join(path, file)
    if os.path.isdir(Olddir):
        continue
    filename = os.path.splitext(file)[0]
    filetype = os.path.splitext(file)[1]

    Newdir = os.path.join(path, str(count) + filetype)
    os.rename(Olddir, Newdir)
    count += 1

# 对负样本数据集重命名
# coding:utf-8
import os

path = "C:\\Users\\Lenovo\\Desktop\\P_N_samples\\mask\\no_mask"  # 你的路径
filelist = os.listdir(path)
count = 100000  # 开始文件名100000.jpg
for file in filelist:
    Olddir = os.path.join(path, file)
    if os.path.isdir(Olddir):
        continue
    filename = os.path.splitext(file)[0]
    filetype = os.path.splitext(file)[1]

    Newdir = os.path.join(path, str(count) + filetype)
    os.rename(Olddir, Newdir)
    count += 1

#修改正样本像素
import pandas as pd
import cv2
for n in range(10000,10866):#代表正数据集中开始和结束照片的数字
    path='C:\\Users\\Lenovo\\Desktop\\P_N_samples\\mask\\have_mask\\'+str(n)+'.jpg'
    # 读取图片
    img = cv2.imread(path)
    img=cv2.resize(img,(20,20)) #修改样本像素为20x20
    cv2.imwrite('C:\\Users\\Lenovo\\Desktop\\P_N_samples\\mask\\have_mask\\' + str(n) + '.jpg', img)
    n += 1

#修改负样本像素
import pandas as pd
import cv2
for n in range(100000,104017):#代表负样本数据集中开始和结束照片的数字
    path='C:\\Users\\Lenovo\\Desktop\\P_N_samples\\mask\\no_mask\\'+str(n)+'.jpg'
    # 读取图片
    img = cv2.imread(path)
    img=cv2.resize(img,(60,60)) #修改样本像素为60x60
    cv2.imwrite('C:\\Users\\Lenovo\\Desktop\\P_N_samples\\mask\\no_mask\\' + str(n) + '.jpg', img)
    n += 1

#正样本文件预处理 每行目录结尾加入 1 0 0 20 20
#coding:utf-8
import os
#suffix="_Apple"
suffix=r" 1 0 0 20 20" #后缀
filelist = open('C:\\Users\\Lenovo\\Desktop\\P_N_samples\\mask\\have_mask.txt','r+',encoding = 'utf-8')
line = filelist.readlines()
for file in line:
    file=file.strip('\n')+suffix+'\n'
    print(file)
    filelist.write(file)

#负样本文件预处理 每行目录结尾加入 1 0 0 60 60
#coding:utf-8
import os
#suffix="_Apple"
suffix=r" 1 0 0 60 60" #后缀
filelist = open('C:\\Users\\Lenovo\\Desktop\\P_N_samples\\mask\\no_mask.txt','r+',encoding = 'utf-8')
line = filelist.readlines()
for file in line:
    file=file.strip('\n')+suffix+'\n'
    print(file)
    filelist.write(file)


