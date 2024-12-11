from django.http import HttpResponse
from django.shortcuts import render

def analyze(request):
    djtext = request.POST.get('text','default value')
    puncstatus = request.POST.get('removepunc','off')
    capsstatus = request.POST.get('capitalize','off')
    linestatus=request.POST.get('newlineremove','off')
    spacestatus=request.POST.get('spaceremover','off')
   
    if puncstatus == 'on':
        punctuation = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        newtext = ""
        
        for i in djtext:
            if i not in punctuation:
                newtext = newtext + i
        params ={'purpose':'Removed Punctuation','analyze_text':newtext}
        djtext=newtext

    if  capsstatus=='on':
        newtext = ""
        for i in djtext:
             newtext = newtext + i.upper()
        params ={'purpose':'Upper case','analyze_text':newtext}
        djtext=newtext

    if linestatus=='on':
        newtext = ""
        for i in djtext:
            if i!='\n' and i!='\r':
             newtext = newtext + i
        params ={'purpose':'Line Remover','analyze_text':newtext}
        djtext=newtext

    if spacestatus=='on':
        newtext = ""
        for index,item in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                newtext = newtext + item
        params ={'purpose':'Space Remover','analyze_text':newtext}
        djtext=newtext
    

    if puncstatus != 'on' and capsstatus!='on' and linestatus!='on' and spacestatus!='on':
        return HttpResponse ("Please select the anyone option")

    return render(request,"analyze.html",params)
    
    
def index(request):
    return render(request,"index.html")








