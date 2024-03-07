from datetime import timedelta

from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .models import MyUser, Purchase, Product, Return
from .forms import PurchaseCreateForm, ProductCreateForm, NewUserForm, ReturnForm
from django.shortcuts import get_object_or_404
from .mixins.myapp.mixins import SuperuserRequiredMixin


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'home.html'
    login_url = 'login/'


class Login(LoginView):
    template_name = 'login.html'
    success_url = '/'

    def get_success_url(self):
        return self.success_url


class Register(CreateView):
    form_class = NewUserForm
    model = MyUser
    template_name = "registration.html"
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.purse = 2000
        user.save()
        return super().form_valid(form)


class Logout(LoginRequiredMixin, LogoutView):
    login_url = 'home'
    next_page = '/'


class ProductCreateView(SuperuserRequiredMixin, CreateView):
    template_name = "create.html"
    login_url = 'login/'
    http_method_names = ['get', 'post']
    form_class = ProductCreateForm
    success_url = '/'


class ProductUpdateView(SuperuserRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'image', 'quantity']
    template_name = 'update.html'
    success_url = '/'
    context_object_name = 'obj'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'detail.html'
    login_url = 'login/'
    context_object_name = 'obj'
    extra_context = {'create_form': PurchaseCreateForm}


class PurchaseCreateView(CreateView):
    template_name = 'detail.html'
    login_url = 'login/'
    http_method_names = ['get', 'post']
    form_class = PurchaseCreateForm
    success_url = 'my_profile/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.buyer = self.request.user
        product_pk = self.kwargs['pk']
        product_instance = get_object_or_404(Product, pk=product_pk)
        obj.product = product_instance
        obj.save()
        return super().form_valid(form=form)


class PurchaseListView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = 'profile.html'
    context_object_name = 'purchase'
    login_url = 'login/'
    extra_context = {'create_form': ReturnForm}

    def get_queryset(self):
        user = self.request.user
        queryset = Purchase.objects.filter(buyer=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=product_pk)
        context['product'] = product
        price = product.price
        context['price'] = price
        user = self.request.user
        purse = user.purse
        for obj in context['purchase']:
            if obj.quantity_of_product is not None:
                obj.total_amount = obj.quantity_of_product * price
            else:
                obj.total_amount = 0
            context['enough_money'] = purse >= obj.total_amount
        return context


class PurchaseListAdminView(SuperuserRequiredMixin, ListView):
    model = Purchase
    template_name = 'purchases.html'
    context_object_name = 'purchases'
    login_url = 'login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        purchases = context['purchases']
        for purchase in purchases:
            # Рассчитываем общую сумму каждой покупки
            total_amount = purchase.quantity_of_product * purchase.product.price
            purchase.total_amount = total_amount
        return context


class ReturnCreateView(LoginRequiredMixin, CreateView):
    template_name = 'profile.html'
    login_url = 'login/'
    http_method_names = ['get', 'post']
    form_class = ReturnForm
    model = Return
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        purchase_pk = self.kwargs.get('pk')
        purchase = get_object_or_404(Purchase, pk=purchase_pk)
        allowed_return_window = purchase.created_at + timedelta(seconds=3)
        allowed_return = timezone.now() < allowed_return_window
        context['allowed_return'] = allowed_return
        return context

