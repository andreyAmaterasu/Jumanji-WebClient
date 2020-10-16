from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Column
from django.forms import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField


class CreateCompanyForm(forms.Form):
    name = forms.CharField(label='Название компании', required=False)
    location = forms.CharField(label='География', required=False)
    employee_count = forms.IntegerField(label='Количество человек в компании', required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label='Информация о компании',
                                  required=False)
    logo = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = False
