from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from authenticate.models import Profile
from django.db.models import Q
# Create your views here.

@login_required
def add_job(request):
    templates ='job/add_job.html'
    contex={'error_input':'You have to input all field with data'}
    print(request.user)

    check_create_user_profile= get_object_or_404(Profile,user= request.user )

    ccup=check_create_user_profile.page_permission
    print (ccup)
    if ccup ==str(1):

        if request.method == 'POST':
            post=JobCircular()
            post.user=request.user
            post.company= request.POST.get('company_name')
            post.post_name= request.POST.get('post_name')
            post.job_type=request.POST.get('job_type')
            post.qualification=request.POST.get('qualifications')
            post.skill=request.POST.get('skill_needed')
            post.website=request.POST.get('website')
            post.age_limit=request.POST.get('age_limit')
            post.job_nature=request.POST.get('job_nature')
            post.salary_range=request.POST.get('salary_range')
            post.save()

            return redirect('home')

        else:
            return render(request,templates,contex)

    else:
        return redirect('profile')


def job_circular_list(request):
    templates= 'job/job_circular_list.html'
    job_circular= JobCircular.objects.all()
    job=job_circular.filter(approve='a')
    query=request.GET.get('q')
    if query:
        job= job.filter(
            Q(skill__icontains=query)|
            Q(job_type__icontains=query)|
            Q(company__icontains=query)
        ).distinct()
    contex= {'job':job}
    return render(request,templates,contex)

def job_circular_details(request, slug):
    templates= 'job/job_details.html'
    job= get_object_or_404(JobCircular, slug=slug)
    contex= {'job':job}
    return render(request,templates,contex)

@login_required
def upload_cv(request):
    templates= 'cv/add_cv.html'
    catagories= CvCatagory.objects.all()
    contex ={'catagory':catagories}

    check_create_user_profile= get_object_or_404(Profile,user= request.user )
    ccup=check_create_user_profile.page_permission
    if ccup ==str(1):

        if request.method == 'POST':
            post=Cv()
            print('hi')
            position=request.POST['position']
            print(position)
            catagory= get_object_or_404(CvCatagory, name=request.POST['position'])
            post.catagory= catagory
            post.user= request.user
            post.skill= request.POST.get('skill')
            post.email= request.POST.get('email')
            post.file= request.POST.get('upload_file')
            post.save()

            return redirect('home')
        else:
            return render(request,templates,contex)
    else:

        return redirect('profile')





def cv_catagory_list(request):
    templates= 'cv/cv_catagory_list.html'
    catagory= CvCatagory.objects.all()
    contex = {'cvcatagory':catagory}
    return render(request,templates,contex)

def cv_catagory_post_list(request,slug):
    templates= 'cv/catagory_post_list.html'
    catagories = CvCatagory.objects.all()
    cv = Cv.objects.all()
    if slug:
        catagory= get_object_or_404(CvCatagory, slug=slug)
        cv= cv.filter(catagory = catagory, approve ='a')
    query=request.GET.get('q')
    if query:
        cv= cv.filter(
            Q(skill__icontains=query)
        ).distinct()
    contex ={'catagories':catagories, 'cv':cv, 'catagory':catagory}
    return render(request,templates,contex)

def cv_details(request,pk):
    templates= 'cv/cv_details.html'
    post= get_object_or_404(Cv, pk=pk)
    return render(request, templates,{'post':post})
