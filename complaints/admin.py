from django.contrib import admin

# Register your models here.

from .models import Status , Location , Engineers , Complaint , Device


class DeviceInline(admin.TabularInline):
	model = Device
	extra = 2

class ComplaintAdmin(admin.ModelAdmin):
	list_display = ('client_name','complaint_details', 'lock_date')
	list_filter = ['status']
	search_fields = ['client_name']
	fieldsets = [
        ('Complaint', {'fields': ['complaint_details']}),
        ('Complaint Details', {'fields': ['client_name','lock_date','assigned_to']}),
        ('Status', {'fields': ['status']}),
        ]
        inlines = [DeviceInline]

admin.site.register(Engineers)
admin.site.register(Complaint , ComplaintAdmin)
