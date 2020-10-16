from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from app_vacancies.forms import CompanyForm, LoginForm, SignupForm
from app_vacancies.models import Company, Specialty, Vacancy
from stepik_vacancies import settings


class MainView(View):
    def get(self, request):
        specialties = Specialty.objects.all()
        companies = Company.objects.all()

        context = {
            'specialties': specialties,
            'companies': companies,
        }
        return render(request, 'index.html', context=context)


class VacanciesView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        context = {
            'vacancies': vacancies,
            'title': settings.ALL_VACANCIES_TITLE,
        }

        return render(request, 'vacancies.html', context=context)


class SpecializationView(View):
    def get(self, request, specialization):
        try:
            category = Specialty.objects.get(code=specialization)
        except Specialty.DoesNotExist:
            raise Http404
        vacancies = Vacancy.objects.filter(specialty=category)
        context = {
            'vacancies': vacancies,
            'title': category.title,
        }
        return render(request, 'vacancies.html', context=context)


class CompaniesView(View):
    def get(self, request, id):
        try:
            company = Company.objects.get(pk=id)
        except Company.DoesNotExist:
            raise Http404
        vacancies = Vacancy.objects.filter(company=company)
        context = {
            'vacancies': vacancies,
            'title': company.name,
            'logo': company.logo,
            'count': company.vacancies.count,
        }
        return render(request, 'company.html', context=context)


class VacancyView(View):
    def get(self, request, id):
        try:
            vacancy = Vacancy.objects.get(pk=id)
        except Vacancy.DoesNotExist:
            raise Http404

        return render(request, 'vacancy.html', {'vacancy': vacancy})


class CompanyCreate(CreateView):
    model = Company
    fields = ['name', 'location', 'description', 'employee_count']

class CompanyUpdate(UpdateView):
    model = Company
    fields = ['name', 'location', 'description', 'employee_count']


class MyCompanyView(View):
    def get(self, request):
        form = CompanyForm()
        try:
            company = Company.objects.get(owner=request.user.pk)
        except Company.DoesNotExist:
            # return render(request, 'new_company.html', {})
            # form = CompanyForm()
            return render(request, 'login.html', {'form': form})
        context = {
            'company': company,
        }
        return render(request, 'vacancies.html', context=context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # context = {
                    #     'username': user.get_full_name(),
                    # }
                    # try:
                    #     company = Company.objects.get(owner=user.pk)
                    # except Company.DoesNotExist:
                    #     return render(request, 'company-create.html', context=context)
                    # return render(request, 'company-edit.html', context=context)
                    return HttpResponseRedirect("/personal/")
                else:
                    return HttpResponse('Disabled account')
            else:
                return render(request, 'login.html', {'form': form, 'error': True})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('main')
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')


def custom_handler500(request):
    return HttpResponseServerError('Ой, что то пошло не так... Простите извините!')
