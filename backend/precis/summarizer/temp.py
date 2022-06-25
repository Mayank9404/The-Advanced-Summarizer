from django.shortcuts import render
from youtube_transcript_api import YouTubeTranscriptApi
from .summ import summarize
from django.http import JsonResponse
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
        youtube_url = request.GET.get('youtube-url')
        transcript = trans(youtube_url)
        summary = summarize(transcript,size)
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
    

    
    