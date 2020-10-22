from crispy_forms.helper import FormHelper
from django import forms

from app_vacancies.models import Company, Vacancy, Specialty, Resume


class CreateCompanyForm(forms.ModelForm):
    # name = forms.CharField(label='Название компании', required=False)
    # location = forms.CharField(label='География', required=False)
    # employee_count = forms.IntegerField(label='Количество человек в компании', required=False)
    # description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label='Информация о компании',
    #                               required=False)
    # logo = forms.ImageField(required=False)

    class Meta:
        model = Company
        fields = ('name', 'location', 'logo', 'description', 'employee_count')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['logo'].required = False


class EditVacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ('title', 'skills', 'description', 'salary_min', 'salary_max', 'specialty')
        speciality = forms.ModelChoiceField(queryset=Specialty.objects.all(), to_field_name="hvvsdhhvsd")
        widgets = {
            'skills': forms.Textarea(attrs={'rows': 4}),
            'description': forms.Textarea(attrs={'rows': 7}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = False

    def __str__(self):
        return self.title


class EditResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        SEMESTER_CHOICES = (
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
            ("6", "6"),
            ("7", "7"),)

        fields = ('firstname', 'secondname', 'job_status', 'waiting_salary', 'specialty', 'qualification',
                  'education', 'work_experience', 'portfolio_link')
        speciality = forms.ModelChoiceField(queryset=Specialty.objects.all())
        widgets = {
            'education': forms.Textarea(attrs={'rows': 4}),
            'work_experience': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = False

    def __str__(self):
        return self.title
