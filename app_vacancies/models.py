from django.contrib.auth.models import User
from django.db import models

from stepik_vacancies.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR


class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR)
    description = models.TextField()
    employee_count = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Specialty(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=20)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR)


class Vacancy(models.Model):
    title = models.CharField(max_length=50)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=255)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateTimeField(auto_now=True)


class Resume(models.Model):
    QULIFICATION_CHOICES = (
        ("Средний (middle)", "Средний (middle)"),
        ("Младший (junior)", "Младший (junior)"),
        ("Старший (senior)", "Старший (senior)"),
    )

    JOB_STATUS_CHOICES = (
        ("Ищу работу", "Ищу работу"),
        ("Открыт к предложениям", "Открыт к предложениям"),
        ("Не ищу работу", "Не ищу работу"),
    )

    firstname = models.CharField(max_length=30)
    secondname = models.CharField(max_length=30)
    job_status = models.CharField(max_length=30, choices=JOB_STATUS_CHOICES, default='1')
    waiting_salary = models.IntegerField()
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=30, choices=QULIFICATION_CHOICES, default='1')
    education = models.CharField(max_length=150)
    work_experience = models.CharField(max_length=200)
    portfolio_link = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=0)


class Response(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    mail = models.CharField(max_length=500)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='responses')


class Application(models.Model):
    written_username = models.CharField(max_length=30)
    written_phone = models.CharField(max_length=20)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
