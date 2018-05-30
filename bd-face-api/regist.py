##coding=utf-8  
import api
import GetReady
import voicecontrol as voice

group_id = "test"



if __name__ == '__main__':
    print("-----------------进入人脸识别系统-------------")
    voice.player("进入人脸识别系统")
    image = GetReady.getIm()
   # print(s)

   #  image = api.get_file_content(s)
    imageType = "BASE64"

    user = api.detect(image ,imageType)
    print(user)

    print("他的年龄：", user['result']['face_list'][0]["age"])
    if user['result']['face_list'][0]["gender"]['type'] == "male":
        voice.player("看上去是一位"+str(user['result']['face_list'][0]["age"])+"岁的男士")
    else:
        voice.player("看上去是一位" + str(user['result']['face_list'][0]["age"]) + "岁的女士")

    print("正在注册你的信息....")
    voice.player("正在注册你的信息....")
    print("你的名字：")
    voice.player("你的名字是：")
    feedback = voice.my_record(1737)
    while True:
        if feedback['err_msg'] == 'success.' :
            print(feedback['result'][0])
            voice.player("注册英文名为："+feedback['result'][0])
            break
        else:
            voice.player("没听清，你的名字是：")
            feedback = voice.my_record(1737)
    #stu_name =  input()
    stu_name = feedback['result'][0][:-1]
    signup = api.addUser(image,imageType,group_id ,stu_name)
    if signup["error_code"] == 0:
        print ("注册成功")
        voice.player("注册成功")
    else:
        print("注册失败，原因： ",signup["error_msg"])
        voice.player("注册失败，原因： "+signup["error_msg"])
       # exit(0)








    





