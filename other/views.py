from django.shortcuts import render

# Create your views here.
def home(request):
    batch_number=29
    templates= 'home.html'
    contex={'batch':batch_number}
    return render(request,templates,contex)

def notice_list(request):
    templates= 'notice_list'
    return render(request)

def notice_details(request, slug):
    templates= 'notice_detaills'
    return render(request,templates)
