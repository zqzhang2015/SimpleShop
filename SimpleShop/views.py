from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from .models import Client, Product, Order
from .forms import EmailForm, OrderForm, OrderLineInlineFormSet
from django.template.loader import get_template
from django.core.mail import send_mail
from .tasks import send_email
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact_view(request):
    form_class = EmailForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_email = request.POST.get('client_email', '')
            form_content = request.POST.get('text_body', '')

            template = get_template('contact_template.txt')
            context = {
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)
            send_mail(
                'Contact Form Submission',
                content,
                'sender@example.com',
                ['dangjoeltang@gmail.com']
            )
            messages.success(request, 'Email has been submitted!')
            return redirect('contact')
    return render(request, 'contact.html', {'form': form_class})

def preview_email(request, pk):
    client_query = Client.objects.get(id=pk)
    orders_query = client_query.order_set.all()

    body_string = ""
    for order in orders_query:
        body_string += "PO Number: {}\n".format(order.po_number)
        for line in order.order_items.all():
            body_string += "- {} x {}\n".format(line.quantity, line.item)

        body_string += "\n"

    form_class = EmailForm(initial={
        'client': client_query.id,
        'recipient_email': client_query.email_address,
        'subject': "Report for " + client_query.first_name + " " + client_query.last_name,
        'body': body_string,
    })

    if request.method == 'POST':
        form = EmailForm(request.POST)
        form.client = pk
        if form.is_valid():
            form.save()
            recipient_email = request.POST.get('recipient_email')
            subject = request.POST.get('subject')
            body = request.POST.get('body')
            additional = request.POST.get('add_comments')

            template = get_template('email_report_template.txt')
            context = {
                'recipient_email': recipient_email,
                'subject': subject,
                'body': body,
                'additional': additional,
            }
            content = template.render(context)

            send_email.delay(recipient_email, content)
            messages.success(request, 'Email has been submitted!')
            return redirect('client-detail', pk=pk)

        messages.error(request, 'Invalid form, please check again.', extra_tags='html_safe alert alert-danger')
        return redirect('preview-email', pk=pk)
        # ADD SOMETHING HERE TO SHOW FORM VALIDATION FAILED

    context = {
        'client': client_query,
        'orders': orders_query,
        'form': form_class,
    }
    return render(request, 'preview_email.html', context)


def client_orders_view(request, pk):
    client = Client.objects.get(id=pk)
    orders = client.order_set.all()
    return render(request, 'client_orders.html', {'client': client, 'orders': orders})


def create_order(request):

    order = Order()

    if request.method == "POST":
        order_form = OrderForm(request.POST)

        formset = OrderLineInlineFormSet(request.POST, request.FILES)

        if order_form.is_valid():
            created_order = order_form.save(commit=False)
            formset = OrderLineInlineFormSet(request.POST, request.FILES, instance=created_order)

            if formset.is_valid():
                created_order.save()
                formset.save()
                messages.success(request, 'Order saved successfully!')
                return redirect('order-list')

    else:
        order_form = OrderForm(instance=order)
        formset = OrderLineInlineFormSet()

    return render(request, "SimpleShop/order_create.html", {
        "order_form": order_form,
        "formset": formset,
    })


def edit_order(request, pk):
    if id:
        order = Order.objects.get(pk=pk)
    else:
        order = Order()

    order_form = OrderForm(instance=order)  # setup a form for the parent
    formset = OrderLineInlineFormSet(instance=order)

    if request.method == "POST":
        order_form = OrderForm(request.POST)

        if id:
            order_form = OrderForm(request.POST, instance=order)

        formset = OrderLineInlineFormSet(request.POST, request.FILES)

        if order_form.is_valid():
            created_order = order_form.save(commit=False)
            formset = OrderLineInlineFormSet(request.POST, request.FILES, instance=created_order)

            if formset.is_valid():
                created_order.save()
                formset.save()
                messages.success(request, 'Order saved successfully!')

                return redirect('order-list')

    return render(request, "SimpleShop/order_update.html", {
        "order_id": order.id,
        "order_form": order_form,
        "formset": formset,
    })


def client_list_view(request):
    clients = Client.objects.all()
    return render(request, 'clientList.html', {'clients': clients})


def product_list_view(request):
    product_query = Product.objects.all()
    context = {
        'products': product_query
    }
    return render(request, 'productList.html', context)


def orders_view(request):
    orders = Order.objects.all()
    return render(request, 'orderList.html', {'orders': orders})


def client_detail_view(request):
    return render(request, 'clientDetail.html')


def error_404(request):
    context = {}
    return render(request, 'error_404.html', context)


# CLIENT CRUD
class ClientCreate(CreateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('client-list')


class ClientUpdate(UpdateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('client-list')


class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('client-list')


# PRODUCT CRUD
class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product-list')


class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product-list')


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product-list')


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('order-list')