from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '11312620'
API_KEY = 'DRnZxYs8pt07OSPUCxXpuiIS'
SECRET_KEY = 'UnGXXwkbPxVSAyooEd8WvDzL0VvajVVq'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
def asr(filename,lan=1536):
    return client.asr(filename, 'pcm', 16000, {'dev_pid': lan,})


def synthesis(text):
    result  = client.synthesis(text, 'zh', 1, {'vol': 5,'per':4})
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        return result
    else:
        return "NAN"