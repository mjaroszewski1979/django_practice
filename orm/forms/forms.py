from django import forms
from datetime import datetime
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton, Div
from crispy_forms import layout, bootstrap
from crispy_forms.layout import Layout, Submit, Row, Column

'''class UniversityForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('forms:index')
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
        Div(
            Div('name', css_class="col-sm-2 m-2"),
            Div('age', css_class="col-sm-2 m-2"),
            Div('subject', css_class="col-sm-2 m-2"),
            Div('date_of_birth', css_class="col-sm-2 m-2"),
            bootstrap.FormActions(
                layout.Submit('submit', 'Add', css_class='col-sm-2 m-2 btn btn-primary')),
            css_class='row',
        )
    )


    SUBJECT_CHOICES = (
        (1, 'Web Development'),
        (2, 'Systems Programming'),
        (3, 'Data Science'),
    )

    name = forms.CharField()
    age = forms.IntegerField()
    subject = forms.ChoiceField(
        choices=SUBJECT_CHOICES, 
        widget=forms.RadioSelect())
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={'type':'date', 'max': datetime.now().date()}))'''

SUBJECT_CHOICES = (
        (1, 'Web Development'),
        (2, 'Systems Programming'),
        (3, 'Data Science'),
    )

class UniversityForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    age = forms.IntegerField()
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    subject = forms.ChoiceField(
        choices=SUBJECT_CHOICES, 
        widget=forms.RadioSelect())
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={'type':'date', 'max': datetime.now().date()}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-10 mb-2'),
                Column('age', css_class='form-group col-10 mb-2'),
                Column('addresss_1', css_class='form-group col-10 mb-2'),
                Column('subject', css_class='form-group col-10 mb-2'),
                Column('date_of_birth', css_class='form-group col-10 mb-2'),
                css_class='form-row'
            ),
            Submit('submit', 'Sign in')
        )

