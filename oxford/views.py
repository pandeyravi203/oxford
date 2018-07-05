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
            app_id = '4ec53208'
            app_key = '290c1054bfd9faf454d9b894623d68cb'
            result={}
            language = 'en'
            word_id = word

            url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

            r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
            result=r.json();
            return render(request,'display.html',{'result':result,'url':result['results'][0]['lexicalEntries'][0]['pronunciations'][0]['audioFile']})