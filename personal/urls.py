from django.urls import path

from personal.views import personal, create_company, vacancy_list, vacancy_edit, resume_edit, resume_create

urlpatterns = [
    path('', personal, name='personal'),
    path('createcompany/', create_company, name='createcompany'),
    path('vacancy-list/', vacancy_list, name='vacancy-list'),
    path('vacancy-edit/<int:pk>/', vacancy_edit, name='vacancy-edit'),
    path('company-edit/', personal, name='company-edit'),
    path('resume-edit/', resume_edit, name='resume-edit'),
    path('resume-edit/resume-create/', resume_create, name='resume-create'),
]
