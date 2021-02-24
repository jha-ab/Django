from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.

def abhi(request):
	jobs = Job.objects
	return render(request, 'jobs/abhi.html', {'jobs':jobs})
	
def detail(request, job_id):
	job_detail = get_object_or_404(Job, pk=job_id) 
	return render(request, 'jobs/detail.html', {'job':job_detail})
