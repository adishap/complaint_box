from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Engineer , Complaint , Status , Amc_client


def index(request):
	return render(request, 'complaints/index.html')


def amc_clients(request):
    latest_amc_list = Amc_client.objects.all()
    context = {'latest_amc_list': latest_amc_list}
    return render(request, 'complaints/amc_clients.html', context)


def amc_details(request, amc_id):
    amc = get_object_or_404(Amc_client, pk=amc_id)
    return render(request, 'complaints/amc_details.html', {'amc': amc})

def engineers(request):
	latest_engineer_list = Engineer.objects.all()
	context = {'latest_engineer_list': latest_engineer_list}
	return render(request, 'complaints/engineers.html', context)

def engineer_details(request, engineer_id):
    engineer = get_object_or_404(Engineer, pk=engineer_id)
    return render(request, 'complaints/engineer_details.html', {'engineer': engineer})

def complaints(request):
    latest_complaint_list = Complaint.objects.all()
    context = {'latest_complaint_list': latest_complaint_list}
    return render(request, 'complaints/complaints.html', context)

def complaint_details(request, complaint_id):
    complaint = get_object_or_404(Complaint, pk=complaint_id)
    latest_status_list = Status.objects.all()
    #context = {'latest_status_list': latest_status_list}
    return render(request, 'complaints/complaint_details.html', {'complaint': complaint , 'latest_status_list': latest_status_list} )

def complaint_update(request , complaint_id):
    c = get_object_or_404(Complaint, pk=complaint_id)
    try:
        selected_status = Status.objects.get(pk = request.POST['status'])
    except (KeyError, Status.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'complaints/complaint_details.html', {
            'complaint':c,
            'error_message': "You didn't select a correct status.",
        })
    else:
        c.status = selected_status
        c.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'complaints/complaint_details.html', {
            'complaint':c,
            'error_message': "Status updated successfully.",
        })