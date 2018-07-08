from django import forms
from django.forms import ModelForm, inlineformset_factory, BaseInlineFormSet
from .models import Client, ContactMessage, Order, OrderLine, Product


class ClientModelForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class EmailForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        widgets = {
            'client': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'recipient_email': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'add_comments': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Add any additional comments here!'})
        }
        fields = '__all__'


class OrderLineForm(forms.ModelForm):

    class Meta:
        model = OrderLine
        widgets = {
            'item': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        fields = (
            '__all__'
        )


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'po_number': forms.TextInput(attrs={'class': 'form-control'}),
            'order_status': forms.Select(attrs={'class': 'form-control'}),
        }
        fields = '__all__'


# class CustomOrderLineInlineFormset(BaseInlineFormSet):
#     def __init__(self, *args, **kwargs):
#         super(CustomOrderLineInlineFormset, self).__init__(*args, **kwargs)
#
#         for form in self.forms:
#             for field in form.fields:
#                 form.fields[field].attrs.update({'class': 'form-control'})


OrderLineInlineFormSet = inlineformset_factory(
    Order,
    OrderLine,
    fields=(
        'item',
        'quantity',
    ),
    extra=5,
    form=OrderLineForm,
)