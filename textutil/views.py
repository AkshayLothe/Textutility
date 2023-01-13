#this is akshay's file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # return HttpResponse('''<H1>Home</H1> <button type="button"> <a href = "http://127.0.0.1:8000/removepunc"> Remove Punctuations </a> </button>
    # button type="button"> <a href = "http://127.0.0.1:8000/capfirst"> Capitalize First </a> </button>''')
    # dictionary={'name':'Akshay','place':'Pune'}
    return render(request, 'index.html')
    # f=open("1.txt","r")
    # x=f.readlines()
    # return HttpResponse(x)

def analyze(request):
    #get text
    djtext = request.POST.get('text', 'default')
    #checking check box value
    removepunc = request.POST.get('removepunc', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    cat = request.POST.get('cat', 'off')
    #if removepunc in on
    if (removepunc == "on"):
        # analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text
        # return HttpResponse("Remove Punctuations <a href='/'> Back!</a>"
        # return render(request, 'analyze.html', params)


    #if capfirst is on
    if (capfirst == "on"):
        x = djtext.upper()
        params = {'purpose': 'Capitalized All', 'analyzed_text': x}
        x = djtext
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (cat == 'on'):
        return HttpResponse('''<h1 style = "font-size:20em"> =✪ ᆺ ✪=</h1>''')
    if (charcounter == "on"):
        count = 0
        for i in range(len(djtext)):
            count = count+1
        return HttpResponse(count)

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover !="on" and capfirst !="on" and cat == "on"):
        return HttpResponse("Please select a valid option to proceed")
    return render(request, 'analyze.html', params)




# def removepunc(request):
#     #get text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     #analyze the text
#     return HttpResponse("Remove Punctuations <a href='/'> Back!</a>")

# def capfirst(request):
#     return HttpResponse("Capitalize first <a href='/'> Back!</a>")


def about(request):
    return HttpResponse("About our website <br><a href='/'> Back to Home </a>")
def contactus(request):
    return HttpResponse("Contact us on akshaylothe1@gmail.com <br> <a href='/'> Back to home</a>")

def references(request):
    return HttpResponse('''<H1>Facebook<H1> <a href= "https://www.facebook.com/"> Facebook Home</a>'''
                        '''<h1>Twitter<h1> <a href="https://twitter.com/home"> Twitter Home</a>'''
                        '''<h1>WhatsApp<h1> <a href="https://web.whatsapp.com/"> WhatsApp Home </a>'''
                        '''<h1>Twitter<h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7&ab_channel=CodeWithHarry"> Code with harry video</a>'''
                        '''<h1>Twitter<h1> <a href="http://127.0.0.1:8000/index"> Our Index Page</a>''')


