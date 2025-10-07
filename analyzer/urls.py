from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                # Homepage with form
    path('analyze/', views.analyze_resume, name='analyze_resume'),  # Action for resume analysis

    path('download_report/', views.download_report, name='download_report'),

]
