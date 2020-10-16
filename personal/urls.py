from django.urls import path
from . import views

from personal.views import personal, create_company, vacancy_list, vacancy_edit

urlpatterns = [
    path('', personal, name='personal'),
    path('createcompany/', create_company, name='createcompany'),
    path('vacancy-list/', vacancy_list, name='vacancy-list'),
    path('vacancy-edit/<int:pk>/', vacancy_edit, name='vacancy-edit'),
    path('company-edit/', personal, name='company-edit'),
]