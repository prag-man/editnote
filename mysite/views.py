# I have created this file (to make this code run, come to the parent mysite in cmd prompt and enter 'python manage.py runserver')
import time

from django.http import HttpResponse #if you want to return html code itself in the function
from django.shortcuts import render #if you want to attach a html file => takes 2 params : 1) requests, 2)file name which is in the templates dir
import random

def index(requests): #function which is being linked to urls.py and is acting as our home page
    return render(requests,'index.html')
    # return HttpResponse('''hello there we are <br>
    # <a href='http://127.0.0.1:8000/about'>about</a> <br>
    # <a href='http://127.0.0.1:8000/capitalize'>capitalize</a><br>
    # <a href='http://127.0.0.1:8000/capitalizefirst'>capitalize first</a><br>
    # <a href='http://127.0.0.1:8000/smallcase'>smallcase</a><br>
    # <a href='http://127.0.0.1:8000/removepunc'>remove punctuation</a><br>
    # <a href='http://127.0.0.1:8000/spaceremove'>remove space</a><br>
    # <a href='http://127.0.0.1:8000/charcount'>character counter</a><br>''')

# def hello(requests):
#     params = {'name': 'pragyam', 'kiski': 'duniya'}
#     return render(requests,'hello.html',params)
#
# def about(requests):
#     return HttpResponse('''about us <br>
#     <a href='http://127.0.0.1:8000'> back to home </a>''')
#
# def capitalize(requests):
#     djtext = requests.POST.get('text','default')
#     new_text= djtext.upper()
#     return HttpResponse(f'''capitalize all the letters : {new_text} <br>
#     <a href='http://127.0.0.1:8000'> back to home </a>''')
#
# def capitalizefirst(requests):
#     return HttpResponse('''capitalize the first letters <br>
#     <a href='http://127.0.0.1:8000'> back to home </a>''')
#
# def smallcase(requests):
#     return HttpResponse('''converts all into smallcase <br>
#     <a href='http://127.0.0.1:8000'> back to home </a>''')
#
# def removepunc(requests):
#     djtext = requests.POST.get('text','default')
#     return HttpResponse('''removes punctuation <br>
#     <a href='http://127.0.0.1:8000'> back to home </a>''')
#
# def spaceremove(requests):
#     return HttpResponse('''removes all the space in the line <br>
#     <a href='http://127.0.0.1:8000'> back to home </a>''')
#
# def charcount(requests):
#     return HttpResponse('''counts the character present <br>
#     <a href='http://127.0.0.1:8000'> back to home </a>''')

# def name(requests):
#     return render(requests,'name.html')
#
# def tell(requests):
#     djtext = requests.POST.get('naam','default') + ' is great'
#     eng = pyttsx3.init()
#     eng.save_to_file(djtext,'tell.mp3')
#     eng.runAndWait()
#     return HttpResponse('''<audio controls autoplay>
#     <source src="C:/Users/asus/PycharmProjects/trydjango/mysite/tell.mp3" type="audio/mpeg">
#     Your browser does not support the audio element.
#     </audio>''')

def analyzer(requests):

    text = requests.POST.get('text','default')#this is how we get input from user => text here is the element name while if there is no value found then default will be forwarded
    cap = requests.POST.get('capitalize','off')
    upper = requests.POST.get('uppercase','off')
    lower = requests.POST.get('lowercase','off')
    rempunc = requests.POST.get('removepunc','off')
    remspace = requests.POST.get('removespace','off')
    charcounter = requests.POST.get('charcount','off')
    linerem = requests.POST.get('linerem','off')

    empty_text = ''
    final_text = ''
    progress_text = ''
    analyzed_text = text

    if upper == 'on':
        analyzed_text = analyzed_text.upper()

    if lower == 'on':
        analyzed_text = analyzed_text.lower()

    if cap == 'on':
        analyzed_text = analyzed_text.title()

    punctuations = '''<>?:"{}|)(*&^%$#@!~`,./;'[]-'''

    if rempunc == 'on':
        for char in analyzed_text:
            if char not in punctuations:
                progress_text = progress_text + char
                analyzed_text = progress_text

    if remspace == 'on':
        for char in analyzed_text :
            if char != ' ':
                final_text = final_text + char
                analyzed_text = final_text



    if charcounter == 'on':
        length = len(analyzed_text)
        final_text = analyzed_text + f' : {length}'
        analyzed_text = final_text

    if linerem == 'on':
        final_text= analyzed_text.replace('\n',' ')
        analyzed_text = final_text

    if upper == 'on' and lower == 'on':
        analyzed_text = 'Error : Both uppercase and lowercase have been selected'
    elif text == '':
        analyzed_text = 'Error : please enter some text for the analyzer to work'

    return HttpResponse(f'<h1 id="hello">Analyzed text : 👇👇 </h1><br> <h3>{analyzed_text}</h3><br>'
                        f'<button onclick="getTextCopied()" id="buttontext">Copy</button> <br>'
                        f'<a href="http://127.0.0.1:8000"> Back to home </a> <br> <h5>Made with ❤️ by Pragyam Soni</h5> ')

def rando(requests):
    return HttpResponse('''<h1 align="centre">Welcome to Random.com</h1>
    <form align="centre" action="/rando/tasks" method="get">
    <button type='submit'>tasks to do</button></form>
    <form align="centre" action="/rando/sites" method="get">
    <button type='submit'>sites to watch out for</button></form>''')

def tasks(requests):
    num = random.randint(0,2)
    li = ['play','sleep','have food']
    return HttpResponse(f'<h1 align="centre">{li[num]}</h1><a href="">new one</a>')


def sites(requests):
    num = random.randint(0,2)
    li = ['youtube.com','dines.com','amazon.com']
    li2 = ['watch videos','does everything','buy goods']
    li3 = ['youtube','dines','amazon']
    return  HttpResponse(f'<h1 align="centre">{li3[num]} : {li2[num]}</h1>'
                         f'link : {li[num]} <br><a href="">new one</a> ')










