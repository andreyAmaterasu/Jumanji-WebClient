import os
import django

from app_vacancies.models import Company, Specialty, Vacancy

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stepik_vacancies.settings')
django.setup()

""" Компании """

companies_data = [
    {"name": "workiro", "location": "", "logo": "https://place-hold.it/100x60", "description": "",
     "employee_count": 0},
    {"name": "rebelrage", "location": "", "logo": "https://place-hold.it/100x60", "description": "",
     "employee_count": 0},
    {"name": "staffingsmarter", "location": "", "logo": "https://place-hold.it/100x60", "description": "",
     "employee_count": 0},
    {"name": "evilthreat h", "location": "", "logo": "https://place-hold.it/100x60", "description": "",
     "employee_count": 0},
    {"name": "hirey ", "location": "", "logo": "https://place-hold.it/100x60", "description": "",
     "employee_count": 0},
    {"name": "swiftattack", "location": "", "logo": "https://place-hold.it/100x60", "description": "",
     "employee_count": 0},
    {"name": "troller", "location": "", "logo": "https://place-hold.it/100x60", "description": "",
     "employee_count": 0},
    {"name": "primalassault", "location": "", "logo": "https://place-hold.it/100x60", "description": "",
     "employee_count": 0}
]

""" Категории """

specialties_data = [
    {"code": "frontend", "title": "Фронтенд", "picture": "https://place-hold.it/100x60"},
    {"code": "backend", "title": "Бэкенд", "picture": "https://place-hold.it/100x60"},
    {"code": "gamedev", "title": "Геймдев", "picture": "https://place-hold.it/100x60"},
    {"code": "devops", "title": "Девопс", "picture": "https://place-hold.it/100x60"},
    {"code": "design", "title": "Дизайн", "picture": "https://place-hold.it/100x60"},
    {"code": "products", "title": "Продукты", "picture": "https://place-hold.it/100x60"},
    {"code": "management", "title": "Менеджмент", "picture": "https://place-hold.it/100x60"},
    {"code": "testing", "title": "Тестирование", "picture": "https://place-hold.it/100x60"}
]

""" Вакансии """

vacancies_data = [
    {"title": "Разработчик на Python", "specialty": Specialty.objects.get(code="backend"),
     "company": Company.objects.get(name="staffingsmarter"), "skills": "", "description": "Потом добавим",
     "salary_min": 100000, "salary_max": 150000, "published_at": "2020-03-11"},
    {"title": "Разработчик в проект на Django", "specialty": Specialty.objects.get(code="backend"),
     "company": Company.objects.get(name="swiftattack"), "skills": "", "description": "Потом добавим",
     "salary_min": "80000", "salary_max": "90000", "published_at": "2020-03-11"},
    {"title": "Разработчик на Swift в аутсорс компанию", "specialty": Specialty.objects.get(code="backend"),
     "company": Company.objects.get(name="swiftattack"), "skills": "", "description": "Потом добавим",
     "salary_min": "120000", "salary_max": "150000", "published_at": "2020-03-11"},
    {"title": "Мидл программист на Python", "specialty": Specialty.objects.get(code="backend"),
     "company": Company.objects.get(name="workiro"), "skills": "", "description": "Потом добавим",
     "salary_min": "80000", "salary_max": "90000", "published_at": "2020-03-11"},
    {"title": "Питонист в стартап", "specialty": Specialty.objects.get(code="backend"),
     "company": Company.objects.get(name="primalassault"), "skills": "", "description": "Потом добавим",
     "salary_min": "120000", "salary_max": "150000", "published_at": "2020-03-11"}
]

if __name__ == '__main__':
    companies = Company.objects.bulk_create(
        [
            Company(
                name=company_data['name'],
                location=company_data['location'],
                logo=company_data['logo'],
                description=company_data['description'],
                employee_count=company_data['employee_count'],
            )
            for company_data in companies_data[0:]
        ]
    )

    specialties = Specialty.objects.bulk_create(
        [
            Specialty(
                code=specialty_data['code'],
                title=specialty_data['title'],
                picture=specialty_data['picture']
            )
            for specialty_data in specialties_data[0:]
        ]
    )

    vacancies = Vacancy.objects.bulk_create(
        [
            Vacancy(
                title=vacancy_data['title'],
                specialty=vacancy_data['specialty'],
                company=vacancy_data['company'],
                description=vacancy_data['description'],
                salary_min=vacancy_data['salary_min'],
                salary_max=vacancy_data['salary_max'],
                published_at=vacancy_data['published_at']
            )
            for vacancy_data in vacancies_data[0:]
        ]
    )
