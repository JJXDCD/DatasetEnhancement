import os
import pyautogui as pg
import time
import cv2
import numpy as np
import PIL
from PIL import Image


imageDirlist=[r"G:\DLDate\datas\train\0",r"G:\DLDate\datas\train\1",r"G:\DLDate\datas\train\2",
                  r"G:\DLDate\datas\train\3",r"G:\DLDate\datas\train\4",r"G:\DLDate\datas\train\5",
                  r'G:\DLDate\datas\test\0',r'G:\DLDate\datas\test\1',r'G:\DLDate\datas\test\2',
                  r'G:\DLDate\datas\test\3',r'G:\DLDate\datas\test\4',r'G:\DLDate\datas\test\5']
save=r'G:\DLDate\Enhancementdatas'

for imageDir in imageDirlist:
    path_list = imageDir.split("\\")
    save_path=os.path.join(save+'//4',path_list[3]+'//'+path_list[4]+'网吧')
    print(save_path)
    # print(imageDir)


background1 = pg.screenshot()
background1=cv2.cvtColor(np.array(background1),cv2.COLOR_RGB2BGR)
cv2.imwrite('background.jpg',background1)

with open("time.txt","w") as f:
    f.write('the total time is '+str(5)+'s'+'\n')
    f.write(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))



image = Image.open(os.path.join('./', 'colored072613183870-副本.jpg'))
image.save(os.path.join('./','5'+'colored072613183870-副本.jpg'))