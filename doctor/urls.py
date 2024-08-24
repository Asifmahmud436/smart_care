from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register('',views.DoctorViewSet)
router.register('specialization',views.SpecializationViewSet)
router.register('designation',views.DesignatinViewSet)
router.register('available',views.AvailableTimeViewSet)
router.register('review',views.ReviewViewSet)
urlpatterns = [
    path('',include(router.urls)),
]
