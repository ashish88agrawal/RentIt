from django import forms

from RentItApp.models import Product_category


class NewProductForm(forms.Form):
    product_name = forms.CharField(label='Product Name', max_length=100, required='true',
                                   widget=forms.TextInput(
                                       attrs={'placeholder': 'Enter Product  Name..', 'class': 'form-control'}))

    product_title = forms.CharField(label='Product Title', max_length=100, required='true',
                                    widget=forms.TextInput(
                                        attrs={'placeholder': 'Enter Ad Title..', 'class': 'form-control'}))

    product_category = forms.CharField(label='First name', max_length=100, required='true',
                                       widget=forms.TextInput(
                                           attrs={'placeholder': 'First name', 'class': 'form-control input-lg'}))
    available_from = forms.DateField(required='true',
                                     widget=forms.DateInput(attrs={'id': 'example-datepicker2',
                                                                   'class': 'form-control input-datepicker date_box',
                                                                   'data-date-format': 'yyyy-mm-dd',
                                                                   'placeholder': 'yyyy/mm/dd'}))

    available_till = forms.DateField(required='true',
                                     widget=forms.DateInput(attrs={'id': 'example-datepicker2',
                                                                   'class': 'form-control input-datepicker date_box',
                                                                   'data-date-format': 'yyyy-mm-dd',
                                                                   'placeholder': 'yyyy/mm/dd'}))

    product_description = forms.CharField(label='First name', max_length=100, required='true',
                                          widget=forms.Textarea(
                                              attrs={'placeholder': 'product-description', 'rows': '3',
                                                     'class': 'form-control input-lg'}))

    product_conditions = forms.CharField(label='First name', max_length=100, required='true',
                                         widget=forms.Textarea(
                                             attrs={'placeholder': 'Conditions to renting out this product.',
                                                    'rows': '3', 'class': 'form-control input-lg'}))

    product_photo1 = forms.ImageField()

    choice = []
    choice = tuple(Product_category.objects.all().values_list())
    print choice
    product_category = forms.ChoiceField(choices=choice,
                                         widget=forms.Select(
                                             attrs={'placeholder': 'Conditions', 'class': 'select-chosen'}))


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
