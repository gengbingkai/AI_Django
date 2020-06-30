import os

from aip import AipFace,AipSpeech,AipNlp
import time

from LookFace.settings import STATICFILES_DIRS
import requests
url ="https://api.ownthink.com/bot?appid=d6cd5b00dd7b43fb6f986e0f352dfd9f&userid=xioaai&spoken=%s"
""" 你的 APPID AK SK """
APP_ID = '17812949'
API_KEY = '04iTP8GoqqlmiEOg9nzlLXmK'
SECRET_KEY = 'ziSRKUIy7RaiiroXHuOs9CswjXP1F1X6'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)
speech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
nlp = AipNlp(APP_ID, API_KEY, SECRET_KEY)

def baidu_face(base_str):

    image = base_str # 难点

    imageType = "BASE64"

    """ 如果有可选参数 """
    options = {}
    options["face_field"] = "age,beauty,expression,gender,emotion,face_shape"
    options["max_face_num"] = 2
    options["face_type"] = "LIVE"
    options["liveness_control"] = "LOW"

    """ 带参数调用人脸检测 """
    res = client.detect(image, imageType,options)

    return res

def baidu_asr(audio_buff):
    res = speech.asr(audio_buff, options={
        'dev_pid': 1536,
    })
    print(res)

    return res.get("result")[0]


def baidu_tts(text):
    result = speech.synthesis(text, options={
        "per": 4,
        "spd": 4,
        "pit": 8,
        "vol": 5
    })
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    filename = f'{time.time()}.mp3'
    filepath = os.path.join(STATICFILES_DIRS[0],filename)
    if not isinstance(result, dict):
        with open(filepath, 'wb') as f:
            f.write(result)

    return filename


# print(res)

# print(res.get("result").get("face_list")[0].get("age"),
#       res.get("result").get("face_list")[0].get("beauty"),
#       res.get("result").get("face_list")[0].get("expression").get("type"),
#       res.get("result").get("face_list")[0].get("gender").get("type"),
#       res.get("result").get("face_list")[0].get("emotion").get("type"),
#       )


def  my_nlp_lowB_plus(text):
    if nlp.simnet(text,"你叫什么名字").get("score")>0.68:
        text = "我叫耿冰凯"
    elif nlp.simnet(text,"你几岁了").get("score")>0.68:
        text = "我今年10s岁了"
    else:
        res = requests.get(url%(text))
        text = res.json().get("data").get("info").get("text")
    return text