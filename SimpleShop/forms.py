from django import forms
from django.forms import ModelForm, inlineformset_factory, BaseInlineFormSet
from .models import Client, ContactMessage, Order, OrderLine, Product


class ContactMe(forms.Form):
    your_email = forms.EmailField(
        label='Your Email',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email Address',
                'class': 'form-control',
            }
        )
    )
    your_name = forms.CharField(
        label='Your Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Full Name',
                'class': 'form-control',
            }
        )
    )
    subject = forms.CharField(
        label='Subject',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Subject Line',
                'class': 'form-control',
            }
        )
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Your message goes here!',
                'class': 'form-control',
            }
        )
    )


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


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = [
            'create_date',
            'modify_date',
        ]
        widgets = {
            'product_id': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sale_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ClientModelForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email_address': forms.TextInput(attrs={'class': 'form-control'}),
        }

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