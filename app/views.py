from django.http import HttpResponse
from django.shortcuts import render

import youtube_dl

def get_this_file_name(url):

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print(ydl)
    return 'url'

def app(request):
    context = {
        'result': ''
    }
    message = ''
    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            file_name = get_this_file_name(url)
            context['result'] = ''
            message = 'success'
        else:
            message = 'error, enter url'
    context['message'] = message
    return render(request, 'app.html', context)