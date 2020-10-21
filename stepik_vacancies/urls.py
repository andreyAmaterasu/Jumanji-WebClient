"""stepik_vacancies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from app_vacancies.views import CompanyView, CompanyCreate, custom_handler404, custom_handler500, MainView, \
    MyCompanyView, SpecializationView, \
    user_login, user_signup, VacanciesView, \
    VacancyView, companies_view

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('companies/', companies_view, name='companies'),
    path('vacancies/cat/<str:specialization>/', SpecializationView.as_view(), name='specialization'),
    path('company/<int:id>/', CompanyView.as_view(), name='company'),
    path('vacancies/<int:id>/', VacancyView, name='vacancy'),
    path('admin/', admin.site.urls),
    path('mycompany/', MyCompanyView.as_view(), name='mycompany'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', user_signup, name='register'),
    path('company/add/<int:id>/', CompanyCreate.as_view(), name='company-add'),
    path('personal/', include('personal.urls')),
]

handler404 = custom_handler404
handler500 = custom_handler500

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
