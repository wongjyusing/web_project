from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    context = 'hello world'
    #return HttpResponse(context)
    return render(request,'hello.html')
