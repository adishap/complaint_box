from django.contrib import admin

# Register your models here.

from .models import Status ,Amc_type, Location , Engineer , Complaint , Device , Amc_client

class DeviceInline(admin.TabularInline):
	model = Device
	extra = 2

class AmcAdmin(admin.ModelAdmin):
	list_display = ('client_name','amc_type', 'renewal_date')
	list_filter = ['renewal_date']
	search_fields = ['client_name']

class ComplaintAdmin(admin.ModelAdmin):
	list_display = ('client_name','complaint_details', 'lock_date')
	list_filter = ['status']
	search_fields = ['client_name']
	fieldsets = [
        ('Complaint', {'fields': ['complaint_details']}),
        ('Complaint Details', {'fields': ['client_name','lock_date','assigned_to','location']}),
        ('Status', {'fields': ['status']}),
        ]
        inlines = [DeviceInline]

admin.site.register(Amc_client , AmcAdmin)

admin.site.register(Engineer)

admin.site.register(Complaint , ComplaintAdmin)
