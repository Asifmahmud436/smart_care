from django.contrib import admin
from doctor.models import Doctor,AvailableTime,Specialization,Designation,Review
# Register your models here.

class SpecializationModel(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

class DesignationModel(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}


admin.site.register(Doctor)
admin.site.register(Specialization,SpecializationModel)
admin.site.register(Designation,DesignationModel)
admin.site.register(AvailableTime)
admin.site.register(Review)
