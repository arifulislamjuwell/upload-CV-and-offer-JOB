from django.shortcuts import render,get_object_or_404
from .models import Sociallink
# Create your views here.
def home(request):
    batch_number=29
    templates= 'home.html'

    facebook= get_object_or_404(Sociallink, name='facebook')
    youtube= get_object_or_404(Sociallink, name='youtube')
    twitter=get_object_or_404(Sociallink, name='twitter')
    gmail=get_object_or_404(Sociallink, name='gmail')
    skype=get_object_or_404(Sociallink,name='skype')
    linkedin=get_object_or_404(Sociallink, name='linkedin')


    contex={'batch':batch_number,'fb':facebook,'yt':youtube,'t':twitter,'gm':gmail,'s':skype,'li':linkedin}
    return render(request,templates,contex)

def notice_list(request):
    templates= 'notice_list'
    return render(request)

def notice_details(request, slug):
    templates= 'notice_detaills'
    return render(request,templates)
