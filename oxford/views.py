from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from . form import Myform
from django.views import generic
import requests
import json
class get_word(View):

    def get(self,request):
               form = Myform()
               return  render(request,'oxford.html',{'form':form})
    def post(self,request):

           form=Myform(request.POST)
           if form.is_valid():
            word = form.cleaned_data['Word']
            compile_url ='https://api.hackerearth.com/v3/code/compile/'
            CLIENT_SECRET = '2b65fdbb92696e55630bab31c6df9fa6f1e568ed'

            source = word

            data = {
                'client_secret': CLIENT_SECRET,
                'async': 0,
                'source': source,
                'lang': "PYTHON",
                'time_limit': 5,
                'memory_limit': 262144,
            }

            r = requests.post(compile_url, data=data)
            return HttpResponse(r.text)
