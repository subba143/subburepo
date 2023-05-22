from django.shortcuts import render
from testapp.models import  HydJob, PuneJob, BngJob
# Create your views here.
def homepage_view(request):
    return render(request, 'testapp/index.html')

def hydjobs_view(request):
    jobs_list = HydJob.objects.all()
    my_dict = {'jobs_list': jobs_list}
    return render(request, 'testapp/hydjobs.html', my_dict)
def bngjobs_view(request):
    jobs_list = BngJob.objects.all()
    my_dict = {'jobs_list': jobs_list}
    return render(request, 'testapp/bngjobs.html', my_dict)
def punejobs_view(request):
    jobs_list = PuneJob.objects.all()
    my_dict = {'jobs_list': jobs_list}
    return render(request, 'testapp/punejobs.html', my_dict)


