from django.contrib import admin
from appointment.models import Appointment
from django.template.loader import render_to_string, get_template
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor_name','patient_name','appointment_types','appointment_status','symptom','time','cancel']

    def patient_name(self,obj):
        return obj.patient.user.first_name

    def doctor_name(self,obj):
        return obj.doctor.user.first_name
        
    def save_model(self,request ,obj ,form):
        obj.save()
        if obj.appointment_status == 'Running' and obj.appointment_types == "Online":
            email_subject = "Appointment is RUNNING"
            email_body = render_to_string('admin_email.html',{'user': obj.patient.user},{'doctor': obj.doctor})
            email = EmailMultiAlternatives(email_subject,'',to=[obj.patient.user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            return Response("Check your mail for confirmation")

admin.site.register(Appointment,AppointmentAdmin)