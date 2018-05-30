import PIL.Image
#import dlib
import numpy as np

def face_landmarks(result, face_locations=None, model="large"):
    """
    给一个百度人脸识别成功后的结果, 返回有关面部定位特征的字典 (眼睛, 鼻子, 等等)
    :参数 result: 百度人脸检测的结果，是一个字典
    :参数 face_locations: Optionally provide a list of face locations to check.
    :返回: 有关面部定位特征的字典 (眼睛, 鼻子, 等等)
    """
    points = result['face_list']['landmark72']


    # 百度人脸检测72个关键点分布图（对应landmark72个点的顺序，序号从0-71）, 详细见https://ai.bdstatic.com/file/52BC00FFD4754A6298D977EDAD033DA0
    return [{
        "chin":    [tuple(row.values()) for row in points[4:8]],
        "left_eyebrow": [tuple(row.values()) for row in points[22:29]],
        "right_eyebrow": [tuple(row.values()) for row in points[39:46]],
        "nose": [tuple(row.values()) for row in points[47:56]],
        "nose_tip": [tuple(row.values()) for row in points[51:52]+[points[57]]],
        "left_eye": [tuple(row.values()) for row in points[13:20]],
        "right_eye": [tuple(row.values()) for row in points[30:37]],
        #这里可以让学生填
        "top_lip": [tuple(row.values()) for row in points[58:62]+points[66:68]],
        "bottom_lip":[tuple(row.values()) for row in points[62:65]+points[69:71]+points[58]]
    }]