from aip import AipFace,AipSpeech

"""你的APPID AK  SK"""

APP_ID = "17824156"
API_KEY = "dTTjbigDOpbAF2640GiMaysX"
SECRET_KEY = "q6u0BGUCj95SEWC94QcgeUped3HpAelh"
client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)

result  = client.synthesis('你好百度', 'zh', 1, {
    "per":4,
    "spd":4,
    "pit":8,
    "vol": 5
})
# result = client.synthesis("锄禾午",options={
#     "per":4,
#     "spd":4,
#     "pit":8,
#     "vol": 5
# })

print(result)
if not isinstance(result,dict):
    with open('auido.mp3','wb')as f:
        f.write(result)


# res = client.asr(get_file_content('auido.mp3'))