# user made file
from django.http import HttpResponse
from django.shortcuts import render

# make sure to add "templates" in settings.py

def index(request):
    return render(request, 'index.html')

def process(request):
    text = request.POST.get('text', 'none')
    uppercase = request.POST.get('uppercase', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    removeextraemptylines = request.POST.get('removeextraemptylines', 'off')
    removeextraspaces = request.POST.get('removeextraspaces', 'off')
    if uppercase=="on" :
        text = text.upper()
    if lowercase=="on" :
        text = text.lower()
    if removeextraemptylines=="on":
        ans=""
        for ch in text:
            if ord(ch)!=10 and ord(ch)!=13:
                ans = ans+ch
        text = ans
    if removeextraspaces == "on":
        ans=""
        print("hello")
        for i in range(0, len(text)-1):
            print(text[i])
            if text[i]==" " and text[i+1]==" ":
                continue
            else:
                ans = ans + text[i]
        text = ans
    charcount = 0
    for char in text:
        if ord(char)>=26 and ord(char)<=126 and char!=" ":
            charcount = charcount + 1
    params = {'text': text, 'charcount': charcount}
    return render(request, 'process.html', params)