import  os
import cv2
import voicecontrol as voice
import base64
from matplotlib import pyplot as plt
from matplotlib import image as matimg


#用base64编码图片
def get_file_content(filePath):
    with open(filePath, mode='rb') as f:
        # print("ok,稍等")
        return base64.b64encode(f.read()).decode("utf-8")

#判断是否有同名图片
def imExist(s):
    for root, dirs, files in os.walk('./'):
        for name in files:
            if name.split(".")[0] == s:
                return  {"result":True,"path":os.path.join(root,name)}
    return {"result":False,"path":root}
#通过摄像头或者本地获取图片
def getimgFromCam():
    cap = cv2.VideoCapture(0)
    while (1):
        # 拍照
        ret, frame = cap.read()
        if ret == True:
            # 显示照片
            cv2.imshow("capture", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):

                # print("请给照片命名：")
                # voice.player("请给照片命名：")
                # s = input()
                # while imExist(s)["result"] == True:
                #     print("这个名字的文件已存在，请换个名字：")
                #     voice.player("这个名字的文件已存在，请换个名字：")
                #     s = input()
                # 非常棒的函数encode，不需要存本地，直接编码
                img_encode = cv2.imencode('.jpeg', frame)[1]
                # print(type(img_encode))
                str_encode = img_encode.tostring()
                break
                # cv2.imwrite(s+'.jpeg', frame)
    cap.release()
    cv2.destroyAllWindows()
    return base64.b64encode(str_encode).decode("utf-8")

def getIm():
    print("从摄像头取图？y/n")
    voice.player("是否从摄像头取图？")
    feedback = voice.my_record()
    while True:
        if feedback['err_msg'] == 'success.' and feedback['result'][0] == 'yes':
            voice.player("ok,稍等一下")
            # re = input()
            # if re.lower() == "y" or re.lower() == "yes" :
            return getimgFromCam()
        if feedback["err_msg"] == 'success.' and feedback["result"][0] == 'no':
        # if re.lower() == "n" or re.lower() == "no":
            #print("请将照片放在pic文件夹下：")
            #voicecontrol.player("请将照片放在pic文件夹下：")
            print("输入检测的照片名称：")
            voice.player("输入检测的照片名称：")
            imname = input()
            while imExist(imname)["result"] == False:
                print("图片不存在，请重新输入：")
                imname = input()
            path = imExist(imname)["path"]
            imshow = matimg.imread(path)
            plt.imshow(imshow)
            plt.show()

            return get_file_content(path)
        voice.player("没听明白.请回答yes或no.")
        voice.player("是否从摄像机取图？")
        feedback = voice.my_record()