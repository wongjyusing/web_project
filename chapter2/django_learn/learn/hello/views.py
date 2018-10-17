from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    context = 'hello world'
    #return HttpResponse(context)
    return render(request,'hello.html')

def hello(request,name):
    context = f'你好，{ name }'

    return HttpResponse(context)

def hi(request,name):
    context = {}
    context['your_name'] = name
    return render(request,'test.html',context)
