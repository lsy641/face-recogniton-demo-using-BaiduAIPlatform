import api
import GetReady
import voicecontrol as voice
def checkstart():
    voice.player("现在需要认证你的身份，请看摄像头")
    image = GetReady.getimgFromCam()
    imageType = "BASE64"
    sear_result = api.search(image, imageType)
    print(sear_result)
    if sear_result['error_code']!=0:
        voice.player("认证失败，原因")
        voice.player(sear_result['error_msg'])
        checkstart()
        return
    if sear_result["result"]["user_list"][0]["score"]>70:
        print("匹配到用户", sear_result["result"]["user_list"][0]["user_id"])
        voice.player("匹配到用户")
        voice.player(sear_result["result"]["user_list"][0]["user_id"])
        voice.player("认证成功。")
    else:
        print("没有匹配到用户，请重新尝试")
        voice.player("没有匹配到用户，请重新尝试")
        checkstart()


checkstart()
