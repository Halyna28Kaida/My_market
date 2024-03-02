from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .models import MyUser, Purchase
from .forms import PurchaseCreateForm
from django.shortcuts import get_object_or_404
# from django.db.models.signals import post_save
# from django.dispatch import receiver


from myapp.models import Product
from myapp.forms import ProductCreateForm, NewUserForm
from myapp.mixins.myapp.mixins import SuperuserRequiredMixin


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
    success_url = '/'

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
    context_object_name = 'obj'
    login_url = 'login/'




