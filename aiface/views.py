from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.core.files.uploadedfile import InMemoryUploadedFile
# from .utils import *
from aiface.utils import *

import base64
# Create your views here.
class AifaceView(View):
    def post(self,request):
        file_obj = request.FILES.get("img") #type:InMemoryUploadedFile
        file = file_obj.read()
        base_str = str(base64.b64encode(file),"utf8")
        res = baidu_face(base_str)
        print(res)
        ret_dict ={
            "age":res.get("result").get("face_list")[0].get("age"),
            "beauty":res.get("result").get("face_list")[0].get("beauty"),
            "expression":res.get("result").get("face_list")[0].get("expression").get("type"),
            "emotion":res.get("result").get("face_list")[0].get("emotion").get("type"),
            "gender":res.get("result").get("face_list")[0].get("gender").get("type"),
        }
        return JsonResponse(ret_dict)


class AiaudioView(View):
    def post(self,request):
        recofile = request.FILES.get("recofile")
        # print(recofile) # __str__
        file_content = recofile.read()
        text = baidu_asr(file_content)
        text = my_nlp_lowB_plus(text)
        filename = baidu_tts(text)
        print(filename)
        return JsonResponse({"msg":text,"filename":filename})


