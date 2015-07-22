from django.http import HttpResponse , Http404
from django.shortcuts import render

from .models import Engineer , Complaint


def index(request):
	output = '''<a href='/complaints/engineers/'>List of Engineers</a>
	 <br>
	 <a href='/complaints/complaints/'>List of complaints</a>'''
	return HttpResponse(output)

def engineers(request):
	latest_engineer_list = Engineer.objects.all()
	context = {'latest_engineer_list': latest_engineer_list}
	return render(request, 'complaints/engineers.html', context)

def engineer_details(request, engineer_id):
    try:
        engineer = Engineer.objects.get(pk=engineer_id)
    except Question.DoesNotExist:
        raise Http404("Engineer does not exist")
    return render(request, 'complaints/engineer_details.html', {'engineer': engineer})

def complaints(request):
    latest_complaint_list = Complaint.objects.all()
    context = {'latest_complaint_list': latest_complaint_list}
    return render(request, 'complaints/complaints.html', context)

def complaint_details(request, complaint_id):
    try:
        complaint = Complaint.objects.get(pk=complaint_id)
    except Question.DoesNotExist:
        raise Http404("Complaint does not exist")
    return render(request, 'complaints/complaint_details.html', {'complaint': complaint})

