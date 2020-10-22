from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

from app_vacancies.models import Company, Response


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = False


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('name', 'phone_number', 'mail')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = False


class SignupForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name')
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields.pop('password2')
        self.fields['password1'].help_text = ''
        self.helper = FormHelper()
        self.helper.form_show_labels = False


class CompanyForm(UserCreationForm):

    class Meta:
        model = Company

        fields = ('name', 'location', 'description', 'employee_count')
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить', css_class='btn-primary col-lg-12'))

        # включаем стили
        # self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
