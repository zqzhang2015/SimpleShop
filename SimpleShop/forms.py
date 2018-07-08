from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Client, ContactMessage, Order, OrderLine


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
        fields = '__all__'


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'


OrderLineInlineFormSet = inlineformset_factory(
    Order,
    OrderLine,
    fields=(
        'item',
        'quantity',
    ),
    extra=1,
)