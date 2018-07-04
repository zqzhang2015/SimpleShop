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
        fields = ('receiver_email', 'text_body',)


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
    extra=3,
)