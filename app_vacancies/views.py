from django.contrib.auth import authenticate, login
from django.db.models import Count
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, UpdateView

from app_vacancies.forms import CompanyForm, LoginForm, SignupForm, ResponseForm
from app_vacancies.models import Company, Specialty, Vacancy
from stepik_vacancies import settings


class MainView(View):
    def get(self, request):
        user = request.user
        specialties = Specialty.objects.all().annotate(vacancies_count=Count('vacancies'))
        companies = Company.objects.all().annotate(vacancies_count=Count('vacancies'))
        request.session['user_company'] = 1

        context = {
            'user': user,
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


class CompanyView(View):
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


def VacancyView(request, id):
    try:
        vacancy = Vacancy.objects.get(pk=id)
    except Vacancy.DoesNotExist:
        raise Http404

    form = ResponseForm()

    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.vacancy = vacancy
            response.save()

    data_context = {
        'vacancy': vacancy,
        'form': form
    }
    return render(request, 'vacancy.html', context=data_context)


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


def companies_view(request):
    companies = Company.objects.all()
    context = {
        'companies': companies,
        'title': settings.ALL_COMPANIES_TITLE,
    }

    return render(request, 'companies.html', context=context)


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
