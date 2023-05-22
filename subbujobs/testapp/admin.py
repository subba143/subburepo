from django.contrib import admin
from testapp.models import  HydJob, PuneJob, BngJob
# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']
admin.site.register(HydJob,HydJobsAdmin)

class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']
admin.site.register(PuneJob,PuneJobsAdmin)

class BngJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']
admin.site.register(BngJob,BngJobsAdmin)

