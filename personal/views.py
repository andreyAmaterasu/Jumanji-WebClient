from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from app_vacancies.models import Company
from .forms import CreateCompanyForm
from app_vacancies.models import Company, Vacancy, Specialty


def personal(request):
    user = request.user
    form = CreateCompanyForm(request.POST)
    context = {
        'username': user.get_full_name(),
    }

    try:
        company = Company.objects.get(owner=user.pk)
    except Company.DoesNotExist:
        return render(request, 'company-create.html', context=context)

    context.update({
        'form': form,
        'company': company
    })

    if request.method == 'POST':
        # form = CreateCompanyForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            cd = form.cleaned_data
            company = Company(id=company.pk, name=cd['name'], location=cd['location'],
                              employee_count=cd['employee_count'], description=cd['description'], logo=cd['logo'],
                              owner_id=request.user.pk)
            company.save()

            context.update({
                'name': company.name,
                'location': company.location,
                'employee_count': company.employee_count,
                'description': company.description,
                'view': True
            })
            return render(request, 'company-edit.html', context=context)
    else:
        return render(request, 'company-edit.html', context=context)


def create_company(request):
    form = CreateCompanyForm(request.POST)
    user = request.user
    context = {
        'username': user.get_full_name(),
        'form': form,
    }

    if request.method == 'POST':
        form = CreateCompanyForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data

            company = Company(name=cd['name'], location=cd['location'],
                              employee_count=cd['employee_count'], description=cd['description'], logo=cd['logo'],
                              owner_id=request.user.pk)
            company.save()

            context.update({
                'company': company
            })
            return HttpResponseRedirect("/personal/")
    else:
        return render(request, 'new-company.html', context=context)


def vacancy_list(request):
    user = request.user

    company = Company.objects.get(owner=user.pk)
    vacancies_of_company = Vacancy.objects.filter(company=company.pk)

    context = {
        'username': user.get_full_name(),
        'vacancies': vacancies_of_company
    }
    return render(request, 'vacancy-list.html', context=context)


def vacancy_edit(request, pk):
    user = request.user
    context = {
        'username': user.get_full_name(),
        'pk': pk
    }

    vacancy = Vacancy.objects.get(pk=pk)
    speciality = Specialty.objects.all()

    context.update({
        'vacancy': vacancy,
        'specialities': speciality
    })

    return render(request, 'vacancy-edit.html', context=context)
