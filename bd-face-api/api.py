#coding=utf-8  
from aip import AipFace
import base64
import chardet

APP_ID = '11312620'
API_KEY = 'DRnZxYs8pt07OSPUCxXpuiIS'
SECRET_KEY = 'UnGXXwkbPxVSAyooEd8WvDzL0VvajVVq'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

#用base64编码图片
def get_file_content(filePath):
    with open(filePath, mode='rb') as f:
        # print("ok,稍等")
        return base64.b64encode(f.read()).decode("utf-8")





#-----------------人脸检测------

def detect(image,imageType):

    #如果有可选参数 """
    options = {}
    options["face_field"] = "age,beauty,gender"
    options["max_face_num"] = 2
    options["face_type"] = "LIVE"

    #带参数调用人脸检测
    return  client.detect(image, imageType, options)



#--------------人脸注册----------------------
# 如果有可选参数 """ 可以是face_token

def addUser(image , imageType , group_id , user_id ):
    options = {}
    options["user_info"] = "user's info"
    options["quality_control"] = "NORMAL"
    options["liveness_control"] = "NONE"

    # 带参数调用人脸注册 """
    return  client.addUser(image, imageType, group_id , user_id, options)




#--------------人脸搜索----------------------
# 如果有可选参数 """
def search(image , imageType):
    groupIdList = "test"

    """ 如果有可选参数 """
    options = {}
    options["quality_control"] = "NORMAL"
    options["liveness_control"] = "NONE"

    options["max_user_num"] = 2

    """ 带参数调用人脸搜索 """
    return client.search(image, imageType, groupIdList,options);


#--------------人脸更新---------------------
def updateUsers(image,imageType,groupId, userId):
    #  如果有可选参数 """
    options = {}
    options["user_info"] = "user's info"
    options["quality_control"] = "NORMAL"
    options["liveness_control"] = "LOW"

    # 带参数调用人脸更新 """
    return client.updateUser(image, imageType, groupId, userId, options)

#--------------人脸删除---------------------
def getUsers(userId, groupId, faceToken):
    # 调用人脸删除 """
    return  client.faceDelete(userId, groupId, faceToken)


#--------------信息查询---------------------
def getUsers(userId, groupId):
    # 调用用户信息查询 """
    return  client.getUser(userId, groupId)






