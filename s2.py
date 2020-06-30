from aip import AipFace,AipSpeech

"""你的APPID AK  SK"""

APP_ID = "17824156"
API_KEY = "dTTjbigDOpbAF2640GiMaysX"
SECRET_KEY = "q6u0BGUCj95SEWC94QcgeUped3HpAelh"
client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)
def get_file_content(filePath):
    with open(filePath,'rb')as fp:
        return fp.read()

res = client.asr(get_file_content('auido.pcm'),'pcm',16000,{
    'dev_pid':1536,
})

print(res.get('result')[0])
# print(res)