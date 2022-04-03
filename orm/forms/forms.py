from django import forms
from django.forms import ModelForm
from datetime import datetime
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton, Div, InlineRadios, PrependedText, PrependedAppendedText
from crispy_forms import layout, bootstrap
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from .models import Students

class CollegeForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('forms:index_1')
        self.helper.form_method = 'POST'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
        Div(
            Div('name', css_class="col-sm-2 m-2"),
            Div('age', css_class="col-sm-2 m-2"),
            Div('subject', css_class="col-sm-2 m-2"),
            Div('date_of_birth', css_class="col-sm-2 m-2"),
            bootstrap.FormActions(
                layout.Submit('submit', 'Add', css_class='col-sm-2 m-2 btn btn-info')),
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
            attrs={'type':'date', 'max': datetime.now().date()}))

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


class SchoolForm(forms.Form):
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-10 mb-2'),
                Column('address_1', css_class='form-group col-10 mb-2'),
                Column('age', css_class='form-group col-10 mb-2'),
                Column('subject', css_class='form-group col-10 mb-2'),
                Column('date_of_birth', css_class='form-group col-10 mb-2'),
                css_class='form-row'
            ),
            Submit('submit', 'Sign in')
        )

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    address_1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    age = forms.IntegerField()
    subject = forms.ChoiceField(
        choices=SUBJECT_CHOICES, 
        widget=forms.RadioSelect())
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={'type':'date', 'max': datetime.now().date()}))    

class NewSchoolForm(forms.Form):
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('name', css_class='form-group col-6'),
                Div('address_1', css_class='form-group col-6'),
                css_class='form-row'
            ),
            Div(
                Div('address_2', css_class='form-group col-6'),
                Div('age', css_class='form-group col-6'),
                css_class='form-row'
            ),
            Div(
                Div('subject', css_class='form-group col-6'),
                Div('date_of_birth', css_class='form-group col-6'),
                css_class='form-row'
            ),
            Submit('submit', 'Sign up', css_class='mt-4')
        )

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    address_1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address1'}))
    address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address2'}))
    age = forms.IntegerField()
    subject = forms.ChoiceField(
        choices=SUBJECT_CHOICES, 
        widget=forms.RadioSelect())
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={'type':'date', 'max': datetime.now().date()}))  

class InlineForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    address_1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address1'}))
    age = forms.IntegerField()
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
                Column(PrependedText('name', '#')), 
                Column(PrependedAppendedText('address_1', '@'))
            ),
            Row(
                Column('age'),
                Column('date_of_birth')
            ),
            InlineRadios('subject'),
            Submit('submit', 'Sign up', css_class='mt-4')
        )

 
class CityForm(ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'address', 'age']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
        Div(
            Div('name', css_class="col-sm-2 m-2"),
            Div('address', css_class="col-sm-2 m-2"),
            Div('age', css_class="col-sm-2 m-2"),
            bootstrap.FormActions(
                layout.Submit('submit', 'Add', css_class='col-sm-2 m-2 btn btn-info')),
            css_class='row',))
        self.request = kwargs.pop('request', None)
        return super(CityForm, self).__init__(*args, **kwargs)

class NewStudsForm(ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'address', 'age']

    @property
    def helper(self):
        helper = FormHelper()

        for field in self.Meta().fields:
            helper.layout.append(
                Field(field)
            )
        
        helper.field_class = 'col-4'
        
        return helper

class AnotherForm(ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'address', 'age']

    def __init__(self, *args, **kwargs):
        super(AnotherForm, self).__init__()

        for field in self.fields:
            data = {
            'placeholder' : f'Student {str(field)}',
            'class' : 'col-sm-10 col-md-3'
            }
            self.fields[str(field)].widget.attrs.update(data)

class CreditCardForm(forms.Form):
    fullname = forms.CharField(label='Full Name', required=True)
    card_number = forms.CharField(label='Card', required=True, max_length=16)
    expire = forms.DateField(label='Expire Date', input_formats=['%m/%y'])
    csv = forms.IntegerField(label='CSV')
    notes = forms.CharField(label='Order Notes', widget=forms.Textarea())

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'
    helper.layout = Layout(
        Field('fullname', css_class='input-sm mb-2'),
        Field('card_number', css_class='input-sm mb-2'),
        Field('expire', css_class='input-sm mb-2'),
        Field('csv', css_class='input-sm mb-2'),
        Field('notes', rows=3),
        FormActions(Submit('purchase', 'purchase', css_class='btn-primary mt-2'))
    )

        
        


        

