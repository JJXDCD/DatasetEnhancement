from PIL import Image
from PIL import ImageEnhance
import os
import cv2
import pyautogui as pg
import numpy as np
import time

def Autoclose():
    pg.moveTo(1674, 1063, 0.5)
    pg.click(button='right')
    pg.moveTo(1599, 1008, 0.5)
    pg.click()
    time.sleep(2)
    pg.moveTo(24, 1060, 0.5)
    pg.click()
    pg.moveTo(21, 1020, 0.5)
    pg.click()
    pg.moveTo(37, 933, 0.5)
    time.sleep(10)
    pg.click()




def flip(root_path,img_name):   #翻转图像
    img = Image.open(os.path.join(root_path, img_name))
    filp_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    # filp_img.save(os.path.join(root_path,img_name.split('.')[0] + '_flip.jpg'))
    return filp_img

def rotation(root_path, img_name):
    img = Image.open(os.path.join(root_path, img_name))
    rotation_img = img.rotate(20) #旋转角度
    # rotation_img.save(os.path.join(root_path,img_name.split('.')[0] + '_rotation.jpg'))
    return rotation_img

def randomColor(root_path, img_name): #随机颜色
    """
    对图像进行颜色抖动
    :param image: PIL的图像image
    :return: 有颜色色差的图像image
    """
    image = Image.open(os.path.join(root_path, img_name))
    random_factor = np.random.randint(0, 31) / 10.  # 随机因子
    color_image = ImageEnhance.Color(image).enhance(random_factor)  # 调整图像的饱和度
    random_factor = np.random.randint(10, 21) / 10.  # 随机因子
    brightness_image = ImageEnhance.Brightness(color_image).enhance(random_factor)  # 调整图像的亮度
    random_factor = np.random.randint(10, 21) / 10.  # 随机因子
    contrast_image = ImageEnhance.Contrast(brightness_image).enhance(random_factor)  # 调整图像对比度
    random_factor = np.random.randint(0, 31) / 10.  # 随机因子
    return ImageEnhance.Sharpness(contrast_image).enhance(random_factor)  # 调整图像锐度

def contrastEnhancement(root_path, img_name):  # 对比度增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_con = ImageEnhance.Contrast(image)
    contrast = 1.5
    image_contrasted = enh_con.enhance(contrast)
    return image_contrasted

def brightnessEnhancement(root_path,img_name):#亮度增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_bri = ImageEnhance.Brightness(image)
    brightness = 1.5
    image_brightened = enh_bri.enhance(brightness)
    return image_brightened


def colorEnhancement(root_path,img_name):#颜色增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_col = ImageEnhance.Color(image)
    color = 1.5
    image_colored = enh_col.enhance(color)
    return image_colored


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
        print("文件夹已创建成功")
    else:
        print("文件夹已存在")


if __name__ == '__main__':


    start = time.time()#r"G:\DLDate\datas\train\0",已经处理完成
    imageDirlist=[r"G:\DLDate\datas\train\1",r"G:\DLDate\datas\train\2",
                  r"G:\DLDate\datas\train\3",r"G:\DLDate\datas\train\4",r"G:\DLDate\datas\train\5",
                  r'G:\DLDate\datas\test\0',r'G:\DLDate\datas\test\1',r'G:\DLDate\datas\test\2',
                  r'G:\DLDate\datas\test\3',r'G:\DLDate\datas\test\4',r'G:\DLDate\datas\test\5']     #要改变的图片的路径文件夹
    save=r'G:\DLDate\Enhancementdatas'
    for imageDir in imageDirlist:
        path_list = imageDir.split("\\")
        save_path = os.path.join(save, path_list[3] + '//' + path_list[4])
        mkdir(save_path)
        print('正在处理的文件夹是：',imageDir,'...........')
        print('保存的路径是： ',save_path)
        for name in os.listdir(imageDir):
            try:

                # print(imageDir+'/flip')
                print('正在处理的图片是：',name,'\n')
                flip_img=flip(imageDir,name)    #翻转图像
                flip_img.save(os.path.join(save_path,'flip'+name))

                rotation_img=rotation(imageDir,name)    #旋转角度20
                rotation_img.save(os.path.join(save_path,'rotation'+name))

                contrasted_image=contrastEnhancement(imageDir,name)     #对比度增强
                contrasted_image.save(os.path.join(save_path,'contrasted'+name))

                brightened_image=brightnessEnhancement(imageDir,name)   #亮度增强
                brightened_image.save(os.path.join(save_path,'brightened'+name))

                colored_image=colorEnhancement(imageDir,name)           #颜色增强
                colored_image.save(os.path.join(save_path,'colored'+name))
            except:

                with open("error.txt", "w") as f:

                    f.write(str(imageDir)+'/'+str(name)+ '\n')




    end=time.time()

    time1=round(end-start)

    with open("time.txt", "w") as f:

        f.write('the total time is '+str(time1)+'s'+'\n')
        f.write(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))

    background1 = pg.screenshot()
    background1 = cv2.cvtColor(np.array(background1), cv2.COLOR_RGB2BGR)
    cv2.imwrite('background.jpg', background1)


    Autoclose()













