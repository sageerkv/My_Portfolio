from django.contrib import admin
from . models import My_portfolio, Project, Service, Experience, Date, Skill


# Register your models here.

admin.site.register(My_portfolio)
admin.site.register(Project)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'service_description')

admin.site.register(Service, ServiceAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'get_date_range', 'description')

    def get_date_range(self, obj):
        return obj.date.date_range if obj.date else ""
    get_date_range.short_description = 'Date Range'

admin.site.register(Experience, ExperienceAdmin)

class DateAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'present_or_end_date', 'is_current', 'date_range')
    list_filter = ('is_current',)
    search_fields = ('start_date', 'present_or_end_date')

admin.site.register(Date, DateAdmin)

admin.site.register(Skill)