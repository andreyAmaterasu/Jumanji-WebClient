from django.db.models import Count, F, Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from app_vacancies.models import Response, Resume
from .forms import CreateCompanyForm, EditVacancyForm, EditResumeForm
from app_vacancies.models import Company, Vacancy, Specialty


def personal(request):
    user = request.user
    context = {
        'username': user.get_full_name(),
    }

    try:
        company = Company.objects.get(owner=user.pk)
    except Company.DoesNotExist:
        return render(request, 'company-create.html', context=context)

    form = CreateCompanyForm(instance=company)
    context.update({
        'form': form,
        'company': company
    })
    request.session['user_company'] = company.pk

    if request.method == 'POST':
        form = CreateCompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()

            context.update({
                'view': True,
                'form': form
            })

    return render(request, 'company-edit.html', context=context)


def create_company(request):
    form = CreateCompanyForm()
    user = request.user
    context = {
        'username': user.get_full_name(),
        'form': form,
    }

    if request.method == 'POST':
        form = CreateCompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = user
            company.save()

            request.session['user_company'] = company.pk
            return HttpResponseRedirect("/personal/")
    return render(request, 'new-company.html', context=context)


def vacancy_list(request):
    user = request.user
    company = Company.objects.get(owner=user.pk)
    vacancies_of_company = Vacancy.objects.filter(company=company.pk).annotate(responses_count=Count('responses'))

    context = {
        'username': user.get_full_name(),
        'vacancies': vacancies_of_company,
    }

    return render(request, 'vacancy-list.html', context=context)


def vacancy_edit(request, pk):
    user = request.user
    vacancy = Vacancy.objects.get(pk=pk)
    form = EditVacancyForm(instance=vacancy)

    try:
        responses = Response.objects.filter(vacancy_id=vacancy.pk)
    except Response.DoesNotExist:
        responses = None

    context = {
        'username': user.get_full_name(),
        'form': form,
        'vacancy': vacancy,
        'responses': responses,
    }

    if request.method == 'POST':
        form = EditVacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()

            context.update({
                'view': True,
                'form': form
            })

    return render(request, 'vacancy-edit.html', context=context)


def resume_edit(request):
    user = request.user
    context = {
        'username': user.get_full_name(),
    }

    try:
        resume = Resume.objects.get(owner=user.pk)
    except Resume.DoesNotExist:
        return render(request, 'resume-create.html', context=context)

    form = EditResumeForm(instance=resume)

    context.update({
        'form': form
    })

    if request.method == 'POST':
        form = EditResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()

            context.update({
                'view': True,
                'form': form
            })

    return render(request, 'resume-edit.html', context=context)


def resume_create(request):
    user = request.user
    form = EditResumeForm()
    context = {
        'username': user.get_full_name(),
        'form': form
    }

    if request.method == 'POST':
        form = EditResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.owner = user
            resume.save()

            context.update({
                'form': form,
            })

    return render(request, 'resume-edit.html', context=context)
