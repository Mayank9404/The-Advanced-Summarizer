from django.shortcuts import render
from youtube_transcript_api import YouTubeTranscriptApi
from .summ import summarize
from django.http import JsonResponse
import urllib.request
from bs4 import BeautifulSoup
# Create your views here.
def home(request):
    data = {}
    return JsonResponse(data)

def result(request):
    #print(dict(request.GET))
    size = request.GET.get('size')
    if ((len(request.GET.get('text-ip')) == 0) and (len(request.GET.get('youtube-url')) == 0)):
        return render(request, 'index.html')
    if len(request.GET.get('text-ip')) != 0:
        text = request.GET.get('text-ip')
        summary = summarize(text,size)
    else:
        url = request.GET.get('youtube-url')
        if ('youtube' in url) or ('youtu' in url):
            youtube_url = url
            text_data = trans(youtube_url)
        else:
            text_data = scrap(url)
        summary = summarize(text_data,size)
    data = {'summary':summary}
    return JsonResponse(data)
    #return render(request, 'result.html', data)


def trans(url):
    lst = url.split('?')
    vid_id = lst[-1][2:]
    ls =YouTubeTranscriptApi.get_transcript(vid_id)
    transcript = ''
    rmv = ['(ambient music)','(splashing)','(waves lapping)','(intense ambient music)']
    for i in ls:
        for j in rmv:
            if j in i['text']:
                i['text'] = i['text'].replace(j,' ')
        for x in i['text']:
          if x == '.':
            i['text'] = i['text'].replace(x,x+' ')
        transcript += (' ' + i['text'])
    return transcript
    
def scrap(urls):
    header= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
      'AppleWebKit/537.11 (KHTML, like Gecko) '
      'Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}

    urls = "https://realpython.com/beautiful-soup-web-scraper-python/"

    req = urllib.request.Request(url=urls, headers=header) 
    html = urllib.request.urlopen(req)

    htmlParse = BeautifulSoup(html, 'html.parser')
    article =''
    for para in htmlParse.find_all("p"):
        article+=para.get_text()
    start1 =0
    end1=0
    flag1=0
    start2 =0
    end2=0
    flag2=0
    x = len(article)
    i=0
    while i<x:
        if article[i] == '<':
            start1=i
            for j in range(i,len(article)):
                if article[j] =='>':
                    end1=j
                    flag1 = 1
                    break
        elif article[i] == '{':
            start2=i
            for j in range(i,len(article)):
                if article[j] =='}':
                    end2=j
                    flag2 = 1
                    break
        if flag1:
            article = article[:start1]+article[end1+1:]
            flag1 =0
            x=len(article)
        elif flag2:
            article = article[:start2]+article[end2+1:]
            flag2 =0
            x=len(article)
        i+=1
    return article