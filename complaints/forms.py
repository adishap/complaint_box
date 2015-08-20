from django import forms

class ComplaintForm(forms.Form):
    client_name = forms.CharField(label='Client Name', max_length=200)
    complaint_details = forms.CharField(label='Complaint Details', max_length=1000)